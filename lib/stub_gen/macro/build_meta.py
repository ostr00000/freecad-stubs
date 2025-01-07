from dataclasses import dataclass, field
from datetime import UTC, datetime
from functools import cached_property
from pathlib import Path

from dataclass_binder import Binder
from git import Repo


@dataclass
class BuildMeta:
    gitPath: Path
    buildDir: Path
    metaFile: Path
    revision: str
    start_datetime: datetime
    save_datetime: datetime | None = field(default=None)

    @classmethod
    def getBuildDir(cls, gitPath: Path):
        return gitPath / 'cpp_ast_build'

    @classmethod
    def load(cls, gitPath: Path):
        buildDir = cls.getBuildDir(gitPath)
        metaFile = buildDir / 'metadata.toml'
        if metaFile.exists():
            try:
                return Binder(cls).parse_toml(metaFile)
            except (TypeError, ValueError):
                pass

        repo = Repo(gitPath)
        revision = repo.head.commit.hexsha

        return BuildMeta(
            gitPath=gitPath,
            buildDir=buildDir,
            metaFile=metaFile,
            revision=revision,
            start_datetime=datetime.now(tz=UTC),
        )

    def save(self):
        self.buildDir.mkdir(parents=True, exist_ok=True)
        with self.metaFile.open('w') as f:
            for line in Binder(self).format_toml():
                f.write(line + '\n')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, _exc_val, _exc_tb):
        if exc_type is not None:
            return

        self.end_datetime = datetime.now(UTC)
        self.revision = self.gitCurrentRevision
        self.save()

    @cached_property
    def gitRepo(self):
        return Repo(self.gitPath)

    @cached_property
    def gitCurrentRevision(self):
        return self.gitRepo.head.commit.hexsha

    def isRevChanged(self):
        return self.gitCurrentRevision != self.revision

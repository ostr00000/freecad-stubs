import logging
import shutil
from pathlib import Path

from stub_gen.decorators import logCurrentTaskDecFactory
from stub_gen.macro.build_meta import BuildMeta

logger = logging.getLogger(__name__)


@logCurrentTaskDecFactory()
def cleanBuildDir(gitPath: Path):
    buildDir = BuildMeta.getBuildDir(gitPath)
    logger.debug(f"Removing: {buildDir}")
    shutil.rmtree(buildDir)


@logCurrentTaskDecFactory()
def generateIntermediateFiles(gitPath: Path):
    if not gitPath.exists():
        raise FileNotFoundError

    with BuildMeta.load(gitPath) as bm:
        if bm.isRevChanged():
            cleanBuildDir(gitPath)

        raise NotImplementedError

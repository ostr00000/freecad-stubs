from functools import lru_cache
from subprocess import check_output

from freecad_stub_gen.config import FREECAD_DIR

LAST_HASH_PATH = FREECAD_DIR / 'freecad_stub_gen.last_hash'


@lru_cache(maxsize=1)
def getCurrentGitHash() -> str:
    args = ['git', 'rev-parse', 'HEAD']
    output = check_output(  # noqa: S603
        # Please trust me - this is call with `LiteralStr`!
        args,
        cwd=FREECAD_DIR,
        text=True,
    )
    return output.strip()


def getOldGitHash() -> str:
    return LAST_HASH_PATH.read_text() if LAST_HASH_PATH.exists() else ''


def isNewGitHead() -> bool:
    return getCurrentGitHash() != getOldGitHash()


def updateGitHashToCurrent():
    curHash = getCurrentGitHash()
    LAST_HASH_PATH.write_text(curHash)

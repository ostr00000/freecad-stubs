import io
import logging
from pathlib import Path

from joblib import Parallel, delayed

from freecad_stub_gen.config import SOURCE_DIR
from freecad_stub_gen.cpp_code.macro.file_preparation import (
    fixPath,
    getContentForOriginalFile,
    readContentForPreprocess,
    removeEmptyLines,
)
from freecad_stub_gen.cpp_code.macro.preprocessor import SaveErrorsPreprocessor
from freecad_stub_gen.debug_functions import genFilesWithLog, timeDec
from freecad_stub_gen.file_functions import genFilesToPreprocess

logger = logging.getLogger(__name__)


def processFile(filePath: Path) -> list[str]:
    outFile = filePath.with_suffix(filePath.suffix + '.ii')
    if outFile.exists():
        logger.info(f"File `{filePath}` exists - skipping")
        return []

    logger.debug(f"Processing: {filePath=}")
    pre = SaveErrorsPreprocessor()
    pre.add_path(str(SOURCE_DIR))

    content = readContentForPreprocess(filePath)
    pre.parse(content, str(filePath))

    macroContent = io.StringIO()
    pre.write(macroContent)
    macroContent.seek(0)

    if pre.errors:
        return list(pre.errors)

    fixedPath = fixPath(pre, filePath)
    onlyCurrentFileContent = getContentForOriginalFile(str(fixedPath), macroContent)
    outFile.write_text(removeEmptyLines(onlyCurrentFileContent))
    return []


def _genTasks():
    dpf = delayed(processFile)
    for filePath in genFilesWithLog(genFilesToPreprocess, desc="Generate macros"):
        yield dpf(filePath)


@timeDec
def generatePreprocessedFiles():
    with Parallel(n_jobs=-1, return_as='generator') as p:
        allErrors = [e for errors in p(_genTasks()) if errors for e in errors]

    for e in allErrors:
        logger.error(e)

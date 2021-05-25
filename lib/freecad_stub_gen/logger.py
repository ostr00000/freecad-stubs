import logging


def logFilter(record: logging.LogRecord) -> bool:
    key = (record.module, record.levelno, record.msg)
    if key in logFilter.seen:
        return False
    logFilter.seen.add(key)
    return True


logFilter.seen = set()


def configLogFilter(loggerName=None):
    for h in logging.getLogger(loggerName).handlers:
        h.addFilter(logFilter)


LEVEL_CODE = 5
LEVEL_NAME_CODE = 'CODE'
logging.addLevelName(LEVEL_CODE, LEVEL_NAME_CODE)

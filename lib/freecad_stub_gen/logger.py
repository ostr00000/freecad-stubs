import logging


class RepeatedFilter(logging.Filter):
    def __init__(self, name=''):
        super().__init__(name)
        self.seen = set()

    def filter(self, record: logging.LogRecord) -> bool:
        key = (record.module, record.levelno, record.msg)
        if key in self.seen:
            return False
        self.seen.add(key)
        return True


LEVEL_CODE = 5
LEVEL_NAME_CODE = 'CODE'
logging.addLevelName(LEVEL_CODE, LEVEL_NAME_CODE)

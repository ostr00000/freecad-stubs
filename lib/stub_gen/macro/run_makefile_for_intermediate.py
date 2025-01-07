import concurrent.futures
import logging
import os
import re
import shlex
from collections.abc import Iterator
from pathlib import Path
from subprocess import check_call

import typed_argparse as tap

logger = logging.getLogger(__name__)
INTERMEDIATE_RULE = re.compile(r'(?P<rule_name>\w+\.i):.*')


def generateRules(makefile: Path) -> Iterator[str]:
    content = makefile.read_text()
    for line in content.splitlines():
        if match := INTERMEDIATE_RULE.match(line):
            yield match.group('rule_name')


def generateCommands(gitPath: Path) -> Iterator[list[str]]:
    for mkPath in gitPath.rglob('Makefile'):
        for rule in generateRules(mkPath):
            yield ['make', '--file', str(mkPath), rule]


class PatchCmakeArgs(tap.TypedArgs):
    repo_path: Path = tap.arg(help="Git project with C++ code.")

    def fixArguments(self):
        self.repo_path = self.repo_path.expanduser().resolve()


def runProcess(cmd: list[str]):
    logger.info(f"Running: {shlex.join(cmd)}")
    check_call(cmd)  # noqa: S603


def runner(args: PatchCmakeArgs):
    args.fixArguments()

    cc = os.cpu_count() or 1
    max_workers = max(cc - 2, 1)
    with concurrent.futures.ThreadPoolExecutor(max_workers) as executor:
        futures = [
            executor.submit(runProcess, cmd) for cmd in generateCommands(args.repo_path)
        ]

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception:
                logger.exception("An error occurred in process")


def main():
    logging.basicConfig(level=logging.DEBUG)
    tap.Parser(PatchCmakeArgs).bind(runner).run()


if __name__ == '__main__':
    main()

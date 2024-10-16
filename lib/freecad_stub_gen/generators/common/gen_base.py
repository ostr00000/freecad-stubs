import contextvars
from abc import ABC, ABCMeta
from pathlib import Path
from typing import Any, Self
from xml.etree.ElementTree import ParseError

from freecad_stub_gen.generators.common.context import (
    currentPath,
    currentSource,
    initContext,
    requiredImports,
)
from freecad_stub_gen.ordered_set import OrderedStrSet
from freecad_stub_gen.python_code.module_container import Module


class BaseGeneratorMeta(ABCMeta, type):
    def __new__(cls, name, bases, namespace: dict[str, Any], **kw):
        if getStub := namespace.get('getStub'):

            def getStubPrepare(self, *args, **kwargs):
                return self.context.run(getStub, self, *args, **kwargs)

            namespace['getStub'] = getStubPrepare

        return super().__new__(cls, name, bases, namespace, **kw)


class BaseGenerator(ABC, metaclass=BaseGeneratorMeta):
    @classmethod
    def safeCreate(cls: type[Self], *args, **kwargs) -> Self | None:
        try:
            return cls(*args, **kwargs)
        except (FileNotFoundError, ParseError):
            return None

    def __init__(self, filePath: Path, sourceDir: Path):
        self.sourceDir = sourceDir
        self.context = contextvars.Context()
        self.context.run(initContext, filePath)
        self.context.run(self.postInit)

    def postInit(self):
        pass

    @property
    def impContent(self):
        return currentSource.get()

    @property
    def baseGenFilePath(self):
        return currentPath.get()

    @property
    def requiredImports(self):
        return requiredImports.get()

    @requiredImports.setter
    def requiredImports(self, value: OrderedStrSet):
        requiredImports.set(value)

    def getStub(self, mod: Module, moduleName: str):
        """Generate stub file for module `mod`.

        An argument `moduleName` may be optionally used if the generator
        cannot determine correct package.
        """
        raise NotImplementedError

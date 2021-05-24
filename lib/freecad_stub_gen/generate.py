import logging
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path

from freecad_stub_gen.config import SOURCE_DIR, GEN_DIR, TARGET_DIR
from freecad_stub_gen.generators.from_methods import FreecadStubGeneratorFromMethods
from freecad_stub_gen.generators.from_xml import FreecadStubGeneratorFromXML
from freecad_stub_gen.module_map import genXmlFiles, genPyCppFiles

logger = logging.getLogger(__name__)



def generateFreeCadStubs(sourcePath=SOURCE_DIR, genPath=GEN_DIR, targetPath=TARGET_DIR):
    sourcePath = sourcePath.resolve()
    genPath = genPath.resolve()
    targetPath = targetPath.resolve()

    for i, xmlPath in enumerate(genXmlFiles(sourcePath)):
        if not (tg := FreecadStubGeneratorFromXML.safeCreate(xmlPath, sourcePath)):
            continue

        typingPath = genPath / xmlPath.relative_to(sourcePath)
        typingPath = typingPath.with_stem(typingPath.stem.removesuffix('Py')).with_suffix('.pyi')
        try:
            tg.generateToFile(typingPath)
        except ET.ParseError:
            continue

    for cppPath in genPyCppFiles(sourcePath):
        if not (methodGen := FreecadStubGeneratorFromMethods.safeCreate(cppPath, sourcePath)):
            continue

        funcFile = genPath / cppPath.relative_to(sourcePath).with_suffix('.pyi')
        funcFile = funcFile.with_stem(funcFile.stem + '__functions')
        methodGen.generateToFile(funcFile)

    _generateUnits(genPath / 'Base' / 'Units.pyi')
    _generateConsole(genPath / 'Base' / 'Console.pyi')
    _generatePythonBase(genPath / 'Base' / 'PyObject.pyi')
    _prepareStructure(genPath, targetPath)
    _addDynamicVariablesToInit(targetPath / 'FreeCAD/__init__.py')

    # TODO P4 preprocess and remove macros
    # https://www.tutorialspoint.com/cplusplus/cpp_preprocessor.htm


def _generatePythonBase(pythonBaseFile: Path):
    assert any('PyObject' in p for p in pythonBaseFile.parts)
    pythonBase = 'class PyObjectBase(object): ...'
    with open(pythonBaseFile, 'w') as file:
        file.write(pythonBase)


def _generateUnits(pythonUnitsFile: Path):
    with open(pythonUnitsFile, 'w') as file:
        file.write('from FreeCAD.Unit import Unit\n')
        file.write('from FreeCAD.Quantity import Quantity\n\n')
        file.write('Quantity = Quantity\n')
        file.write('Unit = Unit\n')


def _generateConsole(pythonConsoleFile: Path):
    with open(pythonConsoleFile, 'w') as file:
        file.write('from FreeCAD.Console__functions import *')


def _addDynamicVariablesToInit(targetPath: Path):
    content = """
GuiUp: int  # but only 0 or 1
Workbench: Gui.Workbench
ActiveDocument: Document
"""
    with open(targetPath, 'a') as file:
        file.write(content)


def _prepareStructure(genPath: Path = GEN_DIR, targetPath: Path = TARGET_DIR):
    shutil.rmtree(targetPath, ignore_errors=True)

    shutil.copytree(genPath / 'Base', targetPath / 'FreeCAD')
    shutil.copytree(genPath / 'App', targetPath / 'FreeCAD', dirs_exist_ok=True)
    for componentPath in genPath.iterdir():
        if componentPath.name not in ('App', 'Mod'):
            targetComponentPath = targetPath / 'FreeCAD' / componentPath.name
            shutil.copytree(componentPath, targetComponentPath)
            _createInitForModules(targetComponentPath)

    _createInitForModules(targetPath / 'FreeCAD')

    for modPath in (genPath / 'Mod').iterdir():
        targetModPath = targetPath / modPath.name

        if (modPath / 'Base').exists():
            shutil.copytree(modPath / 'Base', targetModPath)
        if (modPath / 'App').exists():
            shutil.copytree(modPath / 'App', targetModPath, dirs_exist_ok=True)
        _createInitRecursive(targetModPath)


def _createInitForModules(packagePath: Path, genClassImport=True):
    if not packagePath.exists():
        return

    initFilePath = packagePath / '__init__.py'
    if genClassImport:
        modules = sorted((
            mod for mod in packagePath.iterdir()
            if ((mod.is_file() and mod.suffix == '.pyi')
                or (mod.is_dir() and (mod / '__init__.py').exists()))
        ), key=lambda p: (p.is_file(), p))
        with open(initFilePath, 'w') as initFile:
            for modulePath in modules:
                if modulePath.is_file():
                    initFile.write(f'from .{modulePath.stem} import *\n')
                elif modulePath.is_dir():
                    initFile.write(f'from . import {modulePath.stem}\n')
                else:
                    raise NotImplementedError

    else:
        initFilePath.touch(exist_ok=True)


def _createInitRecursive(packagePath: Path):
    try:
        for module in packagePath.iterdir():
            if module.is_dir():
                _createInitRecursive(module)

        _createInitForModules(packagePath, genClassImport=True)
    except FileNotFoundError as fnf:
        logger.warning(fnf)


def _redirectModule(packagePath: Path, moduleName: str):
    modulePath = packagePath / moduleName
    if modulePath.exists():
        with open(packagePath / '__init__.py', 'a') as file:
            file.write(f'from {moduleName} import *\n')

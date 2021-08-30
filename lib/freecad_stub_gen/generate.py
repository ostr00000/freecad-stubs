import logging
import shutil
from pathlib import Path

from freecad_stub_gen.additional import additionalPath
from freecad_stub_gen.config import SOURCE_DIR, TARGET_DIR
from freecad_stub_gen.generators.from_cpp.functions import FreecadStubGeneratorFromCppFunctions
from freecad_stub_gen.generators.from_cpp.klass import FreecadStubGeneratorFromCppClass
from freecad_stub_gen.generators.from_cpp.module import FreecadStubGeneratorFromCppModule
from freecad_stub_gen.generators.from_xml import FreecadStubGeneratorFromXML
from freecad_stub_gen.module_map import genXmlFiles, genPyCppFiles
from freecad_stub_gen.stub_container import StubContainer

logger = logging.getLogger(__name__)


def _genModule(moduleName: str, modulePath: Path, sourcePath=SOURCE_DIR):
    moduleStub = StubContainer(name=moduleName)

    for xmlPath in genXmlFiles(modulePath):
        if not (tg := FreecadStubGeneratorFromXML.safeCreate(xmlPath, sourcePath)):
            continue
        moduleStub += tg.getStub()

    for cppPath in genPyCppFiles(modulePath):
        for cl in (FreecadStubGeneratorFromCppFunctions,
                   FreecadStubGeneratorFromCppClass,
                   FreecadStubGeneratorFromCppModule):
            if not (mg := cl.safeCreate(cppPath, sourcePath)):
                continue

            if stub := mg.getStub():
                # this is special case when we create separate module
                sp = ('Selection', 'Console', 'Translate',
                      'UnitsApiPy', 'TaskDialogPython')
                if cppPath.stem in sp:
                    subCon = StubContainer(name=cppPath.stem)
                    subCon += stub
                    moduleStub /= subCon
                else:
                    moduleStub += stub

    return moduleStub


def generateFreeCadStubs(sourcePath=SOURCE_DIR, targetPath=TARGET_DIR):
    rootStub = StubContainer()

    freeCADStub = StubContainer('class PyObjectBase(object): ...\n\n', name='FreeCAD')
    freeCADBase = _genModule('Base', sourcePath / 'Base', sourcePath)
    freeCADStub.moveSubContainersFrom(freeCADBase)
    freeCADStub /= freeCADBase

    freeCADStub += _genModule('FreeCAD', sourcePath / 'App', sourcePath)
    freeCADStub += """
App = FreeCAD
Log = FreeCAD.Console.PrintLog
Msg = FreeCAD.Console.PrintMessage
Err = FreeCAD.Console.PrintError
Wrn = FreeCAD.Console.PrintWarning
# be careful with following variables -
# some of them are set in FreeCADGui (GuiUp after InitApplications),
# so may not exist when accessible until FreeCADGuiInit is initialized - use `getattr`"""
    freeCADStub += StubContainer('GuiUp: typing.Literal[0, 1]', {'typing'})
    freeCADStub += StubContainer('Gui = FreeCADGui', {'FreeCADGui'})
    freeCADStub += StubContainer('ActiveDocument: FreeCAD.Document')
    freeCADStub += StubContainer(requiredImports={
        'FreeCAD.Console',
        'FreeCAD.__Translate__ as Qt',
        'FreeCAD.UnitsApiPy as Units',
        'FreeCAD.Base',
        'from FreeCAD.Base import *'})
    rootStub @= freeCADStub

    freeCADGuiStub = _genModule('FreeCADGui', sourcePath / 'Gui')
    freeCADGuiStub += StubContainer('Workbench: FreeCADGui.Workbench')
    freeCADGuiStub += StubContainer('ActiveDocument: FreeCADGui.Document')
    freeCADGuiStub += StubContainer(
        'Control = ControlClass()  # hack to show this module in current module hints')
    freeCADGuiStub += StubContainer(requiredImports={
        'FreeCADGui.Selection',
        'from FreeCADGui.TaskDialogPython import Control as ControlClass'})
    rootStub @= freeCADGuiStub

    for mod in (sourcePath / 'Mod').iterdir():
        if mod.name in ('Test',):
            continue

        ms = _genModule(mod.name, mod / 'App', sourcePath)
        ms += _genModule(mod.name, mod / 'Gui', sourcePath)
        rootStub @= ms

    rootStub.makeSiblingContainersAsPackage()

    shutil.rmtree(targetPath, ignore_errors=True)
    targetPath.mkdir(parents=True, exist_ok=True)
    (targetPath / '__init__.pyi').touch(exist_ok=True)
    rootStub.save(targetPath)

    for stubPackage in targetPath.iterdir():
        if stubPackage.is_dir():
            stubPackage.rename(stubPackage.with_name(stubPackage.name + '-stubs'))

    for additionalPackage in additionalPath.glob('[!_]*.py'):
        targetAdditionalPackage = targetPath / additionalPackage.stem
        targetAdditionalPackage.mkdir()
        shutil.copy(additionalPackage, targetAdditionalPackage / '__init__.py')

# TODO P4 preprocess and remove macros
# https://www.tutorialspoint.com/cplusplus/cpp_preprocessor.htm

import inspect
import logging
import shutil
from pathlib import Path

from freecad_stub_gen.additional import additionalPath
from freecad_stub_gen.config import SOURCE_DIR, TARGET_DIR
from freecad_stub_gen.generators.from_cpp.functions import FreecadStubGeneratorFromCppFunctions
from freecad_stub_gen.generators.from_cpp.klass import FreecadStubGeneratorFromCppClass
from freecad_stub_gen.generators.from_cpp.module import FreecadStubGeneratorFromCppModule
from freecad_stub_gen.generators.from_xml.full import FreecadStubGeneratorFromXML
from freecad_stub_gen.module_container import Module
from freecad_stub_gen.module_namespace import moduleNamespace
from freecad_stub_gen.util import genPyCppFiles, genXmlFiles

logger = logging.getLogger(__name__)


def addExceptions(sourcesRoot: Module):
    base = sourcesRoot['FreeCAD.Base']
    base += inspect.cleandoc("""
class FreeCADError(RuntimeError):
    pass


class FreeCADAbort(BaseException):
    pass
    """) + '\n'
    part = sourcesRoot['Part']
    part += inspect.cleandoc("""
class OCCError(FreeCAD.Base.FreeCADError):
    pass


class OCCDomainError(OCCError):
    pass


class OCCRangeError(OCCDomainError):
    pass


class OCCConstructionError(OCCDomainError):
    pass


class OCCDimensionError(OCCDomainError):
    pass
    """) + '\n'


def _genModule(sourcesRoot: Module, modulePath: Path, sourcePath=SOURCE_DIR,
               moduleName='', subModuleName=''):
    for xmlPath in genXmlFiles(modulePath):
        if not (tg := FreecadStubGeneratorFromXML.safeCreate(xmlPath, sourcePath)):
            continue
        tg.getStub(sourcesRoot, moduleName, submodule=subModuleName)

    for cppPath in genPyCppFiles(modulePath):
        for cl in (FreecadStubGeneratorFromCppFunctions,
                   FreecadStubGeneratorFromCppClass,
                   FreecadStubGeneratorFromCppModule):
            if not (mg := cl.safeCreate(cppPath, sourcePath)):
                continue

            match cppPath.stem:
                # this is special case when we create separate module
                case 'Translate':
                    curModuleName = f'{moduleName}.Qt'
                case 'UnitsApiPy':
                    curModuleName = f'{moduleName}.Units'
                case ('Selection' | 'Console' | 'TaskDialogPython') as stem:
                    curModuleName = f'{moduleName}.{stem}'
                case _:
                    curModuleName = moduleName

            mg.getStub(sourcesRoot, curModuleName)


def generateFreeCadStubs(sourcePath=SOURCE_DIR, targetPath=TARGET_DIR):
    sourcesRoot = Module()

    freeCad = sourcesRoot['FreeCAD']
    freeCad += 'class PyObjectBase(object): ...\n\n\n'

    _genModule(sourcesRoot, sourcePath / 'Base', sourcePath,
               moduleName='FreeCAD', subModuleName='Base')
    _genModule(sourcesRoot, sourcePath / 'App', sourcePath,
               moduleName='FreeCAD')

    freeCad += """
App = FreeCAD
Log = FreeCAD.Console.PrintLog
Msg = FreeCAD.Console.PrintMessage
Err = FreeCAD.Console.PrintError
Wrn = FreeCAD.Console.PrintWarning
# be careful with following variables -
# some of them are set in FreeCADGui (GuiUp after InitApplications),
# so may not exist when accessible until FreeCADGuiInit is initialized - use `getattr`"""
    freeCad += 'GuiUp: typing.Literal[0, 1]'
    freeCad.imports.add('typing')
    freeCad += 'Gui = FreeCADGui'
    freeCad.imports.add('FreeCADGui')
    freeCad += 'ActiveDocument: FreeCAD.Document'
    freeCad.imports.update((
        'FreeCAD.Console',
        'FreeCAD.Qt as Qt',
        'FreeCAD.Units as Units',
        'FreeCAD.Base',
        'from FreeCAD.Base import *'))

    _genModule(sourcesRoot, sourcePath / 'Gui', sourcePath, moduleName='FreeCADGui')
    _genModule(sourcesRoot, sourcePath / 'Main', sourcePath, moduleName='FreeCADGui')
    freeCadGui = sourcesRoot['FreeCADGui']
    freeCadGui += 'Workbench: FreeCADGui.Workbench'
    freeCadGui += 'ActiveDocument: FreeCADGui.Document'
    freeCadGui += 'Control = ControlClass()  # hack to show this module in current module hints'
    freeCadGui.imports.update((
        'FreeCADGui.Selection',
        'from FreeCADGui.TaskDialogPython import Control as ControlClass'))

    for mod in (sourcePath / 'Mod').iterdir():
        moduleName = mod.name
        if moduleName in ('Test',):
            continue

        moduleName = moduleNamespace.convertNamespaceToModule(moduleName)
        _genModule(sourcesRoot, mod / 'App', sourcePath, moduleName=moduleName)
        _genModule(sourcesRoot, mod / 'Gui', sourcePath, moduleName=moduleName)

    addExceptions(sourcesRoot)
    sourcesRoot['FreeCAD.Units'].imports.add(
        'from FreeCAD.Base import Unit as Unit, Quantity as Quantity')
    sourcesRoot.setSubModulesAsPackage()

    shutil.rmtree(targetPath, ignore_errors=True)
    targetPath.mkdir(parents=True, exist_ok=True)
    (targetPath / '__init__.pyi').touch(exist_ok=True)
    sourcesRoot.save(targetPath)

    for stubPackage in targetPath.iterdir():
        if stubPackage.is_dir():
            if mod := moduleNamespace.getModFromAlias(stubPackage.name):
                newName = mod
            else:
                newName = stubPackage.name

            stubPackage.rename(stubPackage.with_name(f'{newName}-stubs'))

    for additionalPackage in additionalPath.glob('[!_]*.py'):
        targetAdditionalPackage = targetPath / additionalPackage.stem
        targetAdditionalPackage.mkdir()
        shutil.copy(additionalPackage, targetAdditionalPackage / '__init__.py')

# TODO P4 preprocess and remove macros
# https://www.tutorialspoint.com/cplusplus/cpp_preprocessor.htm

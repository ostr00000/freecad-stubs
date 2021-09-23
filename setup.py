import os

from setuptools import setup, PackageFinder

with open("README.md") as f:
    readme = f.read()


class StubPackageFinder(PackageFinder):
    @staticmethod
    def _looks_like_package(path):
        return os.path.isfile(os.path.join(path, '__init__.pyi')) \
               or PackageFinder._looks_like_package(path)


freeCadStubPath = 'freecad_stubs'
packages = [
    p for p in StubPackageFinder.find(where=freeCadStubPath)
    if not p.startswith('_')]

setup(
    name='freecad-stubs',
    version='1.0.4',
    description="Python stubs for FreeCAD",
    long_description=readme,
    long_description_content_type='text/markdown',
    license='GPL-3.0',
    url='https://github.com/ostr00000/freecad-stubs',
    package_dir={'': freeCadStubPath},
    package_data={'': ['*.pyi']},
    packages=packages,
    python_requires='>=3.6',
    install_requires=['qtpy'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Typing :: Typed',
    ],
)

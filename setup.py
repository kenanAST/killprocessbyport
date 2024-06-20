from setuptools import setup
from Cython.Build import cythonize

setup(
    name='killprocessbyport',
    ext_modules=cythonize("killprocessbyport.py"),
)
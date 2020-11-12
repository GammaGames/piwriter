from setuptools import setup
from Cython.Build import cythonize

# doesn't work

setup(
    name='EINK',
    ext_modules=cythonize("tty_eink.pyx"),
    zip_safe=False,
)

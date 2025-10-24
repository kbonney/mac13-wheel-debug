from setuptools import setup, Extension

setup(
    name="hello_cibw",
    version="0.0.1",
    ext_modules=[Extension("hello_cibw", ["src/hello.c"])],
)

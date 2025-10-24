from setuptools import setup, Extension

setup(
    name="mac13_debug",
    version="0.0.1",
    ext_modules=[Extension("mac13_debug.hello", ["src/hello.c"])],
    package_dir={"": "src"},
)

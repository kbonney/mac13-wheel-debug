from setuptools import setup, Extension
import datetime

# Generate a unique version based on timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
version = f"0.0.1.dev{timestamp}"

setup(
    name="hello_cibw",
    version=version,
    description="Test package for macOS 13 cibuildwheel reproduction",
    long_description="A minimal C extension to test cibuildwheel wheel tagging on macOS 13",
    long_description_content_type="text/plain",
    ext_modules=[Extension("hello_cibw", ["src/hello.c"])],
)

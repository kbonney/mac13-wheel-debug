# cibuildwheel macOS13 tag reproduction

This repo tests whether `cibuildwheel` produces `macosx_13_0` or `macosx_14_0` wheels
when run on a macOS-13 GitHub Actions runner.

The package is a trivial Python module so the wheel build behavior can be isolated.

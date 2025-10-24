# macOS 13 cibuildwheel Reproduction Repository

This repository reproduces the issue where `cibuildwheel` on macOS 13 runners produces wheels tagged with `macosx_14_0` instead of the expected `macosx_13_0`.

## What This Tests

This minimal C extension package is designed to test whether `cibuildwheel` correctly tags wheels built on macOS 13 runners. The issue is that despite setting `MACOSX_DEPLOYMENT_TARGET=13.0`, the resulting wheels are tagged as `macosx_14_0_x86_64` instead of `macosx_13_0_x86_64`.

## How to Use

1. **Trigger the workflow**: Go to the Actions tab and click "Run workflow" on the "cibuildwheel macOS13 repro" workflow
2. **Check the results**: Look at the "Show wheel tags" step in the workflow logs
3. **Interpret the results**:
   - **Expected (correct)**: `Tag: cp311-cp311-macosx_13_0_x86_64`
   - **Bug confirmed**: `Tag: cp311-cp311-macosx_14_0_x86_64`

## Repository Structure

```
mac13-wheel-debug/
├── pyproject.toml          # Build system configuration
├── setup.py               # Package setup with C extension
├── src/
│   └── hello.c            # Simple C extension module
└── .github/workflows/
    └── build.yml          # GitHub Actions workflow
```

## The Issue

When building Python wheels on macOS 13 runners with `cibuildwheel`, the resulting wheels are incorrectly tagged as `macosx_14_0` instead of `macosx_13_0`, even when `MACOSX_DEPLOYMENT_TARGET=13.0` is explicitly set.

This affects package compatibility and distribution, as wheels tagged for macOS 14 may not work correctly on macOS 13 systems.

## Workflow Configuration

The workflow:
- Runs only on `macos-13` runners
- Sets `MACOSX_DEPLOYMENT_TARGET=13.0` via `CIBW_ENVIRONMENT_MACOS`
- Builds only CPython 3.11 wheels
- Skips unnecessary platforms
- Shows wheel tags for verification
- Includes debugging output via `python -m sysconfig`

## Expected vs Actual Results

**If the bug is present**, you'll see:
```
hello_cibw-0.0.1-cp311-cp311-macosx_14_0_x86_64.whl
Tag: cp311-cp311-macosx_14_0_x86_64
```

**If the bug is fixed**, you'll see:
```
hello_cibw-0.0.1-cp311-cp311-macosx_13_0_x86_64.whl
Tag: cp311-cp311-macosx_13_0_x86_64
```
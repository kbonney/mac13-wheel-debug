Here’s a concise and clear `ISSUE_SUMMARY.md` you can include in your repo:

---

# cibuildwheel macOS 13 Tag Issue — Summary

## 🧩 Overview

This repository reproduces a bug where **`cibuildwheel`**, when run on a **macOS-13 GitHub Actions runner**, produces wheels tagged for **macOS 14** instead of macOS 13 — even when `MACOSX_DEPLOYMENT_TARGET=13.0` is explicitly set.

Expected tag example:

```
macosx_13_0_x86_64
```

Actual output:

```
macosx_14_0_x86_64
```

This mismatch can cause deployment or compatibility issues when distributing prebuilt wheels for macOS.

---

## ⚙️ Reproduction setup

The workflow (`.github/workflows/build.yml`) runs on a **macOS-13 runner**, using `cibuildwheel` to build a minimal Python package.
It sets:

```yaml
CIBW_ENVIRONMENT_MACOS: |
  MACOSX_DEPLOYMENT_TARGET=13.0
```

and builds for Python 3.11 only:

```yaml
cibuildwheel --output-dir wheelhouse
```

---

## 🧪 Troubleshooting steps tried

1. **Setting `MACOSX_DEPLOYMENT_TARGET` in the environment**

   * Added both global and `CIBW_ENVIRONMENT_MACOS` variables.
   * Result: still produces `macosx_14_0` wheels.

2. **Setting `PLAT=macosx-13.0-universal2`**

   * No effect; tag remains 14.0.

3. **Adding `CIBW_BEFORE_BUILD_MACOS` to export the target again**

   * Verified via logs that the variable is set inside the build, but wheel tag unchanged.

4. **Manual renaming & internal metadata patching**

   * Works superficially, but breaks PyPI upload validation due to altered wheel structure.
   * Not a sustainable or valid solution.

5. **Using older cibuildwheel versions**

   * Same outcome; tag appears to come from the host system (macOS 14 SDK) rather than the specified deployment target.

---

## 🧠 Current hypothesis

Even on the **macOS-13 GitHub runner**, the build environment (Python.org universal2 installers or system SDK) may be detecting and using **macOS 14 build tools**, overriding `MACOSX_DEPLOYMENT_TARGET`.

`cibuildwheel` respects environment variables, but the internal compiler or wheel tag computation likely reads from the SDK or Python interpreter’s `sysconfig` defaults instead.

---

## 🎯 Next steps

* Compare outputs between **macOS-13** and **macOS-14** runners in the same workflow.
* Inspect environment variables during build (`sysconfig.get_platform()`).
* Open a minimal issue in the [`pypa/cibuildwheel`](https://github.com/pypa/cibuildwheel/issues) repository once behavior is confirmed reproducible.

---

## 🧰 References

* [`MACOSX_DEPLOYMENT_TARGET` — Python distutils docs](https://docs.python.org/3/using/mac.html#building-and-installing-universal-binaries-on-macos)
* [`cibuildwheel` environment variable reference](https://cibuildwheel.pypa.io/en/stable/options/)
* [PEP 425: Compatibility Tags for Built Distributions](https://peps.python.org/pep-0425/)

---

Would you like me to expand this with the **proposed workflow diff** that builds both macOS-13 and macOS-14 wheels side-by-side (for direct comparison in CI)?

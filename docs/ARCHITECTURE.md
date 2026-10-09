# Project Architecture

```
             Developer

                 │
                 ▼

          Embedded C Source

                 │
                 ▼

            GCC Compiler

                 │
                 ▼

          Firmware Executable

                 │
                 ▼

        Python Test Framework

        ┌─────────┬──────────┐
        ▼         ▼          ▼

   Unit Test  Integration  Coverage

                 │
                 ▼

            Cppcheck Scan

                 │
                 ▼

          GitHub Actions CI

                 │
                 ▼

           Build Successful
```

---

## Components

### Firmware

Embedded C source code.

### Tests

Python unit and integration tests.

### Coverage

Measures code execution percentage.

### Static Analysis

Cppcheck verifies code quality.

### GitHub Actions

Automatically executes the complete pipeline.

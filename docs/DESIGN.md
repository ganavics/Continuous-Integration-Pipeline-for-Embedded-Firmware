# Embedded CI/CD Pipeline Design

## Overview

This project demonstrates a professional Continuous Integration (CI)
pipeline for Embedded C firmware.

Every push to GitHub automatically performs:

- Firmware Compilation
- Unit Testing
- Integration Testing
- Static Code Analysis
- Code Coverage Analysis

---

## Build Flow

Developer

↓

Git Push

↓

GitHub Actions

↓

Compile Firmware

↓

Run Unit Tests

↓

Run Integration Tests

↓

Cppcheck Static Analysis

↓

Coverage Report

↓

Build Success

---

## Technologies

- Embedded C
- GCC
- Makefile
- Python
- unittest
- Coverage.py
- Cppcheck
- Git
- GitHub Actions

---

## Benefits

- Automatic verification
- Faster development
- Professional workflow
- Reliable firmware releases
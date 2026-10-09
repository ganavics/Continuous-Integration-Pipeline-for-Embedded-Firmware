
import streamlit as st
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIRMWARE = ROOT / "firmware"

st.set_page_config(
    page_title="Embedded Firmware CI Dashboard",
    page_icon="⚙️",
    layout="wide"
)

# Store results across Streamlit reruns
for key in ["build_result", "test_result", "coverage_result"]:
    if key not in st.session_state:
        st.session_state[key] = None


def run_command(command, cwd=ROOT):
    try:
        result = subprocess.run(
            command,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=120,
            shell=False
        )
        output = (result.stdout + "\n" + result.stderr).strip()
        return result.returncode, output or (
    "Build completed successfully. Executable created."
    if result.returncode == 0
    else "Command failed."
)
    except Exception as exc:
        return 1, str(exc)


st.title("⚙️ Embedded Firmware Testing Dashboard")
st.write("Build, test, and analyze your Embedded C firmware.")

col1, col2, col3 = st.columns(3)
col1.metric("Project", "Embedded CI/CD")
col2.metric("Test Framework", "Python unittest")
col3.metric("Build Tool", "GCC / Make")

st.divider()

# Firmware build
st.subheader("🔨 Firmware Build")

if st.button("Build Firmware", use_container_width=True):
    code, output = run_command(
        ["gcc", "-Wall", "main.c", "sensor.c", "alarm.c",
         "-o", "firmware.exe"],
        cwd=FIRMWARE
    )
    st.session_state.build_result = (code, output)

if st.session_state.build_result is not None:
    code, output = st.session_state.build_result
    if code == 0:
        st.success("Firmware built successfully!")
    else:
        st.error("Firmware build failed.")
    st.code(output or "Build completed.")

st.divider()

# Automated tests
st.subheader("🧪 Automated Testing")

if st.button("Run All Tests", use_container_width=True):
    code, output = run_command(
        [sys.executable, "-m", "unittest",
         "discover", "-s", "tests", "-v"]
    )
    st.session_state.test_result = (code, output)

if st.session_state.test_result is not None:
    code, output = st.session_state.test_result
    if code == 0:
        st.success("All discovered tests passed!")
    else:
        st.error("Some tests failed.")
    st.code(output)

st.divider()

# Code coverage
st.subheader("📊 Code Coverage")

if st.button("Run Coverage Analysis", use_container_width=True):
    code, output = run_command(
        [sys.executable, "-m", "coverage", "run",
         "-m", "unittest", "discover", "-s", "tests"]
    )

    if code == 0:
        report_code, report = run_command(
            [sys.executable, "-m", "coverage", "report", "-m"]
        )
        st.session_state.coverage_result = (
            report_code, report
        )
    else:
        st.session_state.coverage_result = (code, output)

if st.session_state.coverage_result is not None:
    code, output = st.session_state.coverage_result
    if code == 0:
        st.success("Coverage analysis completed.")
    else:
        st.error("Coverage analysis failed.")
    st.code(output)

st.caption("Local testing dashboard | Embedded Firmware CI/CD Project")

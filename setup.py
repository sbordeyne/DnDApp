import sys
from cx_Freeze import setup, Executable

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "DnDApp",
    version = "0.13.0",
    description = "A tool to play Dungeons and Dragons",
    executables = [Executable("launch.py", base = base)])

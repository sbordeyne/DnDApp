"""Python code to build the app into a .exe file"""

import sys
from cx_Freeze import setup, Executable
# GUI applications require a different base on Windows (the default is for a
# console application).
BASE = None
if sys.platform == "win32":
    BASE = "Win32GUI"

setup(
    name="DnDApp",
    version="0.0.1",
    description="A tool to play Dungeons and Dragons",
    executables=[Executable("launch.py", base=BASE)])

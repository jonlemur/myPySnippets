'''
Compile pyhon to exe with cx_freeze
1. install cx_freeze cmd> python -m pip install cx_Freeze --upgrade
2. edit this file so it points to your main py-file. Name is setup and put it in the main-py dir
3. cmd> python setup.py build

'''

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "myPySideApp",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("pySide.py", base=base)])
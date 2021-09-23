#  Copyright 2021 Harsh Patil & Het Naik
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "optimize": 1,
    "include_files": ["assets/"],
    "packages": ["os", "PyQt5", "pyperclip", "pymysql"],
    "excludes": ["tkinter"]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="UnifiedPass",
    version="1.0",
    description="A system independent credential manager.",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon='assets/icon.png')]
)

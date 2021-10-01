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
import os
import utils
import pyhibp
from PyQt5 import QtWidgets, QtGui, QtCore
from login_ui import LoginUI

if __name__ == "__main__":
    pyhibp.set_user_agent('UnifiedPass/1.1.2 (A system independent credential manager)')
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"

    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)

    QtGui.QFontDatabase.addApplicationFont("assets/OpenSans-Regular.ttf")
    QtGui.QFontDatabase.addApplicationFont("assets/Montserrat-Regular.ttf")
    icon = QtGui.QIcon("assets/icon.png")

    window = QtWidgets.QMainWindow()
    window.setWindowIcon(icon)
    connection = utils.create_connection(window)

    ui = LoginUI(window, connection)
    ui.setup_ui()
    window.show()

    sys.exit(app.exec_())

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
import utils
from PyQt5 import QtWidgets, QtGui
from login_ui import LoginUI

if __name__ == "__main__":
    QtGui.QFontDatabase.addApplicationFont("assets/Montserrat-Regular.ttf")
    QtGui.QFontDatabase.addApplicationFont("assets/OpenSans-Regular.ttf")

    app = QtWidgets.QApplication(sys.argv)
    icon = QtGui.QIcon("assets/icon.png")

    window = QtWidgets.QMainWindow()
    window.setWindowIcon(icon)
    connection = utils.create_connection(window)

    ui = LoginUI(window, connection)
    ui.setup_ui()
    window.show()

    sys.exit(app.exec_())

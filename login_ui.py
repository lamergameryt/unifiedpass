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

import utils
from pymysql import Connection
from PyQt5 import QtCore, QtGui, QtWidgets
from generate_ui import GenerateUI
from pyhibp import pwnedpasswords as pw

def check_credentials(window, connection: Connection, username: str, password: str):
    if not username.rstrip():
        utils.show_error("Please enter a valid username.", window)
        return

    if not password.rsplit():
        utils.show_error("Please enter a valid password.", window)
        return

    if utils.verify_user(connection, username, password):
        utils.show_message(f"Welcome, {username}. Please enter the information present in the window to generate "
                           f"your password.", window)
        ui = GenerateUI(window, password)
        ui.setup_ui()
        window.show()
    else:
        utils.show_error("The entered credentials are invalid!", window)


def register(window, connection: Connection, username: QtWidgets.QLineEdit, password: QtWidgets.QLineEdit):
    if utils.check_user_exists(connection, username.text()):
        utils.show_error("The user with this name already exists! Please register with different username.", window)
        return

    if len(username.text().rstrip()) < 4:
        utils.show_error("The username cannot be shorter than 4 characters.", window)
        return

    if len(password.text().rstrip()) < 8:
        utils.show_error("Please make sure your password is atleast 8 characters long.", window)
        return

    result = pw.is_password_breached(password=password.text().rstrip())
    if result:
        utils.show_error(f"The password you're using has been leaked online {result} times. "
                         f"Please register with a different password.", window)
        return

    utils.register_user(connection, username.text().rstrip(), password.text().rstrip())
    utils.show_message("Your account has been registered. Please proceed to log into your account.", window)
    username.setText("")
    password.setText("")


class LoginUI:
    def __init__(self, window, connection):
        self.central_widget = QtWidgets.QWidget(window)
        self.title = QtWidgets.QLabel(self.central_widget)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.menubar = QtWidgets.QMenuBar(window)

        self.register_btn = QtWidgets.QPushButton(self.central_widget)
        self.login_btn = QtWidgets.QPushButton(self.central_widget)
        self.username = QtWidgets.QLineEdit(self.central_widget)
        self.password = QtWidgets.QLineEdit(self.central_widget)
        self.underline = QtWidgets.QFrame(self.central_widget)
        self.underline_2 = QtWidgets.QFrame(self.central_widget)

        self.window = window
        self.connection = connection

    def setup_ui(self):
        self.window.setObjectName("window")
        self.window.setFixedSize(926, 563)
        self.window.setStyleSheet("background-color: #1f1f1f")
        self.window.setTabShape(QtWidgets.QTabWidget.Rounded)

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())

        self.central_widget.setSizePolicy(size_policy)
        self.central_widget.setObjectName("central_widget")
        self.title.setGeometry(QtCore.QRect(240, 110, 461, 51))

        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(23)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.title.setFont(font)
        self.title.setStyleSheet("color: #D0D0D0;\n"
                                 "letter-spacing: 2px;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.underline.setGeometry(QtCore.QRect(230, 240, 461, 20))

        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.username.setGeometry(QtCore.QRect(230, 210, 461, 31))
        self.username.setFont(font)
        self.username.setStyleSheet("color: #D0D0D0;\n"
                                    "border: none;\n"
                                    "letter-spacing: 1px;")
        self.username.setObjectName("username")

        self.password.setGeometry(QtCore.QRect(230, 290, 461, 31))
        self.password.setFont(font)
        self.password.setStyleSheet("color: #D0D0D0;\n"
                                    "border: none;\n"
                                    "letter-spacing: 1px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")

        self.login_btn.setGeometry(QtCore.QRect(230, 360, 211, 51))
        self.login_btn.setFont(font)
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_btn.setStyleSheet("color: #1f1f1f;\n"
                                     "background-color: #bdbdbd;\n"
                                     "border-radius: 8px;")
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(lambda: check_credentials(
            self.window, self.connection, self.username.text(), self.password.text()
        ))

        self.register_btn.setGeometry(QtCore.QRect(480, 360, 211, 51))
        self.register_btn.setFont(font)
        self.register_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.register_btn.setStyleSheet("color: #1f1f1f;\n"
                                        "background-color: #bdbdbd;\n"
                                        "border-radius: 8px;")
        self.register_btn.setObjectName("register_btn")
        self.register_btn.clicked.connect(lambda: register(self.window, self.connection, self.username, self.password))

        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)

        self.underline.setFont(font)
        self.underline.setStyleSheet("color: #D0D0D0;")
        self.underline.setFrameShadow(QtWidgets.QFrame.Plain)
        self.underline.setFrameShape(QtWidgets.QFrame.HLine)
        self.underline.setObjectName("line")

        self.underline_2.setGeometry(QtCore.QRect(230, 320, 461, 20))
        self.underline_2.setFont(font)
        self.underline_2.setStyleSheet("color: #D0D0D0;")
        self.underline_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.underline_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.underline_2.setObjectName("underline_2")

        # noinspection DuplicatedCode
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 26))
        self.menubar.setObjectName("menubar")
        self.statusbar.setObjectName("statusbar")

        self.window.setCentralWidget(self.central_widget)
        self.window.setMenuBar(self.menubar)
        self.window.setStatusBar(self.statusbar)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self.window)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("window", "UnifiedPass"))
        self.title.setText(_translate("window", "Log Into UnifiedPass"))
        self.username.setPlaceholderText(_translate("window", "Username"))
        self.password.setPlaceholderText(_translate("window", "Password"))
        self.login_btn.setText(_translate("window", "Log In"))
        self.register_btn.setText(_translate("window", "Register"))

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
import password as pass_hash
import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets


def generate_password(window,
                      website: QtWidgets.QLineEdit,
                      email: QtWidgets.QLineEdit,
                      number: QtWidgets.QLineEdit,
                      master_password: str):
    length = utils.get_input("Enter the length of the password", window)
    secure_number: int
    try:
        length = int(length)
        secure_number = int(number.text())
    except Exception as _:
        utils.show_error("Please make sure the security number and the password length are both numbers.")
        return

    final_pass = pass_hash.generate_password(website.text(), email.text(), secure_number, length, master_password)
    pyperclip.copy(final_pass)
    utils.show_message(f"The password for {website.text()} is {final_pass}. The password has also been copied to "
                       "your clipboard.", window)

    website.setText("")
    email.setText("")
    number.setText("")


class GenerateUI:
    def __init__(self, window, _password: str):
        self.central_widget = QtWidgets.QWidget(window)
        self.title = QtWidgets.QLabel(self.central_widget)
        self.website = QtWidgets.QLineEdit(self.central_widget)
        self.email = QtWidgets.QLineEdit(self.central_widget)
        self.number = QtWidgets.QLineEdit(self.central_widget)

        self.underline = QtWidgets.QFrame(self.central_widget)
        self.underline_2 = QtWidgets.QFrame(self.central_widget)
        self.underline_3 = QtWidgets.QFrame(self.central_widget)

        self.generate_btn = QtWidgets.QPushButton(self.central_widget)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.menubar = QtWidgets.QMenuBar(window)
        self.window = window
        self._password = _password

    def setup_ui(self):
        self.window.setObjectName("window")
        self.window.resize(926, 563)
        self.window.setStyleSheet("background-color: #1f1f1f")
        self.central_widget.setObjectName("central_widget")

        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)

        self.title.setGeometry(QtCore.QRect(240, 50, 461, 51))
        self.title.setFont(font)
        self.title.setStyleSheet("color: #D0D0D0;\n"
                                 "letter-spacing: 2px;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)

        self.website.setGeometry(QtCore.QRect(240, 160, 461, 31))
        self.website.setFont(font)
        self.website.setStyleSheet("color: #D0D0D0;\n"
                                   "border: none;\n"
                                   "letter-spacing: 1px;")
        self.website.setObjectName("website")

        self.email.setGeometry(QtCore.QRect(240, 250, 461, 31))
        self.email.setFont(font)
        self.email.setStyleSheet("color: #D0D0D0;\n"
                                 "border: none;\n"
                                 "letter-spacing: 1px;")
        self.email.setObjectName("email")

        self.number.setGeometry(QtCore.QRect(240, 340, 461, 31))
        self.number.setFont(font)
        self.number.setStyleSheet("color: #D0D0D0;\n"
                                  "border: none;\n"
                                  "letter-spacing: 1px;")
        self.number.setInputMask("")
        self.number.setText("")
        self.number.setObjectName("number")

        self.generate_btn.setGeometry(QtCore.QRect(330, 430, 291, 51))
        self.generate_btn.setFont(font)
        self.generate_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generate_btn.setStyleSheet("color: #1f1f1f;\n"
                                        "background-color: #bdbdbd;\n"
                                        "border-radius: 8px;")
        self.generate_btn.setObjectName("generate_btn")
        self.generate_btn.clicked.connect(lambda: generate_password(
            self.window, self.website, self.email, self.number, self._password
        ))

        self.underline.setGeometry(QtCore.QRect(240, 190, 461, 20))
        self.underline.setFont(font)
        self.underline.setStyleSheet("color: #D0D0D0;")
        self.underline.setFrameShadow(QtWidgets.QFrame.Plain)
        self.underline.setFrameShape(QtWidgets.QFrame.HLine)
        self.underline.setObjectName("underline")

        self.underline_2.setGeometry(QtCore.QRect(240, 280, 461, 20))
        self.underline_2.setFont(font)
        self.underline_2.setStyleSheet("color: #D0D0D0;")
        self.underline_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.underline_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.underline_2.setObjectName("underline_2")

        self.underline_3.setGeometry(QtCore.QRect(240, 370, 461, 20))
        self.underline_3.setFont(font)
        self.underline_3.setStyleSheet("color: #D0D0D0;")
        self.underline_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.underline_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.underline_3.setObjectName("underline_3")

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
        self.title.setText(_translate("window", "UnifiedPass"))
        self.website.setPlaceholderText(_translate("window", "Website Link"))
        self.email.setPlaceholderText(_translate("window", "Username / Email"))
        self.number.setPlaceholderText(_translate("window", "Security Number"))
        self.generate_btn.setText(_translate("window", "Generate Password"))

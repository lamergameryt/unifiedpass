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

import config
import sys
import pymysql
import hashlib
from PyQt5 import QtWidgets, QtCore

secure_salt = "unified-pass-salt"


def get_default_message_box(text: str, window=None) -> QtWidgets.QMessageBox:
    error = QtWidgets.QMessageBox()
    if window is not None:
        error.setWindowIcon(window.windowIcon())
    error.setWindowTitle("UnifiedPass")
    error.setText(text)

    return error


def show_error(
    text: str,
    window=None,
    icon=QtWidgets.QMessageBox.Icon.Critical,
    button=QtWidgets.QMessageBox.StandardButton.Close,
):
    error = get_default_message_box(text, window)
    error.setStandardButtons(button)
    error.setIcon(icon)
    error.exec_()


def show_message(
    text: str,
    window=None,
    icon=QtWidgets.QMessageBox.Icon.Information,
    button=QtWidgets.QMessageBox.StandardButton.Close,
):
    error = get_default_message_box(text, window)
    error.setIcon(icon)
    error.setStandardButtons(button)
    error.exec_()


def get_input(text: str, window=None) -> str:
    input_box = QtWidgets.QInputDialog()
    input_box.setWindowTitle("UnifiedPass")
    input_box.setLabelText(text)
    input_box.setWindowFlag(QtCore.Qt.WindowSystemMenuHint, False)
    input_box.setWindowFlag(QtCore.Qt.WindowTitleHint, False)
    input_box.setFixedSize(250, 200)
    if window is not None:
        input_box.setWindowIcon(window.windowIcon())

    input_box.exec_()
    return input_box.textValue()


def create_connection(window):
    try:
        return pymysql.connect(
            host=config.host,
            port=config.port,
            password=config.password,
            user=config.username,
            database=config.database,
            cursorclass=pymysql.cursors.DictCursor,
        )
    except Exception as _:
        show_error(
            "The configuration present in the config.py file is invalid. You can create the database using "
            "the database.sql file.",
            window,
        )
        sys.exit(1)


def check_user_exists(connection: pymysql.Connection, username: str) -> bool:
    with connection.cursor() as cursor:
        query = "SELECT COUNT(id) AS count FROM unifiedpass.information WHERE username=%s"
        cursor.execute(query, username)
        result = cursor.fetchone()

    return result["count"] > 0


def get_hashed_password(password: str) -> str:
    return hashlib.pbkdf2_hmac("SHA256", password.encode("UTF-8"), secure_salt.encode("UTF-8"), 10000, 32).hex()


def register_user(connection: pymysql.Connection, username: str, password: str):
    pass_hash = get_hashed_password(password)
    with connection.cursor() as cursor:
        query = "INSERT INTO unifiedpass.information (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, pass_hash))
        connection.commit()


def verify_user(connection: pymysql.Connection, username: str, password: str) -> bool:
    pass_hash = get_hashed_password(password)
    with connection.cursor() as cursor:
        query = "SELECT COUNT(*) AS count FROM unifiedpass.information WHERE username=%s AND password=%s"
        cursor.execute(query, (username, pass_hash))
        result = cursor.fetchone()

        return result["count"] > 0

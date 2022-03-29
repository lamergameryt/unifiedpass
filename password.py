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

import hashlib

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,-./:;<=>?@[]^_{|}~"


def generate_entropy(website: str, email: str, number: int, master_password: str) -> int:
    """
    Create a random series of integer numbers based on the values entered by the user.
    """
    salt = website + email + hex(number)
    hex_entropy = hashlib.pbkdf2_hmac("sha256", master_password.encode("utf-8"), salt.encode("utf-8"), 10000, 32).hex()
    return int(hex_entropy, 16)


def consume_entropy(generated_password: str, quotient: int, max_length: int) -> str:
    """
    Takes the entropy (quotient) and the length of password (max_length) required
    and uses the remainder of their division as the index to pick a character from
    the characters list.

    This process occurs recursively until the password is of the required length.
    """
    if len(generated_password) >= max_length:
        return generated_password

    quotient, remainder = divmod(quotient, len(characters))
    generated_password += characters[remainder]

    return consume_entropy(generated_password, quotient, max_length)


def generate_password(website: str, email: str, number: int, length: int, master_password: str) -> str:
    entropy = generate_entropy(website, email, number, master_password)
    return render_password(entropy, length)


def render_password(entropy: int, length: int) -> str:
    return consume_entropy("", entropy, length)

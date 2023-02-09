import random
import pyperclip


def create_new(length, characters):
    password = "".join(random.choice(characters) for _ in range(length))
    pyperclip.copy(password)
    return password

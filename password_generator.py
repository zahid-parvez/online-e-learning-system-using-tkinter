#  password generator
# hard level

import random


def get_password():
    lower = 'qwertyuiopasdfghjklzxcvbnm'
    upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    number = '1234567890'
    symbol = '@#_'
    whole = lower + upper + number + symbol
    length = 7
    password = "".join(random.sample(whole, length))
    return password

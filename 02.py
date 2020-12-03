from typing import Dict
import re
from utils import get_entries

entries = get_entries(2)
entries.pop()


def get_rule(entry: str):
    p1 = re.compile(r"(\d{1}-\d{2}(?=.*\w:)|\d{2}-\d{2}(?=.*\w:)|\d{1}-\d{1}(?=.*\w:))", re.MULTILINE)
    p2 = re.compile(r"((?<=\d{1}-\d{2}).\w|(?<=\d{2}-\d{2}).\w|(?<=\d{1}-\d{1}).\w)", re.MULTILINE)
    res = re.split(p1, entry)
    res2 = re.split(p2, entry)
    quantities = res[1].split("-")
    char = res2[1].strip()

    return {
        "min": int(quantities[0]),
        "max": int(quantities[1]),
        "char": char
    }


def get_password(entry: str):
    p1 = re.compile(r"((?<=:).*\w)", re.MULTILINE)
    res = re.split(p1, entry)
    return res[1].strip()


def check_password_validity_p1(rule: Dict, password: str):
    char_count = password.count(rule['char'])
    if rule['max'] >= char_count >= rule['min']:
        return True
    else:
        return False


def check_password_validity_p2(rule: Dict, password: str):
    if password[rule['min']-1] == rule['char'] and password[rule['max']-1] != rule['char']:
        return True
    elif password[rule['min']-1] != rule['char'] and password[rule['max']-1] == rule['char']:
        return True
    else:
        return False


count_p1 = 0
count_p2 = 0

for entry in entries:
    rule = get_rule(entry)
    passw = get_password(entry)
    if check_password_validity_p1(rule, passw):
        count_p1 += 1
    if check_password_validity_p2(rule, passw):
        count_p2 += 1

print('Part 1:', count_p1)
print('Part 2:', count_p2)

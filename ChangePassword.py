# At least 18 alphanumeric characters and list of special chars !@#$&*
# At least 1 Upper case, 1 lower case ,least 1 numeric, 1 special character
# No duplicate repeat characters more than 4
# No more than 4 special characters
# 50 % of password should not be a number

import re

regex = '^[ A-Za-z0-9!@#$&*]*$'
special_char = ['!', '@', '#', '$', '&', '*']


def verify_old_password(old_password):
    #Mock start with 'sys'
    if (old_password.startswith('sys')):
        return True
    else:
        return False


def validate_similarity(old_password, new_password):
    #Mock end with 'same'
    if (old_password.endswith('same') & new_password.endswith('same')):
        return True
    else:
        return False


def verify_repeat_char(new_password):
    # No duplicate repeat characters more than 4
    repeated = {}
    for char in new_password:
        if char in repeated:
            repeated[char] += 1
        else:
            repeated[char] = 1

    for key, value in repeated.items():
        if value > 4:
            return True
    return False


def count_repeat_special(new_password):
    count = 0
    for char in new_password:
        if char in special_char:
            count += 1
    return count


def count_numeric(new_password):
    count = 0
    for char in new_password:
        if char.isdigit():
            count += 1
    return count


def validate_password(new_password):
    if len(new_password) < 18:
        return False

    if not re.match(regex, new_password):
        return False

    if not any(char.isdigit() for char in new_password):
        return False

    if not any(char.isupper() for char in new_password):
        return False

    if not any(char.islower() for char in new_password):
        return False

    if not any(char in special_char for char in new_password):
        return False

    if verify_repeat_char(new_password):
        return False

    if count_repeat_special(new_password) > 4:
        return False

    if (count_numeric(new_password) / len(new_password) >= 0.5):
        return False

    return True


def change_password(old_password, new_password):
    if (len(old_password) < 1) | (len(new_password) < 1):
        return False

    if not verify_old_password(old_password):
        return False

    if validate_similarity(old_password, new_password):
        return False

    return validate_password(new_password)

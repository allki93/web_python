import hashlib as h
# основаня функция
def pwdGenerator(pwd_str: str, salt_str: str, num_char: str) -> str:
    # конкатенация строк
    pwd_str += salt_str
    # кодирование в байт-строку
    byte_str = pwd_str.encode()
    # хеширование
    hash_str = h.sha256(byte_str)
    # преобразование объекта хеш в обычную строку
    if num_char.isnumeric():
        hex_str = hash_str.hexdigest()[:int(num_char)]
    else:
        hex_str = hash_str.hexdigest()

    return hex_str

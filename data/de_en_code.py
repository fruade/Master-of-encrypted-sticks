# Набор символов ASII - алфавита (знаки, цифры, латинские и русские буквы)
ALPHABET = [chr(i) for i in range(32, 127)] + [chr(i) for i in range(1040, 1103)]


def encode(text: str, key: str) -> str:
    """Функция кодирования"""
    result_text = ''
    for i, letter in enumerate(text):
        # Проверяем есть ли символ из строки и ключа в нашем словаре
        if letter in ALPHABET and key[i % len(key)] in ALPHABET:
            # кодируем символ
            result_text += ALPHABET[(ALPHABET.index(letter) + ALPHABET.index(key[i % len(key)])) % len(ALPHABET)]
        else:
            # записываем символ как есть
            result_text += letter
    return result_text


def decode(text: str, key) -> str:
    """Функция декодирования"""
    result_text = ''
    for i, letter in enumerate(text):
        # Проверяем есть ли символ из строки и ключа в нашем словаре
        if letter in ALPHABET and key[i % len(key)] in ALPHABET:
            # раскодируем символ
            result_text += ALPHABET[(ALPHABET.index(letter) - ALPHABET.index(key[i % len(key)])) % len(ALPHABET)]
        else:
            # записываем символ как есть
            result_text += letter
    return result_text


#text = "Простое лучше сложного. Simple is better than complex."
key = "zametki"
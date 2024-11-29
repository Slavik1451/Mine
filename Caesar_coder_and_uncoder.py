def сaesar_uncoder(shift, coded_message):
    uncoded_message = ''
    for i in coded_message:
        if ord(i) - shift < start:
            uncoded_message += chr(ord(i) + 26 - shift)
        else:
            uncoded_message += chr(ord(i) - shift)
    return uncoded_message


def сaesar_coder(shift, uncoded_message):
    coded_message = ''
    for i in uncoded_message:
        if ord(i) + shift > end:
            coded_message += chr(ord(i) - 26 + shift)
        else:
            coded_message += chr(ord(i) + shift)
    return coded_message


start = ord('a')
end = ord('z')

if __name__ == "__main__":
    test_code = сaesar_coder(1, 'ilovepython')
    print(f'Зашифрованное сообщение "ilovepython" = {test_code}')

    test_uncode = сaesar_uncoder(1, test_code)
    print(f'Расшифруем его обратно {test_uncode}')

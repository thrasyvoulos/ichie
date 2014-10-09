def roller(txt):
    result = ''
    uppercase = True
    for character in txt:
        if character.isalpha():
            result += character.upper() if uppercase else character.lower()
            uppercase = not uppercase
        else:
            result += character
    return result

roller("Whether 'tis nobler in the mind to suffer")

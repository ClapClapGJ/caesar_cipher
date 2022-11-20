LAST_CHAR_CODE = ord('Z')
FIRST_CHAR_CODE = ord('A')
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

def caesar_cipher(message: str, shift: int):
    # Result placeholder
    result = ''

    for char in message.upper():
        if char.isalpha():
            # Convert character to the ASCII code
            char_code = ord(char)
            new_char_code = char_code+shift

            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE

            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE

            new_char = chr(new_char_code)
            result += new_char
            # Save non alphabet characters
        else:
            result += char
    return result

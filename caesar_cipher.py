message = 'Hello, World'
shift = 7

LAST_CHAR_CODE = 90
CHAR_RANGE = 26

# Result placeholder
result = ''

for char in message.upper():
    if char.isalpha():
        # Convert character to the ASCII code
        char_code = ord(char)

        new_char_code = char_code+shift

        if new_char_code > LAST_CHAR_CODE:
            new_char_code -= CHAR_RANGE

        new_char = chr(new_char_code)
        result += new_char
        # Save non alphabet characters
    else:
        result += char

print(message)
print(result)
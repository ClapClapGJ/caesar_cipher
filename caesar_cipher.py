message = 'Hello world'
shift = 7

# Result placeholder
result = ''

for char in message:
    # Convert character to the ASCII code
    char_code = ord(char)

    new_char_code = char_code+shift

    new_char = chr(new_char_code)
    result = result+new_char

    print(char, char_code, new_char_code, new_char)
print(message)
print(result)
message = 'Hello, world'
shift = 7

# Result placeholder
result = ''

for char in message:
    if char.isalpha():
        # Convert character to the ASCII code
        char_code = ord(char)

        new_char_code = char_code+shift

        new_char = chr(new_char_code)
        result += new_char
        # Save non alphabet characters
    else:
        result += char

print(message)
print(result)
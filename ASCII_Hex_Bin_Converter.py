def print_hexa():
    hresult = ''
    for char in string:
        decimal_representation = ord(char)
        hexadecimal_string = hex(decimal_representation)
        hexadecimal_string = hexadecimal_string.replace('0x', '')
        hresult += hexadecimal_string.upper() + ' '
    print(f"Hex Representation : \n{hresult}")

def print_bin():    
    bresult = ''
    for char in string:
        decimal_representation = ord(char)
        binary_string = bin(decimal_representation)
        binary_string = binary_string.replace('0b', '')
        bresult += binary_string + ' '
    print(f"\nBinary Representation : \n{bresult}")

string = input("Enter String Statement for Conversion: ")
print_hexa()
print_bin()
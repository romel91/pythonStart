def decimal_to_binary(decimal_number):
    if not 0<= decimal_number < 1024:
        raise ValueError("Input must be a decimal number between 0 and 1023.999...")
    
    binary_representation = bin(int(decimal_number))[2:]
    return binary_representation.zfill(10)  # Ensure the binary number has 10 digits

decimal_number =42.75
binary_number =decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is :{binary_number}")
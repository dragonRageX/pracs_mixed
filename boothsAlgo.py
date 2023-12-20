multiplier_decimal = int(input("Enter the Multiplier value: "))   #M
multiplicand_decimal = int(input("Enter the Multiplicand value: "))   #Q

def decimal_to_binary_str(value, max_bits):
    if value >= 0:
        binary_str = format(value, f"0{max_bits}b")
    else:
        binary_str = format((1 << max_bits) + value, f"0{max_bits}b")   #2's complement
    return binary_str

max_bits = max(multiplier_decimal.bit_length(), multiplicand_decimal.bit_length()) + 1  #calculate which of multiplier or multiplicand has max bits in its binary representation

multiplier_binary_str = decimal_to_binary_str(multiplier_decimal, max_bits)   #M
print(f"M: {multiplier_binary_str}")
multiplicand_binary_str = decimal_to_binary_str(multiplicand_decimal, max_bits)   #Q
print(f"Q: {multiplicand_binary_str}")

minus_multiplier_binary_str = decimal_to_binary_str(-multiplier_decimal, max_bits)   #-M
minus_multiplicand_binary_str = decimal_to_binary_str(-multiplicand_decimal, max_bits)   #-Q

A = format(0, f"0{max_bits}b")
print(f"A: {A}")

count = max_bits
print(f"Count: {count}")

Qnot = "0"

def binary_addition(A, M_binary_str):
    A_decimal = int(A, 2)
    M_decimal = int(M_binary_str, 2)
    result_decimal = A_decimal + M_decimal

    # if result_decimal >= 0:
    result_binary = format(result_decimal, f"0{max_bits}b")
    # else:
    #     result_binary = format((1 << max_bits) + result_decimal, f"0{max_bits}b")   #2's complement
    return result_binary

while(count != 0):
    if(f"{multiplicand_binary_str[-1]}{Qnot}" == "10"):
        A = binary_addition(A, minus_multiplier_binary_str)   #A = A + (-M)
    elif(f"{multiplicand_binary_str[-1]}{Qnot}" == "01"):
        A = binary_addition(A, multiplier_binary_str)   #A = A + M
    
    #ARS
    Qnot = multiplicand_binary_str[-1]

    lsb_A = A[-1]
    multiplicand_binary_str = lsb_A + multiplicand_binary_str[:-1]   #right-shift

    msb_A = A[0]
    A = msb_A + A[:-1]   #right-shift

    count = count - 1

product = f"{A}{multiplicand_binary_str}"
print(f"The product is {product}")

if product[0] == "1":   #2's complement
    # Invert all the bits
    inverted_str = ''.join('1' if bit == '0' else '0' for bit in product)

    # Add 1 to the inverted binary number
    product = bin(int(inverted_str, 2) + 1)[2:]

print(f"The final product is {product}")
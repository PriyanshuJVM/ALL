def prepare_input(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    i = 0
    result = ""
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else "X"
        if a == b:
            result += a + "X"
            i += 1
        else:
            result += a + b
            i += 2
    if len(result) % 2 != 0:
        result += "X"
    return result

def create_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()
    for c in key:
        if c not in used and c.isalpha():
            matrix.append(c)
            used.add(c)
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in used:
            matrix.append(c)
            used.add(c)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_pos(matrix, c):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == c:
                return i, j
    return None

def playfair_encrypt(pairs, matrix):
    result = ""
    for i in range(0, len(pairs), 2):
        a, b = pairs[i], pairs[i + 1]
        row1, col1 = find_pos(matrix, a)
        row2, col2 = find_pos(matrix, b)
        if row1 == row2:
            result += matrix[row1][(col1 + 1) % 5]
            result += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 + 1) % 5][col1]
            result += matrix[(row2 + 1) % 5][col2]
        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]
    return result

def playfair_decrypt(pairs, matrix):
    result = ""
    for i in range(0, len(pairs), 2):
        a, b = pairs[i], pairs[i + 1]
        row1, col1 = find_pos(matrix, a)
        row2, col2 = find_pos(matrix, b)
        if row1 == row2:
            result += matrix[row1][(col1 - 1) % 5]
            result += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 - 1) % 5][col1]
            result += matrix[(row2 - 1) % 5][col2]
        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]
    return result

# Main
plaintext = input("Enter the message: ")
key = input("Enter the key: ")

prepared = prepare_input(plaintext)
matrix = create_matrix(key)

encrypted = playfair_encrypt(prepared, matrix)
print("Encrypted message:", encrypted)

decrypted = playfair_decrypt(encrypted, matrix)
print("Decrypted message:", decrypted)

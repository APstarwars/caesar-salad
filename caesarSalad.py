import sys

def dcode(ciphertext):
    # Gets ciphers from command line or file
    code = []
    try:
        inFile = open(ciphertext, "r")
        for line in inFile:
            code.append(line)
        inFile.close()
    except FileNotFoundError:
        code.append(ciphertext)
    
    # Cracks each cipher
    for cipher in code:
        for shift in range(1, 26):
            output = ""
            for char in cipher:
                if char.isalpha():
                    if char.islower():
                        output += chr(((ord(char) + shift - 97) % 26) + 97)
                    elif char.isupper():
                        output += chr(((ord(char) + shift - 65) % 26) + 65)
                elif char != '\n':
                    output += char
            
            # Checks for valid english words
            wordFile = open("engmix.txt", "r")
            for word in wordFile:
                if (output.lower().find(word.strip('\n')) != -1):
                    print(output)
                    break
            wordFile.close()

if len(sys.argv) != 2:
    print("Usage: python caesarSalad.py [ciphertext/file]")
else:
    dcode(sys.argv[1])

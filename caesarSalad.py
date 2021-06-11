import sys

# Takes ciphertext or a file of ciphertext and returns a list of each cracked cipher
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
    cipherlist = []
    for cipher in code:
        possibilities = {}
        for shift in range(1, 26):
            output = ""
            for char in ciphertext:
                if char.isalpha():
                    if char.islower():
                        output += chr(((ord(char) + shift - 97) % 26) + 97)
                    elif char.isupper():
                        output += chr(((ord(char) + shift - 65) % 26) + 65)
                elif char != '\n':
                    output += char
            output = ' ' + output + ' ' # add space padding to help word search
           
            # Checks for valid english words
            wordFile = open("engmix.txt", "r")
            wordcount = 0
            for word in wordFile:
                if (output.lower().find(' ' + word.strip('\n') + ' ') != -1):
                    wordcount += 1
            wordFile.close()
            if wordcount > 0:
                possibilities[output.strip()] = wordcount
        if len(possibilities) > 0:
            max = list(possibilities.keys())[0]
            for p in possibilities.keys():
                if possibilities[p] > possibilities[max]:
                    max = p
            cipherlist.append(max)
    return cipherlist

if len(sys.argv) != 2:
    print("Usage: python caesarSalad.py [ciphertext/file]")
else:
    print(dcode(sys.argv[1]))

# Import Depedencies
from itertools import cycle

# Import customEncryption
from encryptionCodes import encryptionCodes

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


encrypt = input('Enter Message to Encrypt\n')
encryptionCode = input('Enter Encryption Code\n')
encryptionValues = encryptionCodes.get(encryptionCode)
staticEcryptList = list(encrypt)
encryptList = list(encrypt)
encryptlen = len(encryptList)

encryptionValuesCycle = cycle(encryptionValues)
encryptionValue = int(encryptionValues[0])

for position in range(encryptlen):
    character = encryptList[position]
    if character in alphabet:
        alphabetIndex = alphabet.index(character)
        for i in range(encryptionValue):
            try:
                encryptList[position] = alphabet[alphabetIndex+1]
                character = encryptList[position]
                alphabetIndex = alphabet.index(character)
            except:
                encryptList[position] = 'a'
                if i == encryptionValue-1:
                    break
                character = encryptList[position]
                alphabetIndex = alphabet.index(character)
                encryptList[position] = alphabet[alphabetIndex+1]
    elif character == ' ':
        pass
    else:
        print('{} is not in list'.format(character))
    encryptionValue = int(next(encryptionValuesCycle))


print(''.join(encryptList))
print('Encryption Code Used: {}'.format(encryptionCode))
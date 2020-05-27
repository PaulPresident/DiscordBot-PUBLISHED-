# Import Depedencies
from itertools import cycle

# Import customEncryption
from encryptionCodes import encryptionCodes

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


decrypt = input('Enter Message to Dencrypt\n')
decryptionCode = input('Enter Decryption Code\n')
decryptionValues = encryptionCodes.get(decryptionCode)
decryptList = list(decrypt)
decryptlen = len(decryptList)

decryptionValuesCycle = cycle(decryptionValues)
decryptionValue = int(decryptionValues[0])

for position in range(decryptlen):
    character = decryptList[position]
    if character in alphabet:
        alphabetIndex = alphabet.index(character)
        try:
            decryptList[position] = alphabet[alphabetIndex-decryptionValue]
        except:
            print('error IDFK')
    elif character == ' ':
        pass
    else:
        print('{} is not in list'.format(character))
    decryptionValue = next(decryptionValuesCycle)


print(''.join(decryptList))
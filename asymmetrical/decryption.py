def readMessage():
    mysteryFile = open("asymmetrical/encryptedFile.txt", "r")
    mysteryMessage = mysteryFile.readlines()
    mysteryFile.close()

    encryptedMessage = mysteryMessage[0]
    secretKey = int(mysteryMessage[2])

    messageChars = encryptedMessage.split()

    for item in range(len(messageChars)):
        messageChars[item] = int(messageChars[item]) // secretKey
        messageChars[item] = chr(messageChars[item])
    
    decryptedMessage = "".join(messageChars)
    
    decryptedFile = open("asymmetrical/decryptedFile.txt", "w")
    decryptedFile.write(decryptedMessage)
    
readMessage()
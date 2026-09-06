import createSecretKey as secret

message = input("write your message to send ")

def sendMessage(message):
    cypher = [ord(char) for char in message]
    
    secretKey = secret.createKey()
    
    encryptedMessage = []

    for char in cypher:
        encryptedMessage.append(char*secretKey)
    
    encryptedFile = open("asymmetrical/encryptedFile.txt", 'w')

    for char in encryptedMessage:
        encryptedFile.write(str(char) + " ")

    encryptedFile.write("\n\n" + str(secretKey))
    encryptedFile.close()

sendMessage(message)
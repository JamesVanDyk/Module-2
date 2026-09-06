SHARED_KEY = 6

message = input("input your message ")

def sendMessage(message):
    cypher = [ord(char) for char in message]

    encryptedMessage = []

    for char in cypher:
        encryptedMessage.append(char*SHARED_KEY)

    encryptedFile = open("symmetrical/encryptedFile.txt", 'w')
    
    for char in encryptedMessage:
        encryptedFile.write(str(char) + " ")

sendMessage(message)
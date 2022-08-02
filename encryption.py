# author: Claire Nguyen
# date: August 2, 2022
# The purpose this program is to utilize the Fernet module for basic symmetric encryption
# credit to geeksforgeeks for basic encryption code

from cryptography.fernet import Fernet

# generate key
def generateKey(fileName):
    key = Fernet.generate_key()
    with open(fileName, "wb") as keyFile:
        keyFile.write(key)
    return key

# encrypt message
def encryptMessage(data, key):
    f = Fernet(key)
    encryptedMessage = f.encrypt(data)
    return encryptedMessage, key

# decrypt message
def decryptMessage(data, key):
    f = Fernet(key)
    decryptedMessage = f.decrypt(data)
    return decryptedMessage, key

# main method to utilize encryption/decryption/key functions
def main():
    
    question1 = input("Do you have a pre-existing file to encrypt or decrypt? Yes or no: ")
    
    if(question1.lower() == "yes"):
        
        fileName = input("Enter file name (eg: file.txt): ")
        data = open(fileName, "rb").read()
        
        question1a = input("Type '1' if you are encrypting this file or '2' if you are decrypting it: ")
        
        if(question1a == "1"):
            keyFile = input("Create a name for the file to store your key: ")
            keyFile += ".key"
            key = generateKey(keyFile)
        else:
            question1b = input("Type '1' if you have a key file or '2' if you would like to manually enter your 32 bit key: ")
            if(question1b == "1"):
                fileName = input("Enter the name of the key file (eg: key.key): ")
                key = open(fileName, "rb").read()
            else: 
                key = input("Enter the 32 bit key: ")
            
            message, key = decryptMessage(data, key)
    
            print("key:       " + str(key))
            print("message:   " + str(message))
            fileName = input("Enter the name of the new file to store your decrypted message: ")
            fileName += ".txt"
            with open(fileName, "wb") as messageFile:
                messageFile.write(message)
                
            print("Congratulations! You have decrypted a file.")
    
        exit()
            
    else:
        question2 = input("Do you want to write a new message to encrypt? Yes or no: ")
    
        if(question2.lower() == "yes"):
            data = input("Type the message you want to encrypt: ").encode()
            keyFile = input("Create a name for the file to store your key: ")
            keyFile += ".key"
            key = generateKey(keyFile)
            
            message, key = encryptMessage(data, key)
            
            print("key:       " + str(key))
            print("message:   " + str(message))
            fileName = input("Enter the name of the new file to store your encrypted message: ")
            fileName += ".txt"
            with open(fileName, "wb") as messageFile:
                messageFile.write(message)
                
            print("Congratulations! You have encrypted a message.")
    
            exit()
            
        else:
            print("Bye.")
            exit()
    
if __name__ == '__main__':
    main()

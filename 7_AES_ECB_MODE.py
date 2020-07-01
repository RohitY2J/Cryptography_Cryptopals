from Crypto.Cipher import AES
import base64

#read the file
def read_file(file_name):
    file = open(file_name,'r')
    return file.read()

file_name = "7_AES.txt"
key = 'YELLOW SUBMARINE'
#define the AES object in the ECB mode
decipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
#read the base64 encoded file and decode it
encrypted_msg = base64.b64decode(read_file(file_name))
print(encrypted_msg)
#decrypt the message and store in variable
decrypted_msg = decipher.decrypt(encrypted_msg)
print(decrypted_msg.decode())

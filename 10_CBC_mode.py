from Crypto.Cipher import AES
from binascii import hexlify, unhexlify
import random

def add_padding(msg, desired_size, padded_byte = '\x04'):
    pad_msg = msg
    if(len(msg)%desired_size != 0):
        #get the number of difference byte
        diff =  16 - len(msg)%desired_size
        #make the padded byte of same length
        padding = padded_byte*diff
        #add the pad to the msg
        pad_msg = msg + padding
    return pad_msg

def xor_msg(msg1, msg2):
    #xor_two messages
    xor_msg = bytes([a^b for (a,b) in zip(msg1.encode(), msg2.encode())])
    #convert back to ascii
    return xor_msg.decode()


#encrypt the msg in ecb mode(repeated key)
def AES_ECB_Encrypt(msg, key):
    #msg = add_padding(msg, 16)
    #declare AES object
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    #encrypt the msg, msg should be passed in binary form(bytes)
    encrypted_msg = cipher.encrypt(msg.encode())
    #return the hex 
    return hexlify(encrypted_msg).decode()

#decrypt the encrypted msg
def AES_ECB_Decrypt(encrypted_msg, key):
    #declare object
    decipher = AES.new(key.encode(), AES.MODE_ECB)
    #decrypt the msg, pass the hex bytes as arg b'\xaa'
    #returns the ascii bytes
    decrypted_msg = decipher.decrypt(unhexlify(encrypted_msg))
    return decrypted_msg.decode()

def AES_CBC_Encrypt(msg, iv, key):
    msg = add_padding(msg, 16)
    msg_enc_lst = []
    msg_num_blocks = len(msg)//16
    for i in range(msg_num_blocks):
        #returns the xor
        xor_block = xor_msg(msg[i*16:(i+1)*16], iv)
        #returns the encrypted string
        iv = AES_ECB_Encrypt(xor_block,key)
        msg_enc_lst.append(iv)
    return ''.join(msg_enc_lst)

def AES_CBC_Decrypt(encr, iv, key):
    msg_lst = []
    msg_num_blocks = len(encr)//32
    for i in range(msg_num_blocks):
        #data in hex so take two data for one byte 
        step = encr[i*32:(i+1)*32]
        #decrypt the byte
        ebc_decrypted = AES_ECB_Decrypt(step, key)
        #xor the message
        xord_msg = xor_msg(ebc_decrypted, iv)
        iv = step
        msg_lst.append(xord_msg)
    return ''.join(msg_lst)
        

iv = 'lahdoldmcjdueodp'   
key = "YELLOW SUBMARINE"
enc =  AES_CBC_Encrypt('Hello there how are you my frien?dlopklikegarnehai ta',iv,key)
print(enc)
print(AES_CBC_Decrypt(enc, iv, key))



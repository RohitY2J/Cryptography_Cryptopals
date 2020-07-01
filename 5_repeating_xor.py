from binascii import unhexlify

#read files and return the string
def read_file(file):
    file1 = open(file,'r')
    return file1.read()

#convert the string to bytes
def ascii_to_hex_str(string):
    int_arr = []
    for i in string:
        #convert the character to int and append it
        int_arr.append(ord(i))
    #convert the integer array to bytes 
    return bytes(int_arr)

#perform xor and return xored bytes
def repeated_xor(msg_val, key_val):
    #scale to be multiplied
    scale = int(len(msg_val)/len(key_val))
    #offset to be added in case the len of msg is not multiple of 3
    offset = len(msg_val)%len(key_val)
    #multiply the key with scale
    key_val = key_val * scale
    #convert the bytes to bytearray to append the extra I or C or E 
    key_val_bytearray = bytearray(key_val)
    for i in range(offset):
        key_val_bytearray.append(key_val[i])

    #convert byte array back to bytes
    key_val = bytes(key_val_bytearray)
    return bytes([a^b for (a,b) in zip(msg_val, key_val)])

msgs = read_file("5.1_repeating_xor.txt")
key = "ICE"
hex_msgs = ascii_to_hex_str(msgs)
#obtain the length of upper line
sep = hex_msgs.index(b'\n')
hex_key = ascii_to_hex_str(key)

#encrypted message after xoring with repeated key
encrypt_msgs = repeated_xor(hex_msgs, hex_key)
print(hex_msgs[:sep])
print(encrypt_msgs[0:sep].hex())
print(hex_msgs[sep:])
print(encrypt_msgs[sep:].hex())


#print(encrypt_msgs)


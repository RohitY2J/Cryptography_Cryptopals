from Crypto.Cipher import AES
from binascii import unhexlify

#read file
def read_file(file_name):
    file = open(file_name, 'r')
    return file.read()

#check if the enc_msg is AES encrypted or not
def is_AES_encrypted(enc_msg):
    #convert the hex into bytes
    enc_msg = unhexlify(enc_msg)
    #AES encrypts into block size 16
    blocksize = 16
    #check if the total length is multiple of 16
    if(len(enc_msg)%16 == 0):
        #get the number of blocks
        number_of_blocks = len(enc_msg)//16
        for i in range(number_of_blocks):
            j=i+1
            #for all blocks compare the each block with one another
            #if matched return true
            while j < number_of_blocks-1:
                if enc_msg[i*blocksize:(i+1)*blocksize] == enc_msg[j*blocksize:(j+1)*blocksize]:
                    print(enc_msg[i*blocksize:(i+1)*blocksize])
                    print(enc_msg[j*blocksize:(j+1)*blocksize])
                    print(enc_msg)
                    return True
                j += 1
    else:
        return False

    #for those who have 16 length but are not AES encrypted
    return False

hex_msg = read_file("8_AES_detection.txt")

#split each line into list
hex_lst = hex_msg.splitlines()

flag = False
ans = ''
for i in hex_lst:
    flag = is_AES_encrypted(i)
    if flag == True:
        ans = i
        
        break

print(ans)


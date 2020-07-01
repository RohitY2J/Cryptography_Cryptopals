import base64
from binascii import unhexlify

#returns the score for the plain text
def ascii_ratio(val):
    ascii_text_chars = list(range(97, 122)) + [32]
    letters = sum([ x in ascii_text_chars for x in val])
    return letters / len(val)

def ascii_to_bin_str(string):
    int_arr = []
    for i in string:
        #convert the character to int and append it
        int_arr.append(ord(i))
    #convert the integer array to bytes 
    return bytes(int_arr)

#hamming_distance("this is a test","wokka wokka!!!")=37
def hamming_distance(inp1, inp2):
    #convert the string to bytes
    bin1 = ascii_to_bin_str(inp1)
    bin2 = ascii_to_bin_str(inp2)
    #to find the number of different bits xor the two bytes
    xor_bytes =  bytes([a^b for (a,b) in zip(bin1, bin2)])
    #define variable to count the number of ones
    length = 0
    for i in xor_bytes:
        #convert the byte in to binary number
        binary_val = bin(i)
        #get the number of 1's in the binary number and add it
        #[2:] first two skipped as it is 0b
        length = length + len([ones for ones in binary_val[2:] if ones == '1'])
    
    return length

#read files and return the string
def read_file(file):
    file1 = open(file,'r')
    return file1.read()

def decode_base64(base64_msg):
    #encode to bytes
    base64_bytes = base64_msg.encode()
    msg_bytes = base64.b64decode(base64_bytes)
    #decode to string
    return msg_bytes.decode()

def find_keysize(enc_val):
    #array for storing the keysiz
    key_size_array = []
    #array for storing distance score of each key
    distance_array = []
    for i in range(39):
        keysize = i+2
        #we need to take lengths
        #so second last division convers the last block
        no_of_blocks = len(enc_val)//keysize - 1
        #print(no_of_blocks)
        score_at_each_loop = 0
        #operation as (1 block,2 block), (2 block, 3 block), (3,4), (4,5)
        for j in range(no_of_blocks):
            #print(first_chunk)
            first_chunk = enc_val[j*keysize:(j+1)*keysize]
            #print(second_chunk)
            second_chunk = enc_val[(j+1)*keysize:(j+2)*keysize]
            #distance between two chunks
            distance = hamming_distance(first_chunk, second_chunk)
            #find the score between two chunks for specific keysize 
            score_at_each_loop = score_at_each_loop +  distance
        #normalize the score obtained
        normalized_score = score_at_each_loop/keysize
        #find the avg score
        avg_score = normalized_score/no_of_blocks
        #store the keysize 
        key_size_array.append(keysize)
        #store the score for each keysize
        distance_array.append(avg_score)
    #find the index for smallest score i.e. smallest hamming distance
    index = distance_array.index(min(distance_array))

    #extra code if there are more than one keysize that has same length
    '''
    sorted_score = sorted(distance_array)
    smallest_scores = []
    for k in range(3):
        index = distance_array.index(sorted_score[k])
        #smallest_scores.append([i+2 for i, e in enumerate(distance_array) if e == sorted_score[k]])
        smallest_scores.append(key_size_array[index])
    '''
    return key_size_array[index]

#to separate the each encoded byte for specific key
def separate_blocks(enc_val, keysize):
    #list to store all the blocks
    blocks = []
    #define an empty string for all the keys in the keysize
    for i in range(keysize):
        blocks.append('')

    #separate the blocks
    for j in range(len(enc_val)):
        #we can find the corresponding index of each byte using % sign
        # 1%29 = 1
        # for 29 we get 0, so establish an extra condition 
        if (j+1)%keysize == 0:
            blocks[keysize-1] += enc_val[j]
        else:
            blocks[(j+1)%keysize-1] += enc_val[j]
    
    return blocks

#find the byte to be xor'd with particular block
#code from previous section
def find_xor_byte(msg):
    msg = msg.encode()
    score = []
    ans = []
    keys = []
    for j in range(255):
        counter = bytes([1+j])
        key = len(msg)*counter
        decrypt = bytes([ x^y for (x,y) in zip(msg, key)])
        ans.append(decrypt)
        keys.append(j+1)
        score.append(ascii_ratio(decrypt))
    index = score.index(max(score))
    
    return keys[index]


#get the base64 encoded message
base64_msg = read_file("6_break_repeating_key_xor.txt")
#get the base64 decoded message
message = decode_base64(base64_msg)

#find the best keysize
keysize = find_keysize(message)
#separate the blocks on the basis of the keys
sep_blocks = separate_blocks(message, keysize)
key_list = []
for i in sep_blocks:
    key_list.append(find_xor_byte(i))

print(keysize)
print(bytes(key_list))





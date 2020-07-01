import codecs

hex1= "1c0111001f010100061a024b53535009181c"
hex2 = "686974207468652062756c6c277320657965"

#extract the hex value into hex variable
hex1_val = codecs.decode(hex1, 'hex')
hex2_val = codecs.decode(hex2, 'hex')

#declare a variable
hex_or = ''

#xor each element and 
for i in range(len(hex1_val)):
    x = hex1_val[i] ^ hex2_val[i]
    #convert the int obtained as result into hex and store them
    hex_or = hex_or+hex(x)

#split the hex string in '0x' representation characters
hex_or_split = hex_or.split('0x')

hex_or_str = ''
for i in hex_or_split:
    #concat all the array elements
    hex_or_str = hex_or_str+i
print(hex_or_str)

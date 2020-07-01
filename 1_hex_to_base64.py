import codecs

hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print(hex_str)
print("\n")
#generates 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
#since it is string

#get the hex value from the above string
hex_val = codecs.decode(hex_str,'hex')
print(hex_val)
print("\n")
#generates b"I'm killing your brain like a poisonous mushroom"
#since it is in hex form so converts to ascii before printing

#get the encoded base64 value
base64_val = codecs.encode(hex_val, 'base64')
print(base64_val)
print("\n")
#generates b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t\n'
#which is in base64 encode


#get the string of base64
base64_str = base64_val.decode()
print(base64_str)

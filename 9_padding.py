#adds padding at the end of the supplied message
def add_padding(msg, desired_size, padded_byte = '\x04'):
    #get the number of difference byte
    diff = desired_size - len(msg)
    #make the padded byte of same length
    padding = padded_byte*diff
    #add the pad to the msg
    pad_msg = msg + padding
    return pad_msg

pad_msg = add_padding("Yellow Submarine", 20)
print(pad_msg)

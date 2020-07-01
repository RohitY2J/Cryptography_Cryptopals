from binascii import unhexlify

def ascii_ratio(val):
    ascii_text_chars = list(range(97, 122)) + [32]
    letters = sum([ x in ascii_text_chars for x in val])
    return letters / len(val)

input_sup = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
score = []
ans = []
keys = []
for i in range(255):
    counter = bytes([1+i])
    msg = unhexlify(input_sup)
    key = len(msg)*counter
    decrypt = bytes([ x^y for (x,y) in zip(msg, key)])
    ans.append(decrypt)
    keys.append(i+1)
    score.append(ascii_ratio(decrypt))

index = score.index(max(score))
print(score[index])
print(keys[index])
print(ans[index])



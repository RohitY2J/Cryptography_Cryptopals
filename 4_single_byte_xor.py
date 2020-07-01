from binascii import unhexlify

def ascii_ratio(val):
    ascii_text_chars = list(range(97, 122)) + [32]
    letters = sum([ x in ascii_text_chars for x in val])
    return letters / len(val)

def read_file(file):
    file1 = open(file,'r')
    return file1.read()

string = read_file("info.txt")
lst = string.splitlines()
aggr_ans = []
aggr_score = []
aggr_keys = []
for i in lst:
    score = []
    ans = []
    keys = []
    for j in range(255):
        counter = bytes([1+j])
        msg = unhexlify(i)
        key = len(msg)*counter
        decrypt = bytes([ x^y for (x,y) in zip(msg, key)])
        ans.append(decrypt)
        keys.append(j+1)
        score.append(ascii_ratio(decrypt))
    index = score.index(max(score))
    aggr_ans.append(ans[index])
    aggr_score.append(score[index])
    aggr_keys.append(keys[index])
aggr_index = aggr_score.index(max(aggr_score))
print(aggr_score[aggr_index])
print(aggr_keys[aggr_index])
print(aggr_ans[aggr_index])
    

#print(lst)

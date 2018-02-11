import operator

f = open('words2.txt', encoding='utf8')
lines = f.readlines()

dow = []
for line in lines:
    dow.append(line.lower().replace('\n', ''))

pairs = {}
for line in dow:
    last = ' '
    for ch in line:
        if (ch < 'а' or ch > 'я') and ch != ' ':
            continue
        pair = last + ch
        last = ch
        n = pairs.get(pair, 0)
        pairs[pair] = n + 1
#print(pairs)

x = pairs 
sorted_pairs = sorted(x.items(), key=operator.itemgetter(1), reverse=True)

dow = []
for line in lines:
    dow.append(line.lower().replace('\n', ''))

pairsW = {}
for line in dow:
    last = ' '
    words = line.split()
    for word in words:
        n = pairsW.get(word, 0)
        pairsW[word] = n + 1 #len(word) #len for small lists
#print(pairs)

x = pairsW 
sorted_words = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
#print(sorted_x)

count = 0
for pair in sorted_words:
    count += 1
    if count < 0: break
    #print(pair)
    if count % 50 == 0:
        print(count)
print(count)

'''
# find minimum count of words, contains all alpha-pairs
1. Find most popular words
30657 words with numbers
2. Select only with unic pairs
3. Delete dublicates
'''

words1 = []
words1_ = []
ps = pairs.copy()
yesno = [0, 0]
for word_pair in sorted_words:
    last = ' '
    word = word_pair[0]

    for ch in (word+' '):
        pair = last + ch
        last = ch
        if ps.get(pair, 0) > 0:
            yesno[0] += 1
            yesno.append(pair)
            #ps[pair] = 0
            pairs_in = []
            words1_.append((word, pairs_in))
            words1.append(word)
            lastd = ' '
            for chd in word:
                if (chd < 'а' or chd > 'я') and ch != ' ':
                    continue
                paird = lastd + chd
                if ps.get(paird, 0) > 0:
                    pairs_in.append(paird)
                    ps[paird] = 0
                lastd = chd
            ps[lastd+' '] = 0
            pairs_in.append(lastd+' ')
        else:
            yesno[1] += 1

print(len(words1))
print(len(sorted_words))
print(yesno)

fout = open('words2.txt', 'w', encoding="utf8")
for word in words1:
    fout.write(word + ' ')
fout.close()

fout = open('words2_.txt', 'w', encoding="utf8")
for word in words1_:
    fout.write(str(word) + ' \n')
fout.close()

fout = open('words2_dict.txt', 'w', encoding="utf8")
pair_list = []
for word in words1_:
    fout.write('{"' + str(word) + '",')
    for pair in word[1]:
        fout.write('{"' + str(pair) + '", [0.00, 1.00] },\n')
fout.close()


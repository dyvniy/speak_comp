import operator

f = open('kniga.txt', encoding='utf8')
lines = f.readlines()

print(lines[2])

dow = []
for line in lines:
    dow.append(line.lower().replace('\n', ''))

print(dow[2])

pairs = {}
for line in dow:
    last = ' '
    words = line.split()
    for word in words:
        n = pairs.get(word, 0)
        pairs[word] = n + 1
#print(pairs)

x = pairs 
sorted_words = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
#print(sorted_x)

count = 0
for pair in sorted_words:
    count += 1
    if count < 0: break
    print(pair)
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

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
    for ch in line:
        if (ch < 'а' or ch > 'я') and ch != ' ':
            continue
        pair = last + ch
        last = ch
        n = pairs.get(pair, 0)
        pairs[pair] = n + 1
#print(pairs)

import operator
x = pairs 
sorted_pairs = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
#print(sorted_x)

count = 0
for pair in sorted_pairs:
    count += 1
    if count < 0: break
    print(pair)
    if count % 50 == 0:
        print(count)
print(count)

'''
# find minimum count of words, contains all alpha-pairs
1. Find most popular words
2. Select only with unic pairs
3. Delete dublicates
'''

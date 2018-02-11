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
            ps[pair] = 0
            pairs_in = []
            words1_.append((word, pairs_in))
            words1.append(word)
            lastd = ' '
            for chd in word:
                paird = lastd + chd
                pairs_in.append(paird)
                ps[paird] = 0
                lastd = chd
            ps[lastd+' '] = 0
        else:
            yesno[1] += 1

print(len(words1))
print(len(sorted_words))
print(yesno)
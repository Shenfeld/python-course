a = open("yazkora.txt", "r")
text = a.read().replace("\n", " ").split(".")
out = open('answer.txt', 'w')
for sent in text:
    for word in sent.split(' '):
        if word.endswith ('yo'):
            out.write(word)
    out.write('\n')
out.close()

a = open("yazkora.txt", "r")
text = a.read().replace("\n", " ").split(".")
out = open('answer.txt', 'w')
space = ' '
for sent in text:
    for word in sent.split(space):
        if word.endswith ('yo'):
            out.write(word + space)
    out.write('\n')
out.close()

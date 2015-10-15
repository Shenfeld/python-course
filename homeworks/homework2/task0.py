def plural(n, words):
    n1 = n % 10
    n2 = n % 100
    if n1 == 0 or 5 <= n1 <= 9 or 10 < n2 < 15:
        return str(str(n) + " " + words[2])
    elif n1 == 1:
        return str(str(n) + " " + words[0])
    elif 2 <= n1 <= 4 and (n2 != 12 or n2 != 13 or n2 != 14):
        return str(str(n) + " " + words[1])
words_iron = ['утюг', 'утюга', 'утюгов']
words_spoon = ['ложка', 'ложки', 'ложек']
words_music = ['гармошка', 'гармошки', 'гармошек']
words_teapot = ['чайник', 'чайника', 'чайников']
word = input()
count = int(input())
if word == 'утюг':
    proper_word = plural(count, words_iron)
if word == 'ложка':
    proper_word = plural(count, words_spoon)
if word == 'гармошка':
    proper_word = plural(count, words_music)
if word == 'чайник':
    proper_word = plural(count, words_teapot)
print (proper_word)

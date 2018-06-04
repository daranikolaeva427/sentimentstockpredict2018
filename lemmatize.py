# this line of code lemmatizes corpus (needs mystem installed)

from pymystem3 import Mystem
mystem = Mystem()
text = open('corpus.txt').read()
for line in text:
    lemmas = mystem.lemmatize(line)
	print(line)


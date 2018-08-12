import nltk
import pandas
corpus = nltk.corpus.gutenberg.fileids()

def lexical_diversity(text): # http://www.nltk.org/book_1ed/ch01.html#ref-fun-parameter1
     return len(text) / len(set(text))
    
d = {}
for t in corpus:
    d[t] = lexical_diversity(nltk.corpus.gutenberg.words(t))

df = pandas.DataFrame(list(d.items()), columns=['Text','LexDiv'])


import wikipedia
from random_word import RandomWords

word = RandomWords()
w = word.get_random_word()
print(w)
wikipedia.summary(w)
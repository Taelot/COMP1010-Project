import wikipedia
import re
from random_word import RandomWords
answer = RandomWords().get_random_word()
print(answer)
tgt = wikipedia.search(answer,results=1)[0]
print(tgt)
result = wikipedia.summary(tgt)
print(result)
result = re.sub(tgt,"?????", result)
result = re.sub(tgt.lower(), "?????", result)
print(result)
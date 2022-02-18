from collections import Counter

def duplicate_count(text):
    return sum([x > 1 for x in Counter(text.lower()).values()])
    
text = "abAcDvdaBB"

print(duplicate_count(text))
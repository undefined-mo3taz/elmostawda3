sentance= input("enter the words")
words=sentance.split()
for word in words:
    stack=list(word)
    reversed_word=""
    while stack:
        reversed_word+=stack.pop()
    print(reversed_word, end=" ")
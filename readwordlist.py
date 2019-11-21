# Connect to the file

fin = open("wordlist.txt")

for word in fin:
    if 'or' in word:
        print(word.strip())

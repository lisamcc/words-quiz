# Words Quiz, Lisa McClellan

with open('words_alpha.txt', 'r') as f:
    words = f.read().splitlines()

print(len(words))

count = 0
for w in words:
    if len(w)==5:
        count+=1
print(count)

count = 0
for w in words:
    if len(w) > 7:
        count+=1
print(count)

characters=0
for w in words:
    characters+=len(w)
print(characters)

count=0
for w in words:
    if "e" not in w:
        count += 1
print(count)

first_last = 0
for w in words:
    if w[0]==w[-1]:
        first_last+=1
print(first_last)

count=0
    

count=0
for w in words:
    for i in range(len(w)-):
        if w[i] == "q" and w[i+1] != "u":
            count +=1
    



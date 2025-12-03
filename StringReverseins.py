word = str(input("please enter a word:"))

re_word=""

i = len(word)-1

while i >=0:
    re_word += word[i]

    i-=1
print(re_word)
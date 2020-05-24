# tathastu_week_of_code
ize=int(input("enter the no of wordsyou want to add in dictionary"))
dict=[]
for i in range(size):
    dict.append(input("enter the word" + str(i+1) +": "))
size=int(input("enter the no of character youwant ro add in array"))
array=[]
result=[]
print("enter the character in array one by one")
for i in range(size):
    array.append(input())
for word in dict:
if set(word).issubset(set(array)):
result.append(word)
print(",".join(result + "."))


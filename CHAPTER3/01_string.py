name = "Khushi"

nameshort = name[0:3] #start from index 0 all the way till 3 (excluding 3)
print(nameshort)
character1 = name[1]
print(character1)

# negative slicing
# k h u s h i
#  0  1  2  3  4  5 in positive indexing
# -6 -5 -4 -3 -2 -1 in negative indexing
print(name[-4:-1])
print(name[2:5])

print(name[:4]) #nothing written means 0 and at 4 it is -1

print(name[1:]) # is same as print(name[1:6])
print(name[1:6])
# skip slicing
word = "khushi"
print(word[1:6:2]) 
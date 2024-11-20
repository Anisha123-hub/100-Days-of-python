# Length of a string

fruit = "mango"
len1 = len(fruit)
print("Mango is a", len1,"letter word.")

# String as an array
pie = "ApplePie"
print(pie[:5])
print([6])

# Slicing ecample
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index

# loop through a string
alphabets = "ABCDE"
for i in alphabets:
    print(i)
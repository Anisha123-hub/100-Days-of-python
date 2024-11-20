# String methods
# Upper():

str1 = "AbcDEfghIJ"
print(str1.upper())

# lower():

str1 = "AbcDEfghIJ"
print(str1.lower())

# Strip():
str2 = " Silver Spoon "
print(str2.strip)

# rstrip():
str3 = "Hello !!!"
print(str3.rstrip("!"))

# replace():
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))

# Split():
str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".

# Capitalize():
str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)

# Center():
str1 = "Welcome to the Console!!!"
print(str1.center(50))

# Count():
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)

# endswith():
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

# Find():
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))

# Index():
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))

# isalnum():
str1 = "WelcomeToTheConsole"
print(str1.isalnum())

# isalpha():
str1 = "Welcome"
print(str1.isalpha())

# islower():
str1 = "hello world"
print(str1.islower())

# isprintable():
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())

# isspace():
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

# istitle():
str1 = "World Health Organization" 
print(str1.istitle())

# isupper():
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())

# startswith():
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

# swapcase():
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

# title():
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())



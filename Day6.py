# Explicit typecasting

string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)

# implicit type casting
a = 7
print(type(a))
 
# python automatically converts b to flaot
b = 3.0
print(type(b))
 
# python sutomatically converts c to float
c = a + b 
print(c)
print(type(c)) 
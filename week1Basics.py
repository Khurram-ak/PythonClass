# Question 1
str1="james"

# Index 01234
# length 12345

first=str1[0]
mid=str1[2]
last=str1[len(str1) -1]

print("***************************")
print( "first, middle & last character of string james is : ", first + mid + last)

# Question 2

str2="jonDipPeta"

print("***************************")
print("Middle value of input string jonDipPeta : ",str2[3:6])

# Question 3

str3="Aultar"
str4="World"

mid = int(len(str3)/2)

result = str3[0:mid] + str4 + str3[mid:]
            
            
print("***************************")
print("Adding string World in middle of string Ault : ",result)

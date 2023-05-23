#A four-digit integer is given. Find the number of odd digits in it.
var_int=4586
#Create a variable "var_int" and assign it a four-digit integer value.
def main(var_int):
    return (var_int//1000)% 2 + (var_int//100)%2 + (var_int//10)%2 + var_int%2
#Print the number of odd digits in the variable "var_int".
print(main(4586))

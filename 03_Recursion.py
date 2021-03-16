#its a way of using a function inside a funtion.
# some of n natural no.

n = int(input("please enter the number u want to find the sum of \n"))

def sumOfNaturalnos(n):
    if n == 0:
       return 0
    else:
        return n+sumOfNaturalnos(n-1)

    

print(sumOfNaturalnos(n))

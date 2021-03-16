def greet(name="stranger"):#stranger will work as default argument 
    print("Good day,   "+name)

greet("irfan")
greet()

def sumOf2no(num1,num2=5):
    return(num1+num2)

print(sumOf2no(2,9))

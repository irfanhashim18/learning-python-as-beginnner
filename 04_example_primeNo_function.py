def primeNo(num):
    for n in range(2,num):
        if num % n == 0:
            print(str(num)+"Not a prime No")
            break
        else:
            print(str(num)+"is a prime no")
    else:
        print(f'{num}is a prime no')

primeNo(1)

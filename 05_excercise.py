
'''LESSER OF TWO EVENS: Write a function that returns the lesser 
of two given numbers if both numbers are even, but returns the greater
if one or both numbers are odd
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5'''

def lesser_of_two_evens(x,y):
    even= True
    for i in (x,y):
        if i % 2 == 0: 
            even = True
        else:
            even = False
    if even:
        print(min(x,y))
    else:
        print(max(x,y))

lesser_of_two_evens(2,8)


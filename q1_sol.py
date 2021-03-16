def maximum(x,y,z):
    if (x > y):
        if (x >z):
            return x
        else:
            return z
    else:
        if(y>z):
            return y
        else:
            return z
        



m = maximum(4,8,7)
print("the greatest is" + str(m))

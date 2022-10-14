w=int(input("Enter your weight "))
a=input("Is it in kg(K) or gram (G) ")
if a.upper()=="K": #if (a=="k" or a=="K")
    w = w * 1000
else:
    w= w / 1000
print("The converted weight is ", w)

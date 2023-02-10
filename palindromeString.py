#How can you reverse a string?

a="2112"
b=list(a)
print(b)


def reverse1(b):
    c=[]
    for i in range(len(b)):
        c.append(b[len(b)-1-i])
    
    return(c)  
    

print(reverse1(b))
if(b==reverse1(b)):
    print("Es palindromo")
else:
    print("It is not palindrome")

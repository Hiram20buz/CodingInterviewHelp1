#How can you reverse a string?

a="hola compa"
b=list(a)
print(b)
#print(len(b))
#print(b[0])

#Metodo 1
def reverse1(b):
    c=[]
    for i in range(len(b)):
        c.append(b[len(b)-1-i])
    
    print(c)  
    
reverse1(b)
    
#Metodo 2
def reverse2(b):
    
    for i in range(int(len(b)/2)):
        temp=b[i]
        b[i]=b[len(b)-1-i]
        b[len(b)-1-i]=temp
    
    print(b) 
 
reverse2(b)   
    

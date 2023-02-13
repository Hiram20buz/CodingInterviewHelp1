#Find the count for the occurrence of a particular character in a string.


#string to list
list1 = list("holaaah")

def contador(lista,letter):
    i=0
    for letra in lista:
        if(letra==letter.lower()):
            i+=1
    return i
            
print(contador(list1,"a"))

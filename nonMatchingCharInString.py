#How to get the non-matching characters in a string?
#How to get the matching characters in a string?
 
# function to get unique values 
def unique(list1):
 
    # initialize a null list
    unique_list = []
 
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
 
 
#squares = {1: 1, 2: 4, 3: 9}
#squares['x'] = None # Adding new key without value
letras={}

#string to list
list1 = list("holaaah")

#list with unique values
palabra=unique(list1)

#Initialize dictionary with zero values for each letter
for letra in palabra:
    letras[letra] =0
    
print(letras)

#Iterate for every unique letter in the string and get the count in the dictonary

for letra in palabra:
    for i in range(len(list1)):
        if(letra==list1[i]):
            #print(i,letra)
            letras[letra]+=1
            
print(letras)

for llave in letras:
    if(letras[llave]==1):
        print(llave)

#How to calculate the number of vowels and consonants in a string?

letras={}

#string to list
hello="hola hola". lower()
list1=list(hello.replace(" ", ""))
print(list1)
letras["Vocales"]=0
letras ["Consonantes"]=0
print(letras)

for letra in list1:
    if(letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u"):
        letras["Vocales"]+=1
        
    else:
        letras["Consonantes"]+=1
        
print(letras)

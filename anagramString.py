#How do you prove that the two strings are anagrams?

a="perro"
b=list(a)
#print(b)

c="peror"
d=list(c)
#print(d)

b.sort()
d.sort()

print(b)
print(d)

if(b==d):
    print("Es anagrama")
else:
    print("No es anagrama")

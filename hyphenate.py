s = input("Enter any number: ")
w = s[0]
m = ""
i = 1 
while (i<int(len(s))):
    m += "-" + s[i] 
    i += 1
print(w + m)

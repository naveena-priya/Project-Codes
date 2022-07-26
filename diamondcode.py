n = int(input("Enter any number: "))
s1 = n-1 
s2 = 0 
for i in range(1,n+1):
    print(s1 * " " + "/" + s2 * " " + "\\")
    s1 -= 1 
    s2 += 2
s3 = 0 
s4 = 2*n-2 
for j in range(1,n+1):
    print(s3 * " " + "\\" + s4 * " " + "/")
    s3 += 1 
    s4 -= 2





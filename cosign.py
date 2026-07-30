x = float(input("Enter the value of x: "))
n = int (input("Enter the value of terms: "))

sum = 1
fact = 1
sign =-1

for i in range(2,n+1,2):
    fact = 1
    for j in range (1,i+1):
        fact =fact *j

    sum = sum + sign *(x **i) / fact
    sign = sign * -1

print("cos(x) =",sum)       

print("Enter the value of a,b and c of quadratic equation:")
a,b,c=int(input()),int(input()),int(input())
d=b**2-4*a*c
if d>0:
       print("Real and distint roots") 
elif d==0:
       print("Real and equal roots")
else:
       print("Imaginary roots")           
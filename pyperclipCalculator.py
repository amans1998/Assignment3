print("paste the values")
c=input()
import pyperclip
a=int(pyperclip.paste())
print(a)
c=input()
b=int(pyperclip.paste())
print(b)
print("what operation you want to execute")
print("for addition type add")
print("for subtraction type sub")
print("for multiplication type multi")
print("for division type div")
print("for modulus type mod")
print("for float division type fdiv")
print("for exponent type exp")
s=input()
if s=="add":
    c=a+b
    print("%s + %s = %s" %(a,b,c))
elif s=="sub":
    c=a-b
    print("%s - %s = %s" %(a,b,c))
elif s=="multi":
    c=a*b
    print("%s * %s = %s" %(a,b,c))
elif s=="div":
    c=a/b
    print("%s / %s = %s" %(a,b,c))
elif s=="mod":
    c=a%b
    print("%s modulus %s = %s" %(a,b,c))
elif s=="fdiv":
    c=a//b
    print("%s // %s = %s" %(a,b,c))
elif s=="exp":
    c=a**b
    print("%s ** %s = %s" %(a,b,c))

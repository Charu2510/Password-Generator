import random
#password generation
print("To generate a unique password, Pls enter")
alpha=int(input("No of alphabets"))
num=int(input("No of numbers"))
char=int(input("No of special characters"))
a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
n=["0","1","2","3","4","5","6","7","8","9"]
c=["!","@","#","$","%","^","&","*","_"]
password=""
for i in range(0,alpha):
    d=random.choice(a)
    password+=d
for i in range(0,num):
    e=random.choice(n)
    password+=e
for i in range(0,char):
    f=random.choice(c)
    password+=f
p=list(password)
random.shuffle(p)

w=""
for i in p:
    w+=i
print("Password is",w)   

n=input("enter any number")
o=n
while True :
    str_n=str(n)
    str_rev=str_n[::-1]
    if(str_n==str_rev):
        print(n,"is palin. to",o)
        break
    n=int(str_rev)+int(str_n)

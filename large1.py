a=int(input())
b=int(input())
c=int(input())
if a>b:
    if a>c:
        print(a)
    elif b<c:
        print(c)
elif b>c:
    print(b)
else:
    print(c)

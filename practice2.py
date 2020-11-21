#3つの数を小さい順に表示(3つの数は任意)
a = 10
b = 5
c = 12

if a < b and a < c:
    mini = a
    if b < c:
        maax = c
        mid = b
    else:
        maax = b
        mid = c
elif b < c:
    mini = b
    if a < c:
        maax = c 
        mid = a
else:
    mini = c
    maax = b
    mid = a

print(mini, mid, maax)


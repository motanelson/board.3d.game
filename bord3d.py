print("\033c\033[43;30m\nboard\n")

def board3d(x,y,z):
    b=[]
    a=[]
    aa=[]
    aaa="X"
    for nn in range(x):
        aa=aa+[aaa]
    for n in range(y):
        a=a+[aa]
    for nnn in range(z):
        b=b+[a]
    return b


a=board3d(2,2,2)
print(a)
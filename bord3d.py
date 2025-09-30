print("\033c\033[43;30m\nboard\n")
def saves(files,arrays):
    ll=False
    f1=open(files,"w")
    for n in arrays:
        if ll!=False:
             f1.write(";")
        
        ll=True
        for nn in n:
             l=False
             for nnn in nn:
                 if l:
                     f1.write(", "+str(nnn))
                 else:
                     f1.write(str(nnn))
                 l=True
             f1.write("\n")
    f1.close()

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
saves("my.xyz",a)
print(a)
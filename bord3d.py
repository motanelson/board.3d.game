print("\033c\033[43;30m\nboard\n")
#print("\033c\033[43;30m\nboard\n")
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

# corrigido: cada dimensão é independente
def board3d(x,y,z):
    a=" "
    b=[]
    c=[]
    d=[]
    for xx in range(x):
        b=b+[a]
    for yy in range(y):
        c=c+[b.copy()]
    for zz in range(z):
        d=d+[c.copy()]
    return d


a=board3d(2,2,2)
saves("my.xyz",a)
print(a)
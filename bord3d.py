print("\033c\033[43;30m\nboard\n")
#print("\033c\033[43;30m\nboard\n")
def loads(texts):
    ll=True
    zi=0
    xi=0
    yi=0
    a=[]
    ttt=texts.split(";")
    zi=len(ttt)
    for t in range(zi):
        yyy=ttt[t].split("\n")
        yi=len(yyy)
        for y in range(yi):
            xxx=yyy[y].split(",")
            xi=len(xxx)
            if ll:
                a=board3d(xi,yi,zi)
            ll=False
            for x in range(xi):
                 b=xxx[x].strip()
                 if b=="":
                     a[t][y][x]=" "
                 else:
                     a[t][y][x]=b
    return a
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
def build(lena,incx,incy,incz):
    x=0
    y=0
    z=0
    list1=[]
    for n in range(lena):
        
        l1=[x,y,z]
        list1=list1+[l1]
        x=x+incx
        y=y+incy
        z=z+incz
    return list1 

def mark(list1,array1,value):
    c=0
    for n in list1:
        
        xx=n[0]
        yy=n[1]
        zz=n[2]
        array1[zz][yy][xx]=value
        c=c+1    
    return array1
def board3d(x,y,z):
    return [[[" " for _ in range(x)] for _ in range(y)] for _ in range(z)]

#a=board3d(8,8,8)
#c=build(4,2,2,1)
#d=mark(c,a,"X")
#print(a)
f1=open("my.xyz","r")
var1=f1.read()
f1.close()
a=loads(var1) 
#saves("my.xyz",a)
print(a)
alpha='abcdefghijklmnopqrstuvwxyz'
al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alcomp=[]
alrep=al.copy()
def encrypt(x,y,z):
    encrypted=''
    ystr=''
    compstr=''
    pos=alpha.rfind(z)
    xsec=y[0:(26-pos)]
    if(pos!=0):
        xfir=y[(26-pos):26]
    for i in range(0,len(xfir)):
        alcomp.append(xfir[i])
    for i in range(0,len(xsec)):
        alcomp.append(xsec[i])
    for i in y:
        ystr=ystr+i
    for i in alcomp:
        compstr=compstr+i
    for i in x:
        pos1=alpha.rfind(i)
        encrypted=encrypted+compstr[pos1]
    print('The encrypted message is:',encrypted)
    
def decrypt(x,y,z):
    decrypted=''
    ystr=''
    compstr=''
    pos=alpha.rfind(z)
    xsec=y[0:(26-pos)]
    if(pos!=0):
        xfir=y[(26-pos):26]
    for i in range(0,len(xfir)):
        alcomp.append(xfir[i])
    for i in range(0,len(xsec)):
        alcomp.append(xsec[i])
    for i in y:
        ystr=ystr+i
    for i in alcomp:
        compstr=compstr+i
    print(compstr)
    for i in x:
        pos1=compstr.rfind(i)
        decrypted=decrypted+alpha[pos1]
    print('The decrypted message is:',decrypted)
    
xin=input('Enter the message: ')
yin=input('Enter the key: ')
xl=list(yin)
xuni=[]
for i in xl:
    if i not in xuni:
        xuni.append(i)
for i in xuni:
    alrep.remove(i)
for i in range(0,len(alrep)):
    xuni.append(alrep[i])
zin=input('Enter the index: ')
choice=input('Enter 1 to Encrypt and 2 to Decrypt: ')
if(choice=='1'):
    encrypt(xin,xuni,zin)
else:
    decrypt(xin,xuni,zin)

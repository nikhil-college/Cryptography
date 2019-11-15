def cipherpattern(key):
    alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    skey=[]
    for i in key:
        if i not in skey:
            skey.append(i)
    skey1=list(skey)
    skey.sort(key=lambda x:ord(x))
    klen = len(skey)
    prorder=[]
    for i in skey:
        prorder.append(skey1.index(i))
        alpha.remove(i)
    seglen = len(alpha)//klen
    seg = []
    for i in range(seglen):
        seg.append(alpha[klen*i:klen*(i+1)])
    rem = alpha[klen*seglen:]
    cipher = []
    for i in prorder:
        if i<len(skey):
            cipher.append(skey1[i])
        for j in range(seglen):
            cipher.append(seg[j][i])
        if len(rem)!=0:
            cipher.append(rem[0])
            rem.pop(0)
    return cipher

key = input('enter the key').upper()
org = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cip = cipherpattern(key)
message = input('enter message').upper()
enm = ''
for i in message:
    enm+=cip[org.index(i)]
print(enm)
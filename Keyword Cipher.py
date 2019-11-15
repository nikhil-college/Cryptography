def makekey(key):
    alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    fk=''
    for i in key:
        if i not in fk:
            fk+=i        
    for i in fk:
        alpha.remove(i)
    fk=list(fk)+alpha
    return fk

def encode(key,message):
    ecm=''
    for i in message:
        if i == ' ':
            ecm+=' '
        else:
            ecm+=fk[ord(i)-65]
    return ecm

def decode(key,message):
    alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    ecm=''
    for i in message:
        if i == ' ':
            ecm+=' '
        else:
            ecm+=alpha[fk.index(i)]
    return ecm

process=input('E->Encode and D->Decode: ').upper()
key=input('Enter the key: ').upper()
message=input('Enter text: ').upper()
print(key)
fk=makekey(key)
if process == 'E':
    ecm=encode(fk,message)
else:
    ecm=decode(fk,message)
print(ecm)

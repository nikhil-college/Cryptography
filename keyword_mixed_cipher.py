alpha='abcdefghijklmnopqrstuvwxyz'
al=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alcomp=[]
alrep=al.copy()
keymod=''
def encrypt(x,y):
    encrypted=''
    for i in x:
        pos=alpha.rfind(i)
        encrypted=encrypted+y[pos]
    print('The encrypted message is: ',encrypted)
    
def decrypt(x,y):
    decrypted=''
    for i in x:
        pos=y.rfind(i)
        decrypted=decrypted+alpha[pos]
    print('The decrypted message is: ',decrypted)
    
mess=input('Enter the message: ')
key=input('Enter the key: ')
kl=list(key)
keyuni=[]
for i in kl:
    if i not in keyuni:
        keyuni.append(i)
lenkey=len(keyuni)        
for i in keyuni:
    alrep.remove(i)
for i in range(0,len(alrep)):
    keyuni.append(alrep[i])
print(keyuni)
for i in range(0,lenkey):
    for j in range(0,lenkey+1):
        k=(j*lenkey)+i
        if(k<26):
            keymod=keymod+keyuni[k]
        
choice=input('Enter 1 to Encrypt and 2 to Decrypt: ')
if(choice=='1'):
    encrypt(mess,keymod)
else:
    decrypt(mess,keymod)

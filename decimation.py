import fractions
k=int(raw_input("enter the key"))
p=raw_input("Enter the text upper or lower")
g=fractions.gcd(k,26)
def inverse(k1):
    for i in range(1,101):
        temp=(k1*i)%26
        if temp==1:
            return i
def encrypt(p1,k1):
    c1=''
    p1=p1.lower()
    for i in range(0,len(p1)):
        temp=((k1*ord(p1[i]-96))%26)+96
        c1=c1+chr(temp)
    return c1
def decrypt(c1,inv1):
    p1=''
    c1=c1.lower()
    for i in range(0,len(c1)):
        temp=((inv1*(ord(c1[i])-96))%26)+96
        p1+=chr(temp)
    return p1

if g==1:
    print 'encrypt 1 or decrypt 2'
else:
    print 'Invalid Key'
              

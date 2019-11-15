def gcd(x,y):
    if y!=0:
        return gcd(y,x%y)
    else:
        return x

key = int(input("Enter the key for decimation cipher: "))
ceaser_key=int(input("Enter the key for ceaser cipher: "))

if gcd(key,26)==1:
    plain=input("Enter plain text: ")
    
    cipher=""
    for i in plain:
        if i==" ":
            cipher=cipher+" "
        else:
            cipher=cipher+chr((((ord(i)-97)*key+ceaser_key)%26)+97)
    
    print(cipher)
    dec=""
    ikey=0
    for i in range(26):
        if(key*i)%26==1:
            ikey=i
            break
    print("inverse key: ",ikey)

    for j in cipher:
        if j==" ":
            dec=dec+" "
        else:
            dec=dec+chr((((ord(j)-97)-ceaser_key)*ikey%26)+97)
    print(dec)
else:
    print("invalid key")
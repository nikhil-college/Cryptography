def which(num):
    len1=len(num)
    if len1==10:
        if 'x' in num:
            find10(num)
        else:
            check10(num)
    elif len1==13:
        if 'x' in num:
            find13(num)
        else:
            check13(num)
    else:
        print('invalid length of ISBN number')

def check10(num):
    sum=0
    for i in range(10):
        sum+=int(num[i])*(10-i)
    if sum%11==0:
        print('Valid 10-digit ISBN number')
    else:
        print('Invalid 10-digit ISBN number')

def check13(num):
    sum=0
    for i in range(13):
        if i%2==0:
            sum+=int(num[i])
        else:
            sum+=int(num[i])*3
    if sum%10==0:
        print('Valid 13-digit ISBN number')
    else:
        print('Invalid 13-digit ISBN number')

def find10(num):
    pos=num.find('x')
    s=0;pn=[];cval=0
    for i in range(len(num)):
        if i!=pos:
            s+=int(num[i])*(10-i)
    s=(11-(s%11))%11
    pos=10-pos
    for i in range(10):
        cval=(pos*i)%11
        if cval==s:
            pn.append(i)
    print('The possible values are',set(pn))

def find13(num):
    pos=num.find('x')
    pn=[];s=0
    if pos%2==0:
        step=1
    else:
        step=3
    for i in range(len(num)):
        if i!=pos:
            if i%2==0:
                s+=int(num[i])
            else:
                s+=int(num[i])*3
    s=(10-(s%10))%10
    for i in range(10):
        cval=(pos*i*step)%10
        if cval==s:
            pn.append(i)
    print('The possible values are',set(pn))

num = input('Enter ISBN number')
which(num)

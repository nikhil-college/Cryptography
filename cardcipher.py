##Luhn Number
print('If you dont know a number fill it with an (x)')
x=input("enter the number without spaces")
miss=-1
sum1=0
for i in range(len(x)):
        if x[i]=='x':
            miss=i
        else:
            temp=int(x[i])
            if i%2==0:
                y=(temp*2)%10+(temp*2)//10
                sum1+=y
            elif i%2==1:
                sum1+=temp

if miss==-1:
    if sum1%10==0:
        print('valid card number')
    else:
        print('invalid card number')
else:
    print((10-(sum1%10)),'is the missing number at position',miss)

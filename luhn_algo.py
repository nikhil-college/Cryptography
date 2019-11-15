cred_no=input('Enter the number ');
valid_no=[];
check_no=int(cred_no[len(cred_no)-1]);
for i in range(0,len(cred_no)):
    if i%2==0:
        x=int(cred_no[i])*2;
        if x >=10 :
            y=int(x/10);
            x=x%10;
            temp=x+y;
            x=temp;
        valid_no.append(x);
    else:
        valid_no.append(int(cred_no[i]));
res=sum(valid_no);
if res%10==0:
    print('Valid no ');
else:
    print('Invalid no ');
    temp1=int(res/10)+1;
    temp2=temp1*10;
    new_res=res-check_no;
    newcheck_no=temp2-new_res;
    print('If the last digit was',newcheck_no,'the no would be valid ');

    
    

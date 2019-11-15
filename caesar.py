def encrypt(pt,k):
	pt_value=[]; ct_value=[];
	for i in range(0,len(pt)):
		pt_value.append(ord(pt[i])-65);
		ct_value.append(((pt_value[i]+k)%26));
		ct_value[i]=chr(ct_value[i]+65);
	ct="".join(ct_value);
	return ct;

def decrypt(ct,k):
	pt_value=[]; ct_value=[];
	for i in range(0,len(ct)):
		ct_value.append(ord(ct[i])-65);
		pt_value.append(((ct_value[i]-k)%26));
		pt_value[i]=chr(pt_value[i]+65);
	pt="".join(pt_value);
	return pt;

ans=1;
while ans:
	choice=int(input("enter choice: encrytion-1 decryption-2:"));
	k=int(input("enter the key:"));
	if choice==1:
		pt=input("enter plain text:(in caps)");
		ct=encrypt(pt,k);
		print("cipher text:",ct);
	elif choice==2:
		ct=input("enter cipher text:(in caps)");
		pt=decrypt(ct,k);
		print("plain text:",pt);
	else:
		print("invalid choice");
	ans=int(input("continue?-1/0"));	


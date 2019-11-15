MCD = {  'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.',
         'F':'..-.','G':'--.','H':'....','I':'..',
         'J':'.---','K':'-.-','L':'.-..','M':'--',
         'N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.',
         'S':'...','T':'-','U':'..-','V':'...-','W':'.--',
         'X':'-..-','Y':'-.--','Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----'} 
  
# Function to encrypt the string 
# according to the morse code chart 
def encrypt(message): 
    cipher = '' 
    for letter in message:  
        cipher += MCD[letter] + ' '
  
    return cipher 
  
# Function to decrypt the string 
# from morse to english 
def decrypt(message): 
  
    # extra space added at the end to access the 
    # last morse code 
    message += ' '
  
    decipher = '' 
    citext = '' 
    for letter in message: 
  
        # checks for space 
        if (letter != ' '): 
  
            # counter to keep track of space 
            i = 0
  
            # storing morse code of a single character 
            citext += letter 
  
        # in case of space 
        else: 
            # if i = 1 that indicates a new character 
            i += 1
  
            # if i = 2 that indicates a new word 
            if i == 2 : 
  
                 # adding space to separate words 
                decipher += ' '
            else: 
  
                # accessing the keys using their values (reverse of encryption) 
                decipher += list(MCD.keys())[list(MCD 
                .values()).index(citext)] 
                citext = '' 
  
    return decipher 
def encreturn(): 
    message = input("enter your text")
    result = encrypt(message.upper()) 
    print (result)
    
def decreturn():
    message=input("enter morse code")
    result=decrypt(message)
    print(result)
    

    
y=int(input("enter 1 to encrypt and 2 to decrypt"))
if y==1:
    encreturn()
elif y==2:
    decreturn()
    

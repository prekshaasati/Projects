alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
    message_encode = ''
    for char in text : 
        if char ==' ':
            message_encode+=" "
        elif char not in alphabet : 
            message_encode +=char
        else : 
            index= alphabet.index(char)
            
            print(f"shift {shift}" )
            new_index=index + shift
            new_index %= len(alphabet) # 4%25=4 ( 4%25=0*25+4 ) and 26%25=1 (26%25=1*25+1)
            print(f"new_index {new_index}" )
            print(f"len {len(alphabet)}" )
            # if new_index>=len(alphabet):
            #     new_index%=len(alphabet)
            #     print(f"new_index 1 {new_index}" )
            # print(f"new_index {new_index}" )
            message_encode+=alphabet[new_index]
    print(message_encode)

def decrypt(text,shift):
    message_decode = ''
    for char in text :
        if char ==' ':
            message_encode+=" " 
            index= alphabet.index(char)
        elif char not in alphabet : 
            message_decode +=char
        else : 
            shift%= len(alphabet)
            new_index=index - shift
            message_decode+=alphabet[new_index]
    print(message_decode)

again = True
while again is True : 
    direction= input("Type 'Encode' to Encrypt your message or 'decode' to Decrypt a message\n").lower()
    
    text= input ("Enter youe message\n")
    
    shift= int(input("Enter your shift number"))
    
    if direction=='encode':
        encrypt(text,shift)
    elif direction == 'decode':
        decrypt(text,shift)
    else : 
        print("You have entered wrong input ")    

    go_again = input ("Do you want to continue again : Y/N:").lower()
    print(go_again)

    if go_again =='y':
        again=True
    else : 
        again=False
        print("Thanks for playing , Visit again !")



    



import string

def encrypt():
    message=input("\nType your message:")

    shift_key=int(input("\nType the shift number:"))
    letters_list=list(string.ascii_letters)
    
    encrypted_list=[]
    for i in message:
        if i not in letters_list:
            encrypted_list.append(i)
        else:
            position=letters_list.index(i)
            encrypted_letter=letters_list[(position+shift_key)%46]
            encrypted_list.append(encrypted_letter)
    
    encrypted_word="".join(encrypted_list)
    print(f"Heres the encrypted result:{encrypted_word}")
    cont_inue=input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if cont_inue=="yes":
        mode=input("\nType 'encrypt' for Encrypting, or 'decrypt' for Decrypting:")

        if mode=="encrypt":
            encrypt()
   
        elif mode=="decrypt":
            decrypt()
        else:
            print("Enter a valid mode!!")
        
    else:
        print("Good Bye")





def decrypt():
    message=input("\nType your message:")

    shift_key=int(input("\nType the shift number:"))
    letters_list=list(string.ascii_letters)
    
    decrypted_list=[]
    for i in message:
        if i not in letters_list:
            decrypted_list.append(i)
        else:
            position=letters_list.index(i)
            pos_value=(position-shift_key)%46
            if pos_value>=0:
                decrypted_letter=letters_list[pos_value]
                decrypted_list.append(decrypted_letter)
            else:
                decrypted_letter=letters_list[pos_value+46]
                decrypted_list.append(decrypted_letter)

    
    decrypted_word="".join(decrypted_list)
    print(f"Heres the decrypted result:{decrypted_word}")
    cont_inue=input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if cont_inue=="yes":
        mode=input("\nType 'encrypt' for Encrypting, or 'decrypt' for Decrypting:")

        
        if mode=="encrypt":
            encrypt()
   
        elif mode=="decrypt":
            decrypt()
        else:
            print("Enter a valid mode!!")
        
    else:
        print("Good Bye")

print("Ceaser-Cipher")
print("\n------------")

mode=input("\nType 'encrypt' for Encrypting, or 'decrypt' for Decrypting:")







if mode=="encrypt":
    encrypt()
   
elif mode=="decrypt":
    decrypt()
else:
    print("Enter a valid mode!!")


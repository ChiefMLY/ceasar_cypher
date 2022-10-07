alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',\
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Defining the function Cypher that will take in a text, shift_size and the direction of encryption
def cypher(text, shift_size, cipher_dir):
    final_text = ""
    if cipher_dir == "decode":
        shift_size *= -1
    for char in text:
        '''
This condition checks to see if the char in the text is in the alphabet list, if it is then the character will be
shifted but characters like symbols and numbers that are not in the alphabet list will be retained
        '''
        if char not in alphabet:
            final_text += char
        elif char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_size
            final_text += alphabet[new_position]
    print(f"Here's the {cipher_dir}d result: {final_text}")

#Importing the ascii art that will display at the start of the program
from ceaser_logo import logo
print(logo)

'''
The while loop will make the program repeat as long as it's condition stays True
This will allow the user to use the app multiple times without having to exit and restart the program
'''
repeat = True
while repeat == True:
#this will allow the user to input their text, shift_size and cipher_dir
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
#Calling the cypher funciton
  cypher(text=text, shift_size=shift, cipher_dir=direction)
#Asking the user if they would like ot repeat the program or exit the loop
  rewind = input('Would like to restart the program: ')
  if rewind.lower() == 'no':
    repeat = False
    print('Goodbye!!')

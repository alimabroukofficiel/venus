import string
import random
import os
import colorama
from colorama import Fore 
colorama.init(autoreset=True)
all_chars = list(string.ascii_letters + string.digits + string.punctuation + " " + "\n")
main_key = all_chars.copy()
key = ['/', ']', '"', 'l', 'b', 'E', 'h', 'w', 'L', 'K', 'H', ')', 'Y', 'S', 'W', 'M', '0', 'u', '*', '(', 'r', '4', '\\', 'A', 'x', 
's', '$', 'a', 'V', '_', 'Q', 'R', 'q', 'i', 'k', 'j', 'c', 'n', 'O', '-', 'z', '#', '3', 'C', 'o', '?', ',', '.', '&', '|', '`', 't', 'X', 'f', 'B', 'e', '^', 'D', ' ', 'v', 'm', 'T', '!', ';', ':', 'g', 'N', '%', "'", '5', '<', '6', '[', '{', '=', '8', 'd', 'G', '7', '2', 'y', 'p', 'U', 'P', '~', 'I', '1', 'F', '+', '>', '9', 'J', '@', 'Z', '}' , '\n']
colors = {
     'wornnig': Fore.RED,
     'success' : Fore.GREEN
}


def Encrypt():
    file_name = str(input('[?] Please Enter Path File Name : ')).strip()
    open_file = open(file_name , 'r').read()
    target =  list()
    for letter_file in open_file : 
         target += list(letter_file)
    encypt_text = ''
    for letter in target : 
         index = all_chars.index(letter)
         encypt_text += key[index]
    if not os.path.exists('results') : os.mkdir('results')
    extantion = file_name.split('.')[1]
    with open(f'results/_encypt_.{extantion}' , "w") as encypy_file : 
         encypy_file.write(encypt_text)
         print(colors['success'] +'[+] File Encypted Successfully')
    input('[>] Please Enter Key To Continue ...')


def Descrypt():
    file_name = str(input('[?] Please Enter Path File Name : ')).strip()
    open_file = open(file_name , 'r').read()
    target =  list()
    for letter_file in open_file : 
         target += list(letter_file)
    dencypt_text = ''
    for letter in target : 
         index = key.index(letter)
         dencypt_text += all_chars[index]
    if not os.path.exists('results') : os.mkdir('results')
    extantion = file_name.split('.')[1]
    with open(f'results/_dencypt_.{extantion}' , "w") as encypy_file : 
         encypy_file.write(dencypt_text)
         print( colors['success'] +'[+] File Dencypted Successfully')
    input('[>] Please Enter Key To Continue ...')
    

while True :
     user_input = input('[?] What Do You Wan\'t enc/des : ').strip().lower()
     if user_input == "enc": 
          Encrypt()
          break
     if user_input == "des" : 
          Descrypt()
          break
     else : 
          print('[-] Please Choice enc or des')


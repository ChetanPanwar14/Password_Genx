#defining a function clear
import os 
from os import path, system,name

def clear():
    if (name=="nt") :
        _=system('cls')
    else:
        _=system('clear')

clear()

#displaying title 
import pyfiglet
print(pyfiglet.figlet_format("PASSWORD      GENX"))   
print('\n-----DEVELOPED BY CHETAN PANWAR-----')
def main():   #defining main 
    
    #this is menu feature
    print("\n----------MENU------------")
    print("\n1-GENERATE A PASSWORD")
    print("\n2-SEE SAVED PASSWORD")
    print("\n3-EXIT")

    print("\n--------------------------")

    m=int(input("\nENTER YOUR CHOICE :"))
    
    
    if(m==1): #password generator

        import random
        import array


        MAX_LEN = 12


        DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                                                'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                                                'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                                                'z']

        UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                                'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                                                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                                                'Z']

        SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                        '*', '(', ')', '<']


        COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS


        rand_digit = random.choice(DIGITS)
        rand_upper = random.choice(UPCASE_CHARACTERS)
        rand_lower = random.choice(LOCASE_CHARACTERS)
        rand_symbol = random.choice(SYMBOLS)


        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol



        for x in range(MAX_LEN - 4):
                temp_pass = temp_pass + random.choice(COMBINED_LIST)

                
                temp_pass_list = array.array('u', temp_pass)
                random.shuffle(temp_pass_list)


        password = ""
        for x in temp_pass_list:
                        password = password + x
                        


        print("\nENTER WEBSITE/APP ")
        w=input(":")

        print("\nENTER USERNAME/MAIL/NUMBER OF",w.upper())
        us=input(":")

        n= "USERNAME :" + us
        p= "      PASSWORD :" + password

               

        clear()
        
        
        print("\n",w.upper(),"USERNAME :",us)
        print(" SUGGESTED PASSWORD :",password)
        
        import json

        c=(input("\nDID U USE SUGGESTED PASSWORD ? (Y/n) :"))

        if(c=="y"):
          from json_data import path
          pth = (path.real_path)
          f_pth = (pth +w.upper() + ".json")
          with open( f_pth ,"w+") as f:
           json.dump(n+p, f)
           print("SAVING PASSWORD...........") 
           import time
           time.sleep(2)
           clear()
        
        elif(c=="n"):
                clear()
                main()         
        import time
        time.sleep(2)
        main()
    
    if (m==2):
        import os
        from json_data import path
        listpath = path.real_path
        for f in os.listdir(listpath):
            if f.endswith('.json'):
                 print("\n",f)
        web = input('\n\nSHOW PASSWORD OF :')
        web = web.upper()+'.json'
        clear()
        print('OPENING',web,'FILE.....')
        import time
        time.sleep(3)
        clear()
        import os
        os.chdir(listpath)
        os.system('more '+web)
        input('\nPRESS ANY KEY TO CONTINUE !!')
        clear()
        main()

    

    
    
    if (m==3):
        clear()
        print("EXITING.....")
        exit()    
main()

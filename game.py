import random

computre_number=random.randint(0,25)
tedadhads = 0
while True:
    user_number=int(input())
    tedadhads = tedadhads + 1
    
    if  user_number == computre_number:
        print("TABRIK😊")
        break

    elif user_number< computre_number :
        print("ADAD BALATARI ENTEKHAB KON ➕")

    elif  user_number> computre_number:
         print("ADAD PAEENTAR ENTEKHAB KON ➖ ")
    
print("BAZI TAMOME ", tedadhads,)  
 
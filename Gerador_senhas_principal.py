from gerador_6 import *
from gerador_8 import *
from gerador_9 import *
from gerador_10 import *
import os

os.system("clear")
print("........................ Code")
print(":  Generator Password  : By Caio")
print(":......................: Entreteniment")

while True:
    
    print(".........................................")
    usuario = input(">>tamanho da senha: 6/8/9/10/: ")

    if usuario == "6":
        Codigo_6caracteres()

    elif usuario == "8":
        Codigo_8caracteres()

    elif usuario == "9":
        Codigo_9caracteres()

    elif usuario == "10":
        Codigo_10caracteres()

    else:
        print("error in keyboard")
        break

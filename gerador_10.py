import random

x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 't', 'u', 'v', 's', 'x', 'y', 'w', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'E', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'T', 'U', 'V', 'S', 'X', 'Y', 'W', 'Z']
y = ['!', '@', '#', '$', '%', '&', '*', '+', '-', ':', '/', '>', '<', '=']

def Codigo_10caracteres():

    a = random.choice(x)
    b = random.choice(x)
    c = random.choice(x)
    d = random.choice(x)
    e = random.choice(x)
    f = random.choice(x)
    g = random.choice(x)
    h = random.choice(x)
    i = random.choice(x)
    j = random.choice(x)
    k = random.choice(y)
    l = random.choice(y)

    print(f"[+]senha:\t\t{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}")
    print(f"[+]senha:\t\t{a}{b}{c}{k}{e}{f}{l}{h}{i}{j}\n")

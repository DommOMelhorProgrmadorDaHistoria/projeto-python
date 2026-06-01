import random
import string

# criar sistema original de respostas a senha
input ("digite uma senha inicial")
senha = ""
caracteres = string.ascii_letters
números = string.digits
tamanho = random.random
adicionar_caractere = string.punctuation (input (f"você deseja adicionar um caractere especial?:"))
s = ("sim")
n = ("não")
if adicionar_caractere == (s):
    input ("qual caractere você deseja adicionar?")
    if adicionar_caractere == (n):
        print ("prossiga com a senha")




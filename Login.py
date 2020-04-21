# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:09:51 2020

@author: Nagashi
"""


import hashlib

def arquivos(nome):
    try:
        nome=nome+".txt"
        arquivo=open(nome,"r")
    except FileNotFoundError:
        arquivo=open(nome,"w")
        print("Arquivo {} foi criado".format(nome))

def logar(usuario,senha,on):
    global dados
    try:
        dados=open("database.qz","r")
        with open("database.qz","r") as dados:
            for linha in dados:
                if(linha.find(usuario)>-1 and linha.find(senha.hexdigest())):
                    print("Seja bem-vindx, {}!".format(usuario))
                    on=True
                    
                else:
                    print("Senha ou usuário inválidos.")
                    
                   
    except FileNotFoundError:
        dados=open("database.qz","w")
        dados.writelines(usuario)
        dados.writelines(" ")
        dados.writelines(senha.hexdigest())
        print("O arquivo foi criado contendo as informações.")
        on=True
        return True

def cifrar(senha):
    senha=hashlib.sha256()
    senha.update(senh.encode("utf-8"))
    return senha


usuario=input("Digite seu usuário: ")
senh=input("Digite sua senha: ")

while len(str(senh))<8:
    print("Sua senha deve conter mais que 7 dígitos")
    senh=input("Digite sua senha novamente: ")
on=False
senha=cifrar(senh)
logar(usuario,senha,on)

print(on)
        
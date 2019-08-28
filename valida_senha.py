import re

def valida_senha(senha):
    #----Caso 1---
    # Caso a senha seja curta, abaixo ou igual a 5, porém contenha caracteres maiusculos e minusculo e além disso apresente 
    # caracteres especiais ela pode ser considerada uma senha média.
    # de contrario sera considerada uma senha fraca.

    #----Caso 2----
    # Caso a senha apresente tamanho de 6 a 8 caracteres e possua letras maiuscula como minusculas e números, ela sera media,
    # caso ela nao possua uma das condiçoes, por exemplo, ela sera fraca, apesar do seu tamanho.

    #----Caso 3----
    # Para a senhar ser forte ela precisa conter um tamanho maior que 8 caracteres e além disso necessita apresentar letras
    # maiusculas e minusculas, tal como conter caracteres especiais e numeros, caso nao apresente tal condiçoes porem seja maior
    # que 8 caracteres, sera considerada uma senha media.

    nivel = -1
    

    if len(senha) == 0:
        nivel == -1
        print(nivel)
        return nivel

    if len(senha) <= 5:
        if re.findall(r"[A-Za-z]", senha) and re.findall(r"[@#$%^&]", senha):
            nivel += 2
            print(nivel)
        else:
            nivel += 1
            print(nivel)
        return nivel
    
    if len(senha) <= 8:
        if re.findall(r"[A-Za-z]", senha) and re.findall(r"[0-9]", senha):
            nivel += 2
            print(nivel)
        else:
            nivel += 1
            print(nivel)
        return nivel

    if len(senha) > 8:
        if re.findall(r"[A-Za-z]", senha) and re.findall(r"[0-9]", senha) and re.findall(r"[@#$%^&]", senha):
            nivel += 3
            print(nivel)
        else:
            nivel += 2
            print(nivel)
        return nivel


if __name__ == "__main__":
    print('********* \n\
Níveis de senha: \n\
0 = fraca \n\
1 = media \n\
2 = forte \n\
**********')
    digite = input('Digite sua senha aqui: ')
    valida_senha(digite)
palavra = input("Digite a frase ")

def codificar(frase):
    novafrase = ""
    for letra in frase:
        if letra == " ":  # verifica a existencia de espaço para não substituir a ultima letra
            novafrase += letra
        else:
            novafrase += 'p' + letra
    return novafrase

def decodificar(frase):
    str = ""
    lista = list(frase)
    if lista[1] != "p":
        for i in range(len(lista) - 1):
            lista[0] = ""
            if lista[i] == "p" and lista[i+1] != "p":
                lista[i] = ""
        return str.join(lista).replace("pp", "p")
    else: # cai nesse else apenas se a palavra digitada pelo usuario iniciar com p
        for i in range(len(lista) - 1):
            if i == 0:
                lista[0] = ""
                lista[1] = "p"
            if i >= 2:
                if lista[i] == "p" and lista[i+1] != "p":
                    lista[i] = ""
    return str.join(lista).replace("pp", "p")

codifResult = (codificar(palavra))
print(codifResult)

decodifResult = (decodificar(codifResult))
print(decodifResult)
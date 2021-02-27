# Luiz Otávio, Izadora,Wahuane, Paula, Beatriz
def codificar(frase, mensagem = ''):
    novafrase = ""
    for letra in frase:
        if letra == " ":  # verifica a existencia de espaço para não substituir a ultima letra
            novafrase += letra
        else:
            novafrase += 'p' + letra
    return print(mensagem + novafrase)


def decodificar(frase, mensagem = ''):
    str = ""
    lista = list(frase)
    if lista[1] != "p":
        for i in range(len(lista) - 1):
            lista[0] = ""
            if lista[i] == "p" and lista[i + 1] != "p":
                lista[i] = ""
        return print(mensagem + str.join(lista).replace("pp", "p"))

    else:  # cai nesse else apenas se a palavra digitada pelo usuario iniciar com p
        for i in range(len(lista) - 1):
            if i == 0:
                lista[0] = ""
                lista[1] = "p"
            if i >= 2:
                if lista[i] == "p" and lista[i + 1] != "p":
                    lista[i] = ""
    return print(mensagem + str.join(lista).replace("pp", "p"))


palavra = input("Digite a frase para codificar, caso queira somente decodificar tecle enter: ")

codificar(palavra, "Palavra codificada: ")

palavra = input("Digite a frase para decodificar: ")

decodificar(palavra, "Frase decodificada: ")
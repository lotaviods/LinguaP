from time import sleep


# Luiz Otávio, Izadora,Wahuane, Paula, Beatriz

# formatação
def decodificar_msg(string: str):
    for i in range(30):
        print('\033[35m•\033[m', end='', flush=True)
        sleep(0.09)

    print('\n', f'\033[36m{string.center(30)}\033[m')

    for i in range(30):
        print('\033[35m•\033[m', end='', flush=True)
        sleep(0.09)


# código
msg = str(input(' Informe sua mensagem codificada: ')) \
    .replace('ppppp', '##') \
    .replace('ppp', '#') \
    .replace('p', '') \
    .replace('#', 'p')

decodificar_msg(msg)

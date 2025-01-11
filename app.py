import os

mensagens = []

nome = input('Digite seu nome: ')

while True:
    # Limpando terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], '-', m['texto'])

    print('_'*20)

    # Obtendo texto
    texto = input('Mensagem: ')
    if texto == 'fim':
        break

    # Adicionando mensagens na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })
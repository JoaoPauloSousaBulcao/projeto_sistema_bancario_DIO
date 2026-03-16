saldo = float(input('Digite o saldo onicial da conta: R$'))
extrato = []

def deposito():
    global saldo
    deposito = float(input('Digite o valor do deposito: '))    
    saldo += deposito
    addExtract({'tipo': 'Deposito', 'valor':deposito})
    print(f'Deposito realizado, saldo atual é R$ {saldo:.2f}')

def saque():
    global saldo
    saque = float(input('Digite o valor do saque: '))
    if saque > saldo : 
        print('Não foi possivel realizar o saque pois o saldo em conta é menor.')

    else:
        saldo -= saque
        addExtract({'tipo': 'Saque', 'valor':saque})
        print(f'Saque realizado, saldo atual é R$ {saldo:.2f}')
        return saldo

def addExtract(object):
    extrato.append(object)

def printExtract(extrato):
    print('Transações realizadas na sua conta: \n')
    for elemento in extrato:
        print(f'{elemento['tipo']}: R$ {elemento['valor']:.2f}')
    print(f'Saldo: R${saldo:.2f}\n \n')

while True: 
    print('1-Depositar  \n2-Sacar \n3-Extrato \n4-Saldo \n5-Sair')
    escolha = int(input('Digite qual operação deseja realizar: '))


    match escolha:
        case 1:
            deposito()

        case 2: 
            saque()

        case 3:
            printExtract(extrato)

        
        case 4:
            print(f'Seu saldo é R${saldo:.2f}')

        case 5:
            print('Sessão finalizada')
            break

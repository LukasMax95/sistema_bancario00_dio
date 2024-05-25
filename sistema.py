class Banco:
    menu = '''

[d] depositar
[e] extrato
[s] sacar
[q] sair

'''
    usuario = ""
    saldo = 0
    dia = 1
    limite_saques = 3
    estrato = []
    def __init__(self, usuario):
        self.usuario = usuario
    
    def novodia(self):
         self.limite_saques = 3
         self.dia += 1

    def valorSaque(self):
        r = " por falta de saldo" if self.saldo < 500 else ", pois o valor ultrapassa o limite de $500"
        while(1):#validação do valor a ser sacado
            try:
                    print("digite um valor!")
                    valor = int(input())
            except:
                    print("digite um valor numérico, sem os zeros")
            if(valor <= 0):
                print(f"Não é possivel retirar esse valores negativos!")
                print("Digite outro valor")
            elif(valor > self.saldo) or (valor > 500):
                print(f"Não é possivel retirar esse valor{r}!")
                print("Digite outro valor")
            else:
                 break
        return valor

    def on(self):#comando cmd do banco
        while(True):
            print("Entrando no Banco!")
            print(f"saldo atual: ${self.saldo}")
            print(f"dia: {self.dia}")
            print(self.menu)
            c = input()
            if c == "d":
                valor = self.valorDeposito()
                self.depositar(valor)
            elif c == "s":
                if(self.limite_saques == 0):
                     print("Não foi possível a operação.\n"
                           + "Limite de Saques por Dia atingido")
                elif(self.saldo == 0):
                    print("Não foi possível a operação.\n"
                          + "Saldo Zerado")
                else:
                    valor = self.valorSaque()
                    self.retirar(valor)
            elif c == "e":
                self.extrato()
            elif c == "q":
                print("Saindo do Banco!")
                break
            else:
                print("Comando Inválido!")

    def valorDeposito(self):
        while(1):#validação do valor a ser depositado
            try:
                    print("digite um valor!")
                    valor = int(input())
            except:
                    print("digite um valor numérico, sem os zeros")
            if(valor <= 0):
                print(f"Não é possivel adicionar valores negativos!")
                print("Digite outro valor")
            else:
                 break
        return valor

    def armazenar(self, valor: int, tipo: str): #armazena cada operação em uma lista na forma de um dict
         self.estrato.append({
            "tipo": tipo,
            "valor": valor,
            "dia": self.dia
         })

    def depositar(self, valor):
        print(f"depositando {valor}")
        self.saldo += valor
        self.armazenar(valor, "Depósito")
    
    def retirar(self, valor):
        print(f"retirando {valor}")
        self.saldo -= valor
        self.armazenar(valor, "Saque")
        self.limite_saques -= 1

    
    def extrato(self):
        print(f"Usuário: {self.usuario}\nSaldo: ${self.saldo}")
        #print(self.estrato)
        for operacao in self.estrato:
             print(f'''
                Tipo: {operacao["tipo"]}
                Valor: {operacao["valor"]}
                Dia: {operacao["dia"]}
                '''
            )


def main():
     while(True):
        print("a pra acessar, q pra sair")
        c1 = input()
        if c1 == "a":#pagina do banco
            print("Entrando")
            print("Digite seu nome")#criação de conta
            nome = input()
            conta = Banco(nome)
            while(True):#acesso ao banco
                print("a pra acessar, u para atualizar, q pra sair")
                c2 = input()
                if c2 == "a":
                    conta.on()
                elif c2 == "u":
                    conta.novodia()
                elif c2 == "q":
                    print("Saindo")
                    c1 = "q"
                    break
                else:
                    print("Comando inválido!")
        if c1 == "q":
            break
        else:
            print("Comando Inválido!")


main()
import random as rnd
class Banco:
    menu = '''

[d] depositar
[e] extrato
[s] sacar
[q] sair

'''
    usuarios = []
    usuario = {}
    novousuario = 0
    cpfs_cadastrados = []
    f1 = 0
    f2 = 0
    dia = 1
    def __init__(self):
        print("Banco Criado")

    def nova_conta(self, usuario):
        novo = {}
        novo["nome"] = usuario
        print("Digite seu CPF (Só numeros):\n[c] cancelar")
        cpf = input()
        
        if cpf != "c":
            while(True):
                if cpf in self.cpfs_cadastrados:
                    print("CPF já existe: Digite outro CPF (Só numeros):")
                    cpf = input()
                else:
                    break
            self.cpfs_cadastrados.append(cpf)
            novo["cpf"] = cpf
            novo["agencia"] = rnd.randrange(100, 1500)
            novo["conta"] = self.novousuario
            self.novousuario += 1
            novo["limite saques"] = 3
            novo["estrato"] = []
            novo["saldo"] = 0
            self.usuarios.append(novo)
            self.usuario = novo
        else:
            novo["cpf"] = "X"
            novo["agencia"] = rnd.randrange(100, 1500)
            novo["conta"] = self.novousuario
            self.novousuario += 1
            novo["limite saques"] = 3
            novo["estrato"] = []
            novo["saldo"] = 0
            self.usuarios.append(novo)
            self.usuario = novo
        print(novo)

    def reinit_counters(self):
        self.f1 = 0
        self.f2 = 0
    

    def confirmaUsuario(self):
        while(True):
            print(self.usuario)
            print("Essa é a sua conta? (y/n)")
            r = input()
            if r == "y":
                return True
            elif r == "n":
                return False
            else:
                print("Resposta Inválida!")
        
    def findByName(self, name):
        for usuario in self.usuarios:
            if (usuario["nome"] == name) and (usuario["cpf"] == "X"):
                self.usuario = usuario
                if(self.confirmaUsuario()):
                    return True
            self.f1 += 1
        else:
            return False

    def findByCPF(self, cpf):
        for usuario in self.usuarios:
            if usuario["cpf"] == cpf:
                self.usuario = usuario
                if(self.confirmaUsuario()):
                    return True
            self.f2 += 1
        else:
            return False

    def completarCadastro(self, name):
        if self.findByName(name):
            print("Digite seu CPF (Só numeros):\n[c] cancelar")
            cpf = input()
            if cpf != "c":
                self.cpfs_cadastrados.append(cpf)
                self.usuario["cpf"] = cpf
        else:
            print("Usuário não existe")
    

    def completarCadastro(self):
        print("Digite seu CPF (Só numeros):\n[c] cancelar")
        cpf = input()
        if cpf != "c":
            self.cpfs_cadastrados.append(cpf)
    
    def novodia(self):
         for usuario in self.usuarios:
             usuario["limite saques"] = 3
         self.dia += 1

    def valorSaque(self):
        r = " por falta de saldo" if self.usuario["saldo"] < 500 else ", pois o valor ultrapassa o limite de $500"
        while(1):#validação do valor a ser sacado
            try:
                    print("digite um valor!")
                    valor = int(input())
            except:
                    print("digite um valor numérico, sem os zeros")
            if(valor <= 0):
                print(f"Não é possivel retirar esse valores negativos!")
                print("Digite outro valor")
            elif(valor > self.usuario["saldo"]) or (valor > 500):
                print(f"Não é possivel retirar esse valor{r}!")
                print("Digite outro valor")
            else:
                 break
        return valor

    def on(self, cpf):#comando cmd do banco
        flag = self.findByCPF(cpf)
        if flag:
            if((self.usuario["cpf"] != 0) or (self.usuario["cpf"] != "X")):
                while(True):
                    print("Entrando no Banco!")
                    print(f"saldo atual: ${self.usuario["saldo"]}")
                    print(f"dia: {self.dia}")
                    print(self.menu)
                    c = input()
                    if c == "d":
                        valor = self.valorDeposito()
                        self.depositar(valor)
                    elif c == "s":
                        if(self.usuario["limite saques"] == 0):
                            print("Não foi possível a operação.\n"
                                + "Limite de Saques por Dia atingido")
                        elif(self.usuario["saldo"] == 0):
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
            else:
                while(True):
                    print("Completar Cadastro? (y/n)")
                    resp = input()
                    if resp == "y":
                        self.completarCadastro()
                        self.on()
                        break
                    elif resp == "n":
                        print("Processo Cancelado!")
                        break
                    else:
                        print("Comando Inválido!")
        else:
            print("CPF Inválido ou não existente.")

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
         self.usuario["estrato"].append({
            "tipo": tipo,
            "valor": valor,
            "dia": self.dia
         })

    def depositar(self, valor):
        print(f"depositando {valor}")
        self.usuario["saldo"] += valor
        self.armazenar(valor, "Depósito")
    
    def retirar(self, valor):
        print(f"retirando {valor}")
        self.usuario["saldo"] -= valor
        self.armazenar(valor, "Saque")
        self.usuario["limite saques"] -= 1

    
    def extrato(self):
        print(f"Usuário: {self.usuario["nome"]}\n"
              + f"Saldo: ${self.usuario["saldo"]}"
              + f"Conta: {self.usuario["conta"]}"
              + f"Agencia: {self.usuario["agencia"]}"
        )
        #print(self.estrato)
        for operacao in self.usuario["estrato"]:
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
            
            conta = Banco()
            while(True):#acesso ao banco
                print('''
                    [a] pra acessar
                    [c] pra criar conta
                    [l] listar contas
                    [u] para atualizar
                    [q] pra sair
                ''')
                c2 = input()
                if c2 == "a":
                    print("Digite seu CPF (Só numeros):\n[c] cancelar")
                    cpf = input()
                    conta.on(cpf)
                elif c2 == "c":
                    print("Digite seu nome")#criação de conta
                    nome = input()
                    conta.nova_conta(nome)
                elif c2 == "u":
                    conta.novodia()
                elif c2 == "l":
                    for usuario in conta.usuarios:
                        print(usuario)
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
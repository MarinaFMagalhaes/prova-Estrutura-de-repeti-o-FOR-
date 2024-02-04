class CelularSmartphone:
    def __init__(self) -> None:
        self.senha = None
        self.inicializado = False
        self.tentativas = 3

    def cadastrar_senha(self, senha):
        self.senha = senha
        print("Cadastro realizado!")

    def inicializar_celular(self, senha_digitada):
        if not self.inicializado:
            if senha_digitada == self.senha:
                self.inicializado = True
                print("Bem-vindo!")
            else:
                self.tentativas -= 1
                print(f"Senha incorreta. Você tem {self.tentativas} tentativas restantes.")
                
                if self.tentativas == 0:
                    print("Limite de tentativas atingido. Celular bloqueado.")
        else:
            print("Celular inicializado.")

meu_celular = CelularSmartphone()

senha_cadastro = input("Digite a senha para cadastro: ")
meu_celular.cadastrar_senha(senha_cadastro)

for x in range(3):
    senha_digitada = input("Digite a senha para inicializar: ")
    meu_celular.inicializar_celular(senha_digitada)
    
    if meu_celular.inicializado or meu_celular.tentativas == 0:
        break
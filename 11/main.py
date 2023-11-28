import os

class App:
    @staticmethod
    def bem_vindo():
        print('---------------- Bem vindo ao Programa ----------------', end='\n\n')

    def obter_numero_valido(self):
        while True:
            try:
                valor = input('Digite um número: ')
                numero = int(valor)
            except ValueError as e:
                print(f'\n {valor} é um número inválido', end='\n\n')
                continue
            else:
                return numero

    def exibir_numero(self, numero):
        print(f'\nO número que você digitou é {numero}', end='\n\n')

    @staticmethod
    def final():
        print('---------------- Final do Programa ----------------', end='\n\n')

if __name__ == '__main__':
    os.system('cls')

    app = App()

    App.bem_vindo()

    numero = app.obter_numero_valido()

    app.exibir_numero(numero)


    App.final()
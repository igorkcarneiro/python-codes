class Empregado: #Definição da classe e seu nome (Empregado). Não se esqueça de colocar os dois pontos (“:”) após essa nomenclatura.
    'Classe base para empregados' #Breve descrição da classe. Observe que NÃO é um comentário, e sim uma string que faz parte da documentação da classe.
    contador = 0 #Criação de uma variável de classe – chamada, aqui, de contador. A definição de variáveis é feita conforme as regras da linguagem. Lembre-se de que variável de classe é diferente de variável de instância.

    def __init__ (self, nome, salario): #5-8 Definição do método construtor. Observe seu nome específico: “__init__()”. Quando a Python encontra esse método, trata-o como construtor da classe. Dentro dele, definimos as variáveis de instância da classe.
        self.nome = nome
        self.salario = salario
        Empregado.contador += 1

    def mostra_contador (self): #10-13 Os outros métodos da classe são criados como funções normais, com exceção de que o primeiro argumento para cada método é o self. A Python coloca o self na lista para você, mas ele não precisa ser referenciado quando for chamar os métodos.
        print ("Número de empregados: %d" % Empregado.contador)

    def mostra_empregado (self):
        print ("Nome: ", self.nome, ", Salário: ", self.salario)

emp1 = Empregado("Fabiano",1000)
emp2 = Empregado("João Neves", 1500)

emp1.mostra_empregado()
emp2.mostra_empregado()

emp1.idade = 44
print("Nome: ",emp1.nome," - Salário: ",emp1.salario," - Idade: ",emp1.idade)
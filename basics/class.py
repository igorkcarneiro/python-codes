class estudos: #Definição da classe e seu nome (estudos). Não se esqueça de colocar os dois pontos (“:”) após essa nomenclatura.
    'Classe base para estudos' #Breve descrição da classe. Observe que NÃO é um comentário, e sim uma string que faz parte da documentação da classe.
    contador = 0 #Criação de uma variável de classe – chamada, aqui, de contador. A definição de variáveis é feita conforme as regras da linguagem. Lembre-se de que variável de classe é diferente de variável de instância.

    def __init__ (self, faculdade, curso): #5-8 Definição do método construtor. Observe seu nome específico: “__init__()”. Quando a Python encontra esse método, trata-o como construtor da classe. Dentro dele, definimos as variáveis de instância da classe.
        self.faculdade = faculdade
        self.curso = curso
        estudos.contador += 1

    def mostra_contador (self): #10-13 Os outros métodos da classe são criados como funções normais, com exceção de que o primeiro argumento para cada método é o self. A Python coloca o self na lista para você, mas ele não precisa ser referenciado quando for chamar os métodos.
        print ("Número de estudos: %d" % estudos.contador)

    def mostra_estudos (self):
        print ("faculdade: ", self.faculdade, " Curso: ", self.curso)

emp1 = estudos("Estácio","Defesa Cibernética")
emp2 = estudos("École 42 Rio", "Engenharia de Software")

emp1.mostra_estudos()
emp2.mostra_estudos()

emp1.tipo = "tecnólogo"
print("\nfaculdade: ",emp1.faculdade," Curso: ",emp1.curso," tipo: ",emp1.tipo)
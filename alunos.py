class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando alguns objetos Aluno
aluno1 = Aluno("Albert Einstein", 20)
aluno2 = Aluno("Leonardo da Vinci", 22)
aluno3 = Aluno("Isaac Newton", 21)
aluno4 = Aluno("Stephen Hawking", 35)
aluno5 = Aluno("Marie Curie", 42)
aluno6 = Aluno("William Shakespeare", 18)
aluno7 = Aluno("Galileu Galilei", 27)
aluno8 = Aluno("Nicolau Copérnico", 23)
aluno9 = Aluno("Michelangelo", 25)
aluno10 = Aluno("Cleópatra", 30)
aluno11 = Aluno("John Nash", 31)
aluno12 = Aluno("Alan Turing", 40)

# Criando uma lista de objetos Aluno
alunos = [aluno1, aluno2, aluno3, aluno4, aluno5, aluno6, aluno7, aluno8, aluno9, aluno10, aluno11, aluno12]

# Ordena a lista de objetos 'alunos' em ordem alfabética pelo atributo 'nome' de cada objeto.
# A função 'lambda x: x.nome' extrai o atributo 'nome' de cada objeto 'aluno' para ser usado como chave de ordenação.
alunos_ordenados = sorted(alunos, key=lambda x: x.nome)

# Exibe apresentação
print("\nAlunos e suas idades\n")
# Exibindo a lista ordenada
for aluno in alunos_ordenados:
    print(f"Nome: {aluno.nome}, Idade: {aluno.idade}")

# Projeto de Automatização de Notas Escolares
# Agenda 10 - Desenvolvimento de Sistemas I
# Autor: Camila Ferreira Santos
# Turma: TMD

# Declaração de variáveis
alunosAprovados = 0
alunosReprovados = 0


# Função para calcular a média e verificar a aprovação do aluno
def calcularMedia(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return media

def verificarAprovacao(mediaAluno):
    global alunosAprovados, alunosReprovados

    if mediaAluno >= 6.0:
        alunosAprovados += 1
        return "Aprovado"
    else:
        alunosReprovados += 1
        return "Reprovado"


# Entrada de dados
qtdeAlunos = int(input("Digite a quantidade de alunos da turma: "))


# Coleta de dados dos alunos
for x in range(qtdeAlunos):
    print("\n------------")
    print(f"Aluno {x + 1}")
    print("------------")

    nomeAluno = input("Digite o nome do aluno: ")
    notas = []

    # Coleta e validação as quatro notas bimestrais do aluno
    for i in range(4):
        while True:
            try:
                nota = float(input(f"Digite a nota do {i + 1}º Bimestre: "))

                if nota < 0 or nota > 10:
                    print("Nota inválida, digite novamente.")
                else:
                    notas.append(nota)
                    break

            except ValueError:
                print("Valor inválido, digite uma nota numérica.")

    # Chamada da função para calcular a média e verificar a situação do aluno
    mediaAluno = calcularMedia(notas[0], notas[1], notas[2], notas[3])

    situacaoAluno = verificarAprovacao(mediaAluno)

    print(f"\nMédia: {mediaAluno:.2f}")
    print(f"Situação: {situacaoAluno}")


# Relatório final da turma
print("\n----------------------------------")
print("Relatório de Desempenho da Turma")
print("----------------------------------")
print(f"Total de alunos aprovados: {alunosAprovados}")
print(f"Total de alunos reprovados: {alunosReprovados}")
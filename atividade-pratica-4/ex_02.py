# 2 - Criar um código que registre as notas de alunos e calcular a média da turma.

notas = []

qtd_alunos = int(input("Quantos alunos há na turma? "))

for i in range(1, qtd_alunos + 1):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    notas.append(nota)

media_turma = sum(notas) / len(notas)

print("\nNotas registradas:")
for i, nota in enumerate(notas, start=1):
    print(f"Aluno {i}: {nota:.2f}")

print(f"\nMédia da turma: {media_turma:.2f}")

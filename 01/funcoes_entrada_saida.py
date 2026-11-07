# Função input sempre retorna uma string,
# então precisamos converter para o tipo desejado

idade = int(input("Digite sua idade: "))
idade = (int(idade))
print(idade)

nome = "Guilherme"
sobrenome = "Carvalho"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(sobrenome, nome, sep=", ")

print(1+10)
print(1.5)
print(True)
print("Olá, Bem-vindo ao curso de Python!")

int()
float()
bool()
str()

age = 25
name = "Breno"

age, name = 25, "Breno"

print("Meu nome é {name} e tenho {age} anos.".format(name=name, age=age))

# existe uma convençao para usarmos as constantes
# em letras maiúsculas
# constantes são valores que não mudam durante a execução do programa

ABS_PATH = "/home/breno/Documentos/Projetos/Python"
DEBUG = True
STATES = ["SP", "RJ", "MG", "ES"]
AMOUNT = 30.2

# BOAS PRÁTICAS DE NOMENCLATURA
# Variáveis e funções: minúsculas e underscore
# SNAKE_CASE: nome_da_variavel, nome_da_funcao()
# Classes: PascalCase
# Escolher nomes significativos para variáveis, funções e classes
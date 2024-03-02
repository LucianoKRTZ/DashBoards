# definindo funcoes em variaveis
def somaUm(num):
    return num+1
f1 = somaUm
f1(2)

# definindo funcoes em funcoes

def soma_Um(num):
    def addNum(num):
        return num+1
    return addNum(num)

soma_Um(4)

# definindo funcoes como argumento

def somaUm(num):
    return num+1

def functionCall(function):
    numAdd = 5
    return function(numAdd)

functionCall(somaUm)

# funcao retornando outra funcao

def funcOla():
    def digaOI():
        return 'HI'
    return digaOI

hello = funcOla()
hello()

# exemplo de uso para deixar o texto maiusculo

def decoradorMaiusculo(function):
    def wrapper():
        func = function()
        criaMaiusculo = func.upper()
        return criaMaiusculo
    return wrapper
    

def digaOI():
    return 'hello there'

funcDecorada = decoradorMaiusculo(digaOI)
funcDecorada()
# ou

def decoradorMaiusculo(function):
    def wrapper():
        func = function()
        criaMaiusculo = func.upper()
        return criaMaiusculo
    return wrapper
    
@decoradorMaiusculo # faz o mesmo que ocorreu em cima
def digaOI():
    return 'hello there'

digaOI()

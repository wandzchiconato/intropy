# 1 - Imports - Bibliotecas

# 2 - Classe

# 3 Metodos e funções
# Metodo não tem retorno
# Função tem retorno

# def = definition definição


def print_hi(name):

    print(f'Hello {name}') #f' format concatena
    print('oi, ' + name)

def area_do_retangulo(largura, comprimento):
    return largura * comprimento

def area_do_quadrado(lado):
    return lado ** 2

def area_do_triangulo(largura, comprimento):
    return largura * comprimento /2

def contatagem_progressiva (fim):
    for numero in range(fim): #repetir o bloco de zero até o fim
        print(numero)       #exibir o numero

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        #contador = numero + 1
        #print(f'{contador} - {nome}')

       if numero < 9 :
           print(f'00{numero+ 1} - {nome}')
       elif numero <99:
           print(f'0{numero + 1} - {nome}')
       else:
        print (numero + 1, '-', nome)


def brincar_de_plin(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print ('PLIM!')
        else:
            print('{:0>3}'.format(numero))


# estrutura de identificação  / execução do script

if __name__ == '__main__':
    print_hi('World')

# chamar a função de calculo da area do retangulo

    resultado = area_do_retangulo(7,9)
    print(f' A area do retangulo é de  {resultado} M²')


# chamar a função de calculo do quadrado

    resultado = area_do_quadrado(22)
    print(f' A area do quadrado é de {resultado} m²')

# chamar a função de calculo do triangulo

    resultado = area_do_triangulo(5,7)
    print(f' A area do triangulo é de {resultado} m2')

# Executar uma contagem progressiva
contatagem_progressiva(2)

# Exibir o nome do candidato varias vezes
apoiar_candidato('Wandz', 100)


#Funçao brincar de plin
brincar_de_plin(100)
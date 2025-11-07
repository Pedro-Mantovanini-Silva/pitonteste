#print("Hello World!") #Serve para imprimir mensagens no terminal
#input("Qual seu nome?: ") #Recebe as entradas do usuario
#i = 1 #Variaveis inteiras 
#i = 'Olá' #Variaveis em string

#Maneiras de formatar um texto
#nome_usuario = input('Digite seu nome: ')
#print("Olá " + nome_usuario)
#print(f"Olá {nome_usuario}")
#print("Olá {}".format(nome_usuario)

#nomi_user = input('qual tu nome :')
#
#idadi_user = input('qual tu idad :')
#
#print(f"Hola {nomi_user} tu tens {idadi_user}")

#Operadores lógicos no python
#print(1+1)
#print(1-1)
#print(4//2) #Ao usar 2 barras(//) tiramos as casas decimais. Não deve ser usado em programs que precisam de uma resposta exata, por exemplo: Calculadoras, gestão, etc.
#print(1*3)


# Descubra o ano de nascimento do usuario e sua idade atual apenas com o ano atual. Vai usar: Variaveis, input, print e operadores logicos.

#ano = 2025
#
#ano_de_nascimento = int(input('Que ano se nasceu :'))
#
#idade_do_user = print(f"Sua idade é {ano - ano_de_nascimento}") 



#Verificações com if, elif e else.

# if (se) algo for igual, acontecer, precisar, etc e ele for verdadeiro ele continua.

#numero = int(input("Digite um número: "))

#if numero > 10:
#    print('Seu número é maior que 10')
## elif: mesma função do if só que quando uma afirmação for verdadeira el nao verifica as proximas
#if numero < 10:
#    print("Seu número é MENOR que 10")
#if numero == 6:
#    print("Uau, você digitou 6")

#Ou

#elif numero < 10:
#    print("Seu número é MENOR que 10")
#elif numero == 6:
#    print("Uau, você digitou 6")
#
#print("Fim")

# else, usado quando nao tem algo especifico
#idade = 18
#if idade >= 18:
    #print('Pode beber')
#else:
    #print("Não pode")


#Descubra a idade do usuario e mostre se ele pode ou não beber bebidas alcólicas.

#ano = 2025

#nascimento = int(input('Você nasceu em que ano :'))

#idade_user = {ano - nascimento}

#if idade_user > 18:
    #print('Você pode beber alcul')
    
user_ano = int(input('Qual sua idade : '))

if user_ano <= 18:
    print(f"Você não pode beber alcool")
    
else:
    print(f"Você pode beber alcool")
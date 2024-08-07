# #### Inteiros (`int`)
import math


while True:

    menu_exercicio = int(input("Digite o número (Opção de 1 a 25) equivalente ao exercício que deseja Testar: "))
    exercicioImplementado = 0;
    saida = 0;
    quantidadeTentativasValidas = 5;

    # 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
    if menu_exercicio == 1:
        primeiro_numero = int(input("1 - Digite um número inteiro: "))
        segundo_numero = int(input("2 - Digite Mais um número inteiro: "))
        somatorio = primeiro_numero + segundo_numero
        print(f"A soma dos números inteiros informados é: {somatorio}")

    exercicioImplementado = menu_exercicio;

    # 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
    if menu_exercicio == 2:
        numero = float(input("Digite um número: "))
        divisao = numero%5 #Retorna o resto da divisão 
        print(f"O resto da divisão de {numero} por 5 é: {divisao}")

    exercicioImplementado = menu_exercicio;

    # 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
    if menu_exercicio == 3:
        numero1 = int(input("Digite Um Número: "))
        numero2 = int(input("Digite mais um número"))
        resultado = numero1*numero2
        print(f"O Resultado da múltiplicação entre os números fornecidos é: {resultado}")

    exercicioImplementado = menu_exercicio;

    # 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
    if menu_exercicio == 4:
        numero1 = int(input("Digite Um Número: "))
        numero2 = int(input("Digite mais um número"))
        resultado = int(numero1//numero2)
        print(f"O Resultado da Divisão Inteira entre os números fornecidos é: {resultado}")

    exercicioImplementado = menu_exercicio;

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
    if menu_exercicio == 5:
        numero1 = int(input("Digite Um Número: "))
        expoente = int(input("Digite o expoente que deseja que o número fornecido seja elevado: "))
        resultado = int(numero1**expoente)
        print(f"O Resultado de {numero1} elevado à {expoente} é: {resultado}")

    exercicioImplementado = menu_exercicio;

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
    if menu_exercicio == 6:
        numero1 = float(input("Digite Um Número de Decimal: "))
        numero2 = float(input("Digite o Segundo Número Decimal: "))
        resultado = numero1 + numero2;
        print(f"A Soma dos números decimais é: {resultado}")

    exercicioImplementado = menu_exercicio;

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
    if menu_exercicio == 7:
        numero1 = float(input("Digite Um Número de Decimal: "))
        numero2 = float(input("Digite o Segundo Número Decimal: "))
        resultado = float(numero1 + numero2);
        print(f"A Soma dos números decimais é: {resultado:_.2f}")

    exercicioImplementado = menu_exercicio;

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
    if menu_exercicio == 10:
        raio = float(input("Informe o Raio de um Círculo: "))
        areaCirculo = math.pi*(raio**2)
        print(f"A área do Círculo de Raio tamanho {raio} é de: {areaCirculo:_.2f}")

    exercicioImplementado = menu_exercicio;
# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação



    if menu_exercicio > exercicioImplementado:
        print("Exercício ainda não implementado")


    while True:
        if quantidadeTentativasValidas == 5: #Primeira Interação
            saida = int(input("Digite 99 para sair ou 0 para voltar ao Menu Inicial: "))
        else:
            saida = int(input("Opção Inválida, Digite 99 para sair ou 0 para voltar ao Menu Inicial: "))
        if saida == 99:
            False
            break
        elif saida == 00:
            break
        elif quantidadeTentativasValidas == 0:
            break
        elif saida != 0 & saida != 99:
            quantidadeTentativasValidas -= 1;
    
    if quantidadeTentativasValidas == 0:
        print("Quantidade de Tentativas esgotadas, Inicie novamente a aplicação")
        break
    

    

        
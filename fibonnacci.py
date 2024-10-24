
def verifica_fibonacci(numero):
    fibonacci = [0,1]

    while fibonacci[-1] < numero:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    
    if numero in fibonacci:
        print(f"O numero {numero} pertence à sequência de Fibonacci")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci")


print("Vamos verificar se um número inteiro pertence a sequencia de Fibonacci")

while True:
    try:
        numero_informado = int(input("Informe um número para verificação: "))
        resultado = verifica_fibonacci(numero_informado)
        break
    except ValueError:
        print("Por favor insira um valor válido")

    
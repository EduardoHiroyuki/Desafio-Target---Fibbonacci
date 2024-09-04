def fibonacci(n):
    if n <= 0:
        return "O número deve ser positivo"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_prev, fib_atual = 0, 1
        for _ in range(3, n+1):
            fib_prev, fib_atual = fib_atual, fib_prev + fib_atual
        return fib_atual

num = int(input("Digite um número: "))
resultado = fibonacci(num)
print(f"O {num}º número da sequência de Fibonacci é {resultado}")

if resultado == num:
    print("O número informado pertence à sequência de Fibonacci.")
else:
    print("O número informado não pertence à sequência de Fibonacci.")
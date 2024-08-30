def fibonacci_sequence(n):
 
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        next_value = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_value)
    return fib_seq

def is_in_fibonacci(num):
    
    if num < 0:
        return False
    fib_seq = fibonacci_sequence(num)
    return num in fib_seq

def main():
    try:
        number = int(input("Digite um número: "))
        if is_in_fibonacci(number):
            print(f"O número {number} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {number} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()

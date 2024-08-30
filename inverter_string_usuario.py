def inverter_string(s):
    """Inverte os caracteres de uma string sem usar funções prontas."""
    string_invertida = ''
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

def main():
    entrada = input("Digite a string a ser invertida: ")
    resultado = inverter_string(entrada)
    print(f"String invertida: {resultado}")

if __name__ == "__main__":
    main()

def calcular_percentual(faturamento_por_estado):
    """Calcula o percentual de representação de cada estado dentro do valor total mensal."""
    total_faturamento = sum(faturamento_por_estado.values())
    
    percentual_por_estado = {}
    for estado, faturamento in faturamento_por_estado.items():
        percentual = (faturamento / total_faturamento) * 100
        percentual_por_estado[estado] = percentual
    
    return percentual_por_estado

def main():

    faturamento_por_estado = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    
    percentual_por_estado = calcular_percentual(faturamento_por_estado)
    
    print("Percentual de representação por estado:")
    for estado, percentual in percentual_por_estado.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main()

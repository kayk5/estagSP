import json

def calcular_estatisticas(faturamento_diario):
    """Calcula e retorna o menor e maior valor de faturamento, e o número de dias com faturamento acima da média mensal."""
    
    faturamento_diario = [valor for valor in faturamento_diario if valor > 0]

    if not faturamento_diario:
        return None, None, 0  

    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)

    dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_media

def main():
    try:
      
        with open('faturamento.json', 'r') as file:
            data = json.load(file)

       
       
        faturamento_diario = [item['valor'] for item in data['faturamento']]

        menor_faturamento, maior_faturamento, dias_acima_media = calcular_estatisticas(faturamento_diario)

        print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
        print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
        print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")

    except FileNotFoundError:
        print("O arquivo 'faturamento.json' não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
    except KeyError as e:
        print(f"Chave ausente no arquivo JSON: {e}")

if __name__ == "__main__":
    main()

# Função para contar diamantes em uma string
def count_diamonds(test_case):
    stack = []
    diamond_count = 0

    # Ignora as partículas de areia, então consideramos apenas os símbolos '<' e '>'
    for char in test_case:
        if char == '<':
            stack.append(char)
        elif char == '>' and stack:
            # Encontra um par <>, conta como um diamante
            stack.pop()
            diamond_count += 1

    return diamond_count

# Função principal para o processo
def main():
    # Lê o número de casos de teste
    n = int(input().strip())
    results = []

    for _ in range(n):
        # Lê o caso de teste e processa
        test_case = input().strip()
        diamonds = count_diamonds(test_case)
        results.append(str(diamonds))

    # Exibe os resultados de todos os casos de teste
    print("\n".join(results))

# Executa a função principal
main()

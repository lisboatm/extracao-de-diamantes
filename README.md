## Descrição do Problema

João está trabalhando em uma mina e seu objetivo é extrair o máximo de diamantes possíveis a partir de uma sequência de caracteres. Na mina, existem:

- **Diamantes**: Representados pelo padrão `<>`.
- **Partículas de areia**: Representadas pelo caractere `.`.

Durante o processo de extração:
1. Todos os caracteres de areia (`.`) podem ser ignorados.
2. Cada vez que um diamante é encontrado (o padrão `<>`), ele deve ser removido da sequência.
3. A remoção de um diamante pode permitir que novos diamantes sejam formados.

A cada iteração, a remoção de um diamante pode resultar na formação de novos padrões que também devem ser extraídos, até que não haja mais diamantes possíveis de extrair.

## Entrada

- A primeira linha contém um número inteiro **N** (1 ≤ N ≤ 1000), que representa o número de casos de teste.
- Cada uma das próximas **N** linhas contém uma sequência de caracteres (de até 1000 caracteres), que pode incluir os seguintes símbolos:
  - `<>` (diamantes)
  - `.` (areia)

## Saída

Para cada linha de entrada, você deve imprimir um número inteiro representando a quantidade total de diamantes que podem ser extraídos daquela linha.

## Exemplo

### Entrada
```
2
<..><.<..>>
<<<..<......<<<<....>
```

### Saída
```
3
1
```

### Explicação
- Para o primeiro caso:
  - `<..><.<..>>`:
    - Primeiro diamante extraído: `<..>` -> Resta: `<.<..>>`
    - Segundo diamante extraído: `<..>` -> Resta: `<>`
    - Terceiro diamante extraído: `<>` -> Resta: ``
    - Total de diamantes extraídos: **3**
- Para o segundo caso:
  - `<<<..<......<<<<....>`:
    - Apenas um diamante pode ser extraído: `<...>` -> Resta: `<<<...<<<<....>`
    - Total de diamantes extraídos: **1**

## Implementação em Python

Aqui está o código utilizado para resolver o problema:

```python
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

```

## Explicação do Código

1. **Função `extrair_diamantes`**:
   - Utiliza uma pilha para rastrear os caracteres `<` e `>`.
   - Sempre que encontra um `<`, ele é empilhado.
   - Quando encontra um `>`, verifica se há um `<` correspondente na pilha:
     - Se houver, forma-se um diamante e o `<` é removido da pilha.
     - O contador de diamantes é incrementado.
   
2. **Função `main`**:
   - Lê o número de casos de teste.
   - Para cada caso, lê a sequência e calcula o número de diamantes possíveis usando a função `extrair_diamantes`.
   - Imprime o resultado para cada linha de entrada.

## Complexidade

- A complexidade do algoritmo é **O(N * M)**, onde **N** é o número de casos de teste e **M** é o comprimento da sequência em cada caso.
- A solução é eficiente para os limites dados, pois utiliza uma pilha para realizar a correspondência entre os caracteres `<` e `>`, processando cada caractere apenas uma vez.

## Como Executar o Código

Certifique-se de ter **Python 3** instalado em seu sistema. Para executar o programa, siga estas etapas:

1. Salve o código em um arquivo, por exemplo, `extracao_de_diamantes.py`.
2. Abra o terminal e navegue até o diretório onde o arquivo foi salvo.
3. Execute o programa com:
   ```bash
   extracao_de_diamantes.py
   ```
4. Insira os dados de entrada manualmente ou redirecione a entrada a partir de um arquivo:
   ```bash
   python extracao_de_diamantes.py < input.txt
   ```

## Conclusão

Este problema é um exemplo clássico de uso de **estruturas de pilha** para resolver problemas de pareamento e agrupamento de símbolos. A solução foi otimizada para ser eficiente dentro das restrições de tempo e espaço, garantindo que o número máximo de diamantes seja extraído em cada caso de teste.

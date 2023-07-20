# python yield with
Apply Yield and With in Python

## YIELD

Em Python, a palavra-chave `yield` é usada em funções geradoras para criar um gerador. Um gerador é um tipo especial de função que pode ser iterado e retorna um valor por vez, em vez de retornar todos os valores de uma só vez, como uma função normal.

Quando uma função contém a instrução `yield`, ela se torna uma função geradora, e seu comportamento é diferente de uma função comum. Em vez de executar o código inteiro e retornar o resultado final, uma função geradora é pausada e retém seu estado sempre que um valor é gerado usando a instrução `yield`. Quando a próxima iteração é feita, a função retoma a execução a partir do ponto em que foi pausada, mantendo seu estado interno.

Vamos entender isso melhor com um exemplo:

```python
def contador(max_value):
    num = 0
    while num <= max_value:
        yield num
        num += 1

# Criando o gerador
meu_contador = contador(5)

# Iterando sobre o gerador
for valor in meu_contador:
    print(valor)
```

Neste exemplo, a função `contador` é uma função geradora que gera números de 0 a `max_value`. Cada vez que o gerador é iterado (por meio de um loop `for`, por exemplo), ele executa o código dentro da função até encontrar a instrução `yield`. Quando isso acontece, ele pausa a execução e retorna o valor para o loop. Na próxima iteração, a execução da função é retomada a partir do ponto onde parou, mantendo o valor de `num` e permitindo que o próximo valor seja gerado.

Os geradores são úteis quando você tem uma grande quantidade de dados ou resultados que não precisa armazenar completamente na memória, mas quer processar um item de cada vez de forma eficiente. Eles são amplamente usados para gerar sequências infinitas, tratar grandes volumes de dados ou simplificar a lógica de cálculos complexos que não requerem manter todos os resultados em memória ao mesmo tempo.








## WITH
Em Python, o bloco `with` é usado em conjunto com objetos que implementam os chamados "context managers". Os context managers permitem definir ações que devem ser executadas antes e depois de um determinado bloco de código. O bloco `with` garante que essas ações sejam realizadas de forma adequada e automática, mesmo que ocorram exceções durante a execução do código.

A sintaxe básica do bloco `with` é a seguinte:

```python
with contexto as variavel:
    # código que utiliza a variável
```

Os context managers são comumente usados para recursos que precisam ser abertos, manipulados e, em seguida, fechados de forma correta, como arquivos, conexões de rede, transações de banco de dados, entre outros. Ao usar o `with`, você garante que o recurso será liberado e fechado corretamente, mesmo que ocorra uma exceção no bloco de código.

Um exemplo comum é a leitura de um arquivo usando o contexto `with`:

```python
# Abre o arquivo e o fecha automaticamente após o bloco with
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    # Faz algo com o conteúdo do arquivo
```

Neste exemplo, quando o bloco `with` é concluído (seja normalmente ou por causa de uma exceção), o contexto gerenciado pelo `open` garante que o arquivo seja fechado corretamente, mesmo que ocorra um erro durante a leitura.

Os context managers podem ser definidos pelo programador criando uma classe com os métodos especiais `__enter__` e `__exit__`, ou usando a função `contextlib.contextmanager` para criar geradores de contexto de forma mais concisa. Além disso, muitos objetos fornecidos pela biblioteca padrão de Python já são context managers, tornando fácil e conveniente o uso do `with` para gerenciamento seguro de recursos.
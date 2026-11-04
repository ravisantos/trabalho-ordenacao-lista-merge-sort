# Merge Sort — Algoritmo de Ordenação

## 1. Explicação do algoritmo

O **Merge Sort** consiste em um método de ordenação de listas onde a lista é desconstruída para, posteriormente, ser reconstruída com seus elementos na ordem correta.

Em uma lista de números de 1 a 12 fora de ordem, por exemplo:

- Primeiramente, a lista é dividida em 2 partes (esquerda e direita), cada uma com 6 elementos.
- Depois, em 4 partes, cada uma com aproximadamente 3 elementos.
- Em seguida, em grupos cada vez menores, até chegar a 12 grupos, cada um contendo apenas 1 elemento.

Após a divisão, a lista começa a ser reconstruída no mesmo processo, utilizando condicionais que comparam os elementos e determinam a posição correta de cada um na ordem desejada.

Por exemplo:

Considerando que a lista foi dividida em 12 grupos de 1 elemento cada, o método começa comparando os primeiros elementos de cada lado. O menor elemento é adicionado à lista resultante, e a comparação continua com os próximos elementos, até que todos estejam em suas posições corretas.

Dessa forma, os grupos são reunidos gradualmente até formar novamente uma única lista, agora ordenada.

---

## 2. Código-fonte

```python
lista = [5, 3, 8, 6, 2, 7, 4, 1]

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mid = len(lista) // 2
    left = merge_sort(lista[:mid])
    right = merge_sort(lista[mid:])

    return merge(left, right)

def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])

sorted_list = merge_sort(lista)
print("Lista ordenada:", sorted_list)
```

---

## 3. Teste de mesa

**Lista inicial:**

`[5, 3, 8, 6, 2, 7, 4, 1]`

### Etapa 1 — Divisão da lista

A função `merge_sort()` divide a lista recursivamente em duas partes, utilizando `mid` para determinar o ponto de divisão.

O processo acontece da seguinte maneira:

```text
             [5, 3, 8, 6, 2, 7, 4, 1]
                  /           \
          [5, 3, 8, 6]       [2, 7, 4, 1]
            /      \           /      \
         [5, 3]   [8, 6]     [2, 7]   [4, 1]
          / \      / \       / \      / \
        [5] [3]  [8] [6]   [2] [7]  [4] [1]
```

Quando cada divisão chega a uma lista com apenas um elemento, a condição `if len(lista) <= 1` é satisfeita, encerrando aquela chamada recursiva e retornando a lista.

### Etapa 2 — Primeiras comparações

A função `merge()` começa a reconstruir as listas, comparando seus primeiros elementos.

| Comparação | Condição | Resultado |
|---|---|---|
| 5 e 3 | 5 < 3 | `[3, 5]` |
| 8 e 6 | 8 < 6 | `[6, 8]` |
| 2 e 7 | 2 < 7 | `[2, 7]` |
| 4 e 1 | 4 < 1 | `[1, 4]` |

Ao final dessas comparações, temos:

```text
[3, 5]   [6, 8]   [2, 7]   [1, 4]
```

### Etapa 3 — Segunda reconstrução

Agora, as listas ordenadas anteriormente são comparadas novamente.

| Comparação | Condição | Elemento escolhido |
|---|---|---|
| 3 e 6 | 3 < 6 | 3 |
| 5 e 6 | 5 < 6 | 5 |
| 2 e 1 | 2 < 1 | 1 |
| 2 e 4 | 2 < 4 | 2 |
| 7 e 4 | 7 < 4 | 4 |
| 7 e restante | Lista da direita vazia | 7 |

Resultados:

```text
[3, 5, 6, 8]   [1, 2, 4, 7]
```

### Etapa 4 — Comparação final

Por último, as duas listas restantes são comparadas e reunidas em uma única lista.

| Comparação | Condição | Elemento escolhido |
|---|---|---|
| 3 e 1 | 3 < 1 | 1 |
| 3 e 2 | 3 < 2 | 2 |
| 3 e 4 | 3 < 4 | 3 |
| 5 e 4 | 5 < 4 | 4 |
| 5 e 7 | 5 < 7 | 5 |
| 6 e 7 | 6 < 7 | 6 |
| 8 e 7 | 8 < 7 | 7 |
| 8 e lista vazia | Lista da direita vazia | 8 |

Quando uma das listas fica vazia, a condição `if not left` ou `if not right` é satisfeita, fazendo com que os elementos restantes sejam adicionados diretamente ao resultado.

**Resultado final:**

```python
Lista ordenada: [1, 2, 3, 4, 5, 6, 7, 8]
```

---

## 4. Conclusão

O Merge Sort demonstra como a recursividade pode ser utilizada para resolver problemas de ordenação. Ao dividir uma lista em partes menores e reconstruí-la por meio de comparações, o algoritmo consegue organizar seus elementos de maneira eficiente.

Sua complexidade de tempo é **O(n log n)**, tanto no melhor quanto no caso médio e no pior caso.
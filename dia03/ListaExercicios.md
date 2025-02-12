### Criando uma lista
```python
lista1 = ["arroz", "feijão", "peito de frango", "alface"]
print(lista1)

```
['arroz', 'feijão', 'peito de frango', 'alface']
### Atualizando um item da lista
```python
lista1[2] = "bife"
print(lista1)

```
['arroz', 'feijão', 'bife', 'alface']

### Deletando um item da lista
```python
del lista1[1]
print(lista1)

```
['arroz', 'peito de frango', 'alface']

### Criando lista de listas
```python
listas = [[1, 2, 3], [10, 20, 30], [1.5, 3, 4.5]]
print(listas)

```
[[1, 2, 3], [10, 20, 30], [1.5, 3, 4.5]]

### Atribuindo items da lista a uma variável
```python
a = listas[0]
print(a)

```
[1, 2, 3]

```python
b = a[2]
print(b)

```
3

### Operações com listas
```python
x = listas[0][0]
print(x)

```
1

```python
c = listas[2][0] + 10
print(c)

```
11.5

```python
z = 20
w = z * listas[0][2]
print(w)

```
60

### Concatenando listas
```python
lista_1 = [34, 30, 26]
lista_2 = [10, 20, 30]
total = lista_1 + lista_2
print(total)

```
[34, 30, 26, 10, 20, 30]

### Operador IN
```python
print(25 in lista_1)

```
False

```python
print(30 in lista_2)

```
True

### Funções  Built-in
```python
len(lista_2)

```
3

```python
max(lista_1)

```
34

```python
min(lista_1)

```
26

### Adicionando item a lista
```python
lista_nomes = ["Ana", "Maria", "João", "Paulo"]
lista_nomes.append("Vitória")
print(lista_nomes)

```
['Ana', 'Maria', 'João', 'Paulo', 'Vitória']

### Copiando items de uma lista para outra
```python
old_list = [1, 2, 5, 20]
new_list = []

for item in old_list:
  new_list.append(item)
print(new_list)

```
[1, 2, 5, 20]

```python
new_list.extend([100, 605, 220])
print(new_list)

```
[1, 2, 5, 20, 100, 605, 220]

```python
new_list.insert(2, 3)

```
[1, 2, 3, 3, 3, 3, 3, 5, 20, 100, 605, 220]

```python
new_list.index(5)

```
7

```python
new_list.remove(3)

```
[1, 2, 3, 3, 3, 5, 20, 100, 605, 220]

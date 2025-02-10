alunos_dict = {"Gustavo": 30, "Pedro": 25, "Carolina": 29, "Ana": 22}

### No dicionário, cada elemento é um par de chaves e valor, separados por vírgula
```python
print(alunos_dict["Ana"])

```
22

### Adicionando elementos no dicionário
```python
alunos_dict["Marcelo"] = 45
print(alunos_dict)

```
alunos_dict = {"Gustavo": 30, "Pedro": 25, "Carolina": 29, "Ana": 22, "Marcelo": 45}

### Deixando um dicionário vazio
```python
alunos_dict.clear()

```

### Deletando um dicionário
```python
del alunos_dict

```

### Funções Built-in
estudantes = {"Pedro": 25, "Camila": 32, "Henrique": 26}
```python
len(estudantes)

```
3

```python
alunos_dict.keys()

```
dict_keys(['Pedro', 'Camila', 'Henrique'])

```python
estudantes.values()

```
dict_values([25, 32, 26])

```python
estudantes.items()

```
dict_items([('Pedro', 25), ('Camila', 32), ('Henrique', 26)])

### Dicionário de Listas
dict3 = {'chave1': 1230, 'chave2':[22, 453, 73, 41], 'chave3':['carne', 'frango', 'peixe']}

```python
print(dict3['chave3'][0].upper())  # 'CARNE'

```
'CARNE'

```python
var1 = dict3['chave2'][0] - 2
print(var1)

```
20





### As strings podem ser entre aspas simples e aspas duplas
```python
print("Hello World")
print('Hello World')

```
Hello World

Hello World

### A indexação em Python sempre começa por zero
```python
s = 'Data Science'
print(s)

```
Data Science

```python
print(s[0])

```
D

```python
print(s[1])

```
a

### Podemos usar o operador : para executar um slicing
```python
print(s[1:])

```
ata Science

```
print(s[:3])

```
Dat

### Concatenando Strings
```python
s = (s + 'Academy')
print(s)

```
Data Science Academy

```python
letra = 'k'
print(letra*5)

```
kkkkk

### Também é possível aplicar Funções Built-in nas strings
```python
print(s.upper())

```
DATA SCIENCE ACADEMY

```python
print(s.lower())

```
data science academy

```python
print(s.split())

```
['Data', 'Science', 'Academy']

```python
print(s.count('a'))

```
4

```python
print(s.capitalize())

```
Data science academy

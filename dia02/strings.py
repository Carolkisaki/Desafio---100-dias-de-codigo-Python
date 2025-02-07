# As strings podem ser entre aspas simples e aspas duplas
print("Hello World")
print('Hello World')

# A indexação em Python sempre começa por zero
s = 'Data Science'
print(s)
Data Science

print(s[0])
'D'
print(s[1])
'a'

# Podemos usar o operador : para executar um slicing
print(s[1:])
'ata Science'
print(s[:3])
'Dat'

# Concatenando Strings
s = (s + 'Academy')
print(s)
'Data Science Academy'

letra = 'k'
print(letra*5)
'kkkkk'

#Também é possível aplicar Funções Built-in nas strings
print(s.upper())
'DATA SCIENCE ACADEMY'

print(s.lower())
'data science academy'

print(s.split())
['Data', 'Science', 'Academy']

print(s.count('a'))
4

print(s.capitalize())
'Data science academy'

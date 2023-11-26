x = 1
x = .87
x = complex(56, 2j)
x = True

x = 'alberto'
x = "alberto"
x = """
    ioajwdjawiod awdauiwduaw
    awudhuiaw d
    awuidhaiwd
"""
y = 458 + 89 + .218
x = f'wiadhiuhwd {y:.2f}'

x = ['beatriz', 'roberta']
x.append('alberto')
x.append('adriano')
x.extend(['renato', 'manoel'])
x.insert(2, 'XVIDROS')
x.remove('adriano')
x.pop(2)

x = 'alberto', 'gustavo'

x = {'nome': 'alberto', 'idade': 18}
x['nome'] = 'augusto'
x['novo'] = True

z = x.items()

a, b, (c, d) = 1, 2, (1, 2)

a, b = list(z)[0]

# for key, value in x.items():
#     print(f'{key} -> {value}')

y = ['alberto', 'gustavo', 'yasmin']

x = [nome.upper() + ' 2 0' for nome in y]

print(x)
print(type(x))

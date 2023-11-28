import os


os.system('cls')

# for i in range(10):
#     print(i)

# print(range(10)[7])

# print(type(range(10)))

lista = [1, 1, 2, 3, 4, 87, 10, 20, 4, 5, 6, 7, 65 , 6]

for x in lista:
    print(x)

    if x > 500:
        break
else:
    print('caiu no else')

print('final')

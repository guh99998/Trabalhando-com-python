import os

os.system('cls')

# for x in range(1,10,2):
#     print(x)

# for i in range(10):
#     print(i)

lista = [1, 1, 2, 3, 4, 87, 10, 20, 5, 56, 81, 518, 0, 60]

for x in lista:
    print(x)

    if x > 600:
        break

else:
    print('caiu no else')


print('final')
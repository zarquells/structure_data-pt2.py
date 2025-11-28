import numpy as np

# exercicio 01
list_of_nums = []
list_of_nums.append(10)
print(list_of_nums)

# exercicio 02
list_of_nums1 = []
listinha = [5, 3, 8, 6, 1]
for i in range(len(listinha)):
    list_of_nums1.append(listinha[i])
print(list_of_nums1)

# exercicio 03
list_of_nums2 = [1,2,3]
def function_insert(lista, value):
    lista.append(value)
    return 'Lista atualizada:', lista
print(function_insert(list_of_nums2, -1))

# exercicio 04
list_of_nums3 = [11, 2, 48, 33, 3, 22, 21]
def function_search(lista, value):
    for i in range(len(lista)):
        if lista[i] == value:
            return 'Índice do elemento encontrado: ', i
        
    return 'Elemento não encontrado', -1
print(function_search(list_of_nums3, 330))

# exercicio 05
list_of_nums4 = [11, 2, 48, 33, 3, 22,21]
def function_remove(lista, value):
    for i in range(len(lista)):
        if lista[i] == value:
            lista.pop(i)
            return 'Elemento removido, lista atualizada: ', lista
    return 'Não foi encontrado o elemento na lista', value
print(function_remove(list_of_nums4, 3))

# exercicio 06
list_of_nums5 = [10,20,30,40,50]
def function_insert_ord(lista, value):
    for i in range(len(lista)):
        if lista[i] > value:
            lista.insert(i, value)
            return 'Lista ordenada com novo elemento:', lista
        lista.append(value)
        return 'Lista ordenada com novo elemento:', lista
print(function_insert_ord(list_of_nums5, 5))

# exercicio 07
list_of_nums6 = []
def function_insert_ten(lista):
    for i in range(1, 11):
        lista.append(i)
    return 'Lista com novos valores:', lista
print(function_insert_ten(list_of_nums6))

# exercicio 08
list_of_nums7 = [1,2,3]
def function_reverse(lista):
    for i in range(len(lista)):
        count = -1
        lista.insert(i, lista[count])
        lista.pop()
    return 'Lista invertida:', lista
print(function_reverse(list_of_nums7))

# exercicio 09
list_of_nums8 = [2, 2]
def function_sum_list(lista):
    return 'Soma de todos os elementos juntos:', sum(lista)
print(function_sum_list(list_of_nums8))

# exercicio 10
list_of_nums9 = [2, 900, 300, 4]
def function_search_max(lista):
    return 'Maior elemento na lista:', max(lista)
print(function_search_max(list_of_nums9))

# exercicio 11
list_of_nums10 = [2, 900, 300, 4]
def function_search_min(lista):
    return 'Menor elemento na lista:', min(lista)
print(function_search_min(list_of_nums10))

# exercicio 12
list_of_nums11 = [2, 2, 20, 3]
def function_search_element(lista, elemento):
    return 'Quantas vezes o elemento aparece na lista:', lista.count(int(elemento))
print(function_search_element(list_of_nums11, 2))

# exercicio 13
list_of_nums12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def function_search_pares(lista):
    listinha = []
    for i in range(len(lista)): #em cada índice da lista
        if (lista[i] % 2 == 0):
            listinha.append(lista[i])
    return 'Números pares: ', listinha
print(function_search_pares(list_of_nums12))

# exercicio 14
list_of_nums13 = [2, 4, 6, 8, 10]
def function_pow_elements(lista):
    listinha = []
    for i in range(len(lista)):
        listinha.append((lista[i]**2))
    return 'Todos os elementos ao quadradinho:', listinha
print(function_pow_elements(list_of_nums13))

# exercicio 15
list_of_nums14 = [11, 2, 48, 33, 3, 22,21]
def function_search_boolean(lista, value):
    if value in lista:
        return 'Existe o elemento na lista?', True
    return 'Existe o elemento na lista?', False
print(function_search_boolean(list_of_nums14, 110))

# exercicio 16
list_of_nums15 = [1, 1, 2, 2, 3, 3]
def function_no_duplicates(lista):
    listinha = []
    for i in range(len(lista)):
        if lista[i] not in listinha:
            listinha.append(lista[i])
    return 'Lista sem duplicatas:', listinha
print(function_no_duplicates(list_of_nums15))

# exercicio 17
list_of_nums16 = [1, 2, 3]
def function_insert_no_duplicates(lista, value):
    for i in range(len(lista)):
        if value not in lista:
            lista.append(value)
            return 'Adicionado', lista
        else:
            return 'Não pode não! Já existe o valor na lista'
print(function_insert_no_duplicates(list_of_nums16, 1))

# exercicio 18
list_of_nums17 = [1, 2, 3]
list_of_nums18 = [4, 5, 6]
def function_combine_lists(lista1, lista2):
    lista1.extend(lista2)
    return 'Lista extendida: ', lista1
print(function_combine_lists(list_of_nums17, list_of_nums18))

# exercicio 19
# não sei fazer de outro jeito

# exercicio 20
list_of_nums19 = [3, 3]
def function_mediam(lista):
    media = sum(lista)/len(lista)
    return 'Média da lista:', media
print(function_mediam(list_of_nums19))

# exercicio 21
list_of_nums20 = [10, 100, 1000]
def function_second_bigvalue(lista):
    listinha = lista
    listinha.remove(max(list_of_nums20))

    return 'Segundo maior da lista: ', max(listinha)
print(function_second_bigvalue(list_of_nums20))

# exercicio 22
def function_return_maiorvalue(lista, value):
    for i in range(len(lista)):
        if lista[i] > value:
            return 'Índice do número maior que o inserido:', i
        elif lista[i] == value:
            return 'Índice do número IGUAL ao inserido:', i
    return 'Não há número maior na lista que o inserido'
print(function_return_maiorvalue(list_of_nums20, 10000))
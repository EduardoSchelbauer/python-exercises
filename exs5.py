def remove_duplicates(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst

lista = [1, 2, 3, 2, 4, 1, 5, 6, 5]
nova_lista = remove_duplicates(lista)
print(nova_lista)
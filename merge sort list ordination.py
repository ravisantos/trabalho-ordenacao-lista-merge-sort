#merge sort puramente recursivo

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

# def merge_sort_invert(lista):
#     if len(lista) <=1:
#         return lista

#     mid = len(lista) // 2
#     left = merge_sort_invert(lista[:mid])
#     right = merge_sort_invert(lista[mid:])

#     return merge_invert(left, right)

# def merge_invert(left, right):
#     if not left:
#         return right
#     if not right:
#         return left

#     if left[0] > right[0]:
#         return [left[0]] + merge_invert(left[1:], right)
#     else:
#         return [right[0]] + merge_invert(left, right[1:])

# sorted_list_invert = merge_sort_invert(lista)
# print("Lista ordenada (invertida):", sorted_list_invert)
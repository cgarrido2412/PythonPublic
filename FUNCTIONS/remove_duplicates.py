def remove_duplicates(list_one):
    list_two = []
    if list_one:
        for item in list_one:
            if item not in list_two:
                list_two.append(item)
    else:
        return list_one
    return list_two
print(remove_duplicates([1,2,2,2,3]))

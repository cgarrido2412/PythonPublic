def my_function(x):
    return list(dict.fromkeys(x))
    
my_list = my_function(['a', 'a', 'b', 'c', 'd'])
print(my_list)

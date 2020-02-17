def file_test(x):
    try:
        open(x)
    except FileNotFoundError:
        print('Unable to open file.')
        exit()

def integer_check(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

#!Python3
import random

def validate_integer(s): 

    try:
        int(s)
        return True

    except ValueError:
        return False

try:    

    def generate():
        integer_check = False

        while integer_check is False:

            try:
                length = int(input('Specify a password length (integer): \n'))

                if validate_integer(length) is True:
                    integer_check = True

                else:
                    pass

            except ValueError:
                print('You need to type an integer.')
        similar_characters = 'il|1LoO0il|1LoO0il|1LoO0il|1LoO0il|1LoO0'
        ambiguous_characters = '{}[]()//\'"`~,;:.<>'
        character_pool = similar_characters + ambiguous_characters
        password = ''.join(random.sample(character_pool, length))
        print(password)
    finished = False

    while finished is False:
        generate()
        check = input('Generate another? [y/n] \n')

        if check == 'n':
            print('Exiting...')
            finished = True

        elif check =='y':
            pass 

        else:
            print('Only choose [y/n] \nExiting...')
            break

except KeyboardInterrupt:
    print('Program terminated by user.')

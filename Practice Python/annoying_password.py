import random

try:    

    def generate():
        length = int(input('Specify a password length (integer): \n'))
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
            finished = True

        else:
            pass

except KeyboardInterrupt:
    print('Program terminated by user.')

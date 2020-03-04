def capitalize_first_letter_of_every_word(s):
    words = s.split(' ')
    for x in range(len(words)):
        words[x] = words[x].capitalize()
    answer = ' '.join([x for x in words])
    return answer

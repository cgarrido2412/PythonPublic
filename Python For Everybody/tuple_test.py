dictionary_for_hour = dict()
my_list = []
file_name = input('Enter file name: \n')

try:
    file_handle = open(file_name)

    for line in file_handle:
        words = line.split()

        if len(words) < 2 or words[0] != 'From':
            continue

        column_position = words[5].find(':')
        hour = words[5][:column_position]

        if hour not in dictionary_for_hour:
            dictionary_for_hour[hour] = 1

        else:
            dictionary_for_hour[hour] += 1

    for key, val in list(dictionary_for_hour.items()):
        my_list.append((key, val))
        my_list.sort()

    for key, val in my_list:
        print(key, val)

except:
    print('File cannot be opened:', file_name)
    quit()

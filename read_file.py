def read_file(input_file):

    # Read file and handle exceptions
    try:
        file = open(input_file, 'r')
        dictionary = {}

        for line in file:
            (key, value) = (line.strip()).split(', ')
            dictionary.update({key: value})
        file.close()

        return dictionary

    except FileNotFoundError as error:
        print(error)

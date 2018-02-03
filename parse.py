def parse(request):
    # Converting to JSON
    data_json = request.json()

    # Navigating the JSON file to most recent measurements
    main = data_json['list'][0]['main']
    weather = data_json['list'][0]['weather'][0]
    wind = data_json['list'][0]['wind']
    updated = data_json['list'][0]['dt']

    # Setting up Variables for easy retrieval
    temp = main['temp']
    temp_min = main['temp_min']
    temp_max = main['temp_max']

    description = weather['description']

    wind_speed = wind['speed']

    # Convert time
    import utc_to_x
    converted_time = utc_to_x.convert(updated)

    output = [temp, temp_max, temp_min, description, wind_speed, updated]

    result = 'The forecast for today is: ' + output[3]
    result += ' with a high of ' + str(int(output[1]))
    result += 'F, a low of ' + str(int(output[2]))
    result += 'F ,and winds at ' + str(int(output[4]))
    result += ' mph. This information was updated on ' + str(output[5]) + ' GMT.'

    return result

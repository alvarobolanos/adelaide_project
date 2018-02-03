import requests


def acquire():

    # Communication setup

    api = "a74423ff84723beb9a456818267086f1"
    url = "http://api.openweathermap.org/data/2.5/forecast?units=imperial&id=4167147&appid="+api
    # print('Fetching data from: '+url)
    request = requests.get(url)

    return request

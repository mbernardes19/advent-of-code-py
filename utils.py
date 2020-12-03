from decouple import config
import http.client

COOKIE = config('COOKIE')


def get_entries(day):
    url = 'adventofcode.com'
    connection = http.client.HTTPSConnection(url)
    headers = {'cookie': COOKIE}
    connection.request('GET', '/2020/day/{}/input'.format(day), None, headers)
    response = connection.getresponse()
    return response.read().decode().split("\n")

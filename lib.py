import requests
from unittest.mock import patch

search_url = "https://nominatim.openstreetmap.org/search"
ram_url = "https://rickandmortyapi.com/api/character"
reverse_url = "https://nominatim.openstreetmap.org/reverse"


def rick_and_mor_api():
    response = requests.get(url=ram_url)
    if response.ok:
        result = response.json()
        return result['info']['count']
    return 0


def counter(url):
    print(url)
    response = requests.get(url=url)
    count = 0
    if response.ok:
        result = response.json()
        count += len(result['results'])
        if result['info']['next']:
            count += counter(result['info']['next'])
    return count


def rick_and_mor_api_counter():
    return counter(ram_url)


def dir_geocoding(amenity, limit=10):
    params_limit = {
        "amenity": amenity,
        "limit": limit,
        "format": 'json'
    }

    response = requests.get(url=search_url,
                            params=params_limit)

    result = response.json()
    print(result)
    return result


def rev_geocoding(lat, lon, limit=10):
    params_limit = {
        "limit": limit,
        "accept-language": "en",
        "format": 'json'
    }
    url = reverse_url + "?lat=" + str(lat) + "&lon=" + str(lon)
    print(url)
    response = requests.get(url=url,
                            params=params_limit)

    result = response.json()
    print(result)
    return result


def test_api(amenity, limit=10, format='json'):
    params_limit = {
        "amenity": amenity,
        "limit": limit,
        "format": format
    }
    response = requests.get(url=search_url,
                            params=params_limit)
    result = response.json()
    print(result)
    return result


def mock_test(amenity, limit, format):
    with patch('requests.get') as mock_get:
        class MockResponse:
            def json(self):
                return [{'name': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'}]
        mock_get.return_value = MockResponse()
        return test_api(amenity, limit, format)


def get_limit(limit):
    params_limit = {
        "amenity": 'pub',
        "limit": limit,
        "format": 'json'
    }

    response = requests.get(url=search_url,
                            params=params_limit)

    result = response.json()
    if response.ok:
        return len(result)


def get_default_limit():
    """
    :return: Возвращает дефолтное количество
    """
    params_limit = {
        "amenity": 'pub',
        "format": 'json'
    }
    response = requests.get(url=search_url,
                            params=params_limit)
    result = response.json()
    if response.ok:
        return len(result)


def get_limit_magnit(dump):
    count = 0
    with open(dump, 'r') as f:
        file = f.readlines()
        for line in file:
            addr = line.split(',')
            city = addr[0]
            streetname = addr[1]
            housenumber = addr[2]

            params_sdek = {
                'city': city,
                'street': f'{housenumber}{streetname}',
                "format": 'json'
            }

            print(params_sdek)

            response = requests.get(url=search_url,
                                    params=params_sdek)
            print(response.url)
            if response.ok:
                for i in response.json():
                    if 'Магнит' in i['display_name']:
                        count += 1
                        print(i)
    return count

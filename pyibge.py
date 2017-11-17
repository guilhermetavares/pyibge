import re
from urllib.request import urlopen
from urllib.error import HTTPError


def geografos(city):
    '''
    city must be a slug
    Example: Ribeirão Preto -> ribeirao-preto
    '''

    try:
        url = 'http://www.geografos.com.br/gentilicos/gentilico-{0}.php'
        content = str(urlopen(url.format(city)).read())
    except HTTPError:
        return None

    for item in re.compile('IBGE: (.*?)<br>').findall(content):
        number = re.sub(r'[^\d]+', '', item)
        if number:
            return number
    
    return None

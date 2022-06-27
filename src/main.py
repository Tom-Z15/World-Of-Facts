import requests as r


class Api:
    def __init__(self, url:str, category:str) -> None:
        self.url = url
        self.category = category


    def get_json(self):
        rq = r.get(self.url)
        if rq.status_code != 200:
            return 1
        try:
            data = rq.json()
            return data
        except:
            return 2
    

    def get_text(self):
        rq = r.get(self.url)
        if rq.status_code != r.status_codes.ok:
            return 1
        try:
            data = rq.text
            return data
        except:
            return 2


apis = [
        Api('http://dog-api.kinduff.com/api/facts', 'Dogs'),
        Api('https://catfact.ninja/fact', 'Cats'),
        Api('https://api.chucknorris.io/jokes/random', 'Chuck Norris')
    ]


def get_api(category:str):
    for api in apis:
        if api.category.lower() == category.lower():
            return api

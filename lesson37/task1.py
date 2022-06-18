import requests
url = 'https://misu.pp.ua/api/import/indicators'
head = {'Authorization' : 'Token f634ee85a9ae3d4c6b28fe831f3c27802c7f563e'}

a = requests.post(url, headers = head, json={
    "pressure": [
        {
            "value": 200,
            "date": "2022-11-15T13:44:00+03:00",
            "additional": 150
        }
    ]
})
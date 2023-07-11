import requests


def random_user(user_data):
    person = user_data["results"][0]["name"]
    print(person["first"] , person["last"])

url =  'https://randomuser.me/api/' #url to api
response = requests.get(url) 
if response.status_code == 200: #200 = ok
    data = response.json() #data comes in as a string (text), so you make it json
    random_user(data)

else:
    print(f"Can't fetch data from API, status {response.status_code}")
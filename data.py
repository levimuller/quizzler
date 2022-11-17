import requests

TYPE = "boolean"
AMOUNT = 10

parameters = {
    "type": TYPE,
    "amount": AMOUNT,
    "category": 18
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]

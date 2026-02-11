# Ditt namn
# Din klass
# Datum

import requests

# In this uppgift you are supposed to fill in the spots where it says xxx or the rows with TODO
# Take the https address and open it in your browser to see the API content

# Uppgift 1

response = requests.get("https://open.er-api.com/v6/latest/USD")
answer = response.json()
print(f"One USD is worth {xxx} SEK right now.")

# Uppgift 2

response = requests.get("https://randomuser.me/api/")
answer = response.json()
print(
    f"Your agent name is {' '.join(answer['results'][0]['name'].values())} and you live in {xxx}"
)


# Uppgift 3

response = requests.get(
    "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=mojito"
)
answer = response.json()
print(f"The different mojito drinks I can offer is:")
# TODO - Print out all mojito drinks from answer. You will need a for loop.

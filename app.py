import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "5o-VAGm3X6Jw-4UI-eeZ_vXX3vaTt44OQWm898DIXUeyznhCIhJHCQhdBOg9_2AcFieclal5jljIynax0MYCl86UEovc7eh8OWpgh6B-sQw4vc464WJLAeL7cU3IXnYx"

headers = {
    "Authorization": "Bearer " + api_key
}

params = {
    "term": "Barber",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]

# [item for item in list]
names = [business["name"]
         for business in businesses if business["rating"] > 4.5]

# for business in businesses:
#     print(business["name"])

print(names)

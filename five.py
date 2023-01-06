import requests
import json

# r = requests.get("https://pokeapi.co/api/v2/pokemon/1/")
# print(r.data)

# r = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")

# json_object = json.loads(r.text)
# # print(json.dumps(json_object, indent=2))
# print(json_object['name'])

# ----------------------

# pokemon_number = 0
# while pokemon_number < 151:
#     pokemon_number += 1
#     r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}/")
#     json_object = json.loads(r.text)
#     print(json_object['name'])


# ----------------------

# pokemon_number = 0
# while pokemon_number < 151:
#     pokemon_number += 1
#     r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}/")
#     json_object = json.loads(r.text)
#     types = json_object['types']
#     types_list = []
#     for type in types:
#         types_list.append(type['type'] ['name'])
#     print(f"{json_object['name']} types are {types_list}")


# ----------------------

# request = requests.get("http://jenkins.dev.tgp.digicert.com:8080/job/pipelines/api/python?pretty=true")

# print(request.text)

# ----------------------

request = requests.get("http://jenkins.dev.tgp.digicert.com:8080/job/pipelines/api/python?pretty=true")

print(request.text)
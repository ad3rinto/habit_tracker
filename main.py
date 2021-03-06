import requests
from datetime import datetime


TOKEN = 'your own token'
USERNAME = 'your own user name'
GRAPH_ID = 'graph1'
# weblink https://pixe.la/v1/users/aad3rinto/graphs/graph1.html
# USED TO CREATE CREDENTIALS

pixela_endpoint = 'https://pixe.la/v1/users'
# user_params = {
#     'token': 'TOKEN',
#     'username': 'USERNAME',
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes',
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# CREATE A GRAPH
# graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
# graph_config = {
#     'id': 'graph1',
#     'name': 'Walking Graph',
#     'type': 'float',
#     'unit': 'Km',
#     'color': 'ajisai'
# }
headers = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# posting a value to the graph
today = datetime(year=2021, month=10, day=13)
#print(today.strftime('%Y%m%d'))

graph_post_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
post_pixel_params = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '500'
}

response = requests.post(url=graph_post_pixel_endpoint, json=post_pixel_params, headers=headers)
print(response.text)

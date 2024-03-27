import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()
TOKEN = os.environ.get('TOKEN')
USERNAME = os.environ.get("USERNAME")
GRAPH_ID = 'graph1'
# weblink https://pixe.la/v1/users/aad3rinto/graphs/graph1.html
# USED TO CREATE CREDENTIALS
# print(TOKEN, USERNAME)
pixela_endpoint = 'https://pixe.la/v1/users'
# user_params = {
#     'token': TOKEN,
#     'username': USERNAME,
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
#
headers = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# posting a value to the graph
# today = datetime(year=2021, month=10, day=13)
today = datetime.today()
print(today.strftime('%Y%m%d'))
#
graph_post_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
post_pixel_params = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '1500'
}

response = requests.post(url=graph_post_pixel_endpoint, json=post_pixel_params, headers=headers)
print(response.text)

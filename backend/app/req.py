import requests

# new_user = {
#     'firstName': 'Cesar',
#     'lastName': 'Moreno',
#     'email': 'cmoreno@neural.com.do',
#     'password': '032659',
#     'role': 'CLIENT',
# }

# response = requests.post(
#     'http://localhost:8000/users',
#     json=new_user
# )

response = requests.get('https://randomuser.me/api/')
print(response.text)

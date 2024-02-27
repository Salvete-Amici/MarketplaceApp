from faker import Faker
import requests 
import json

faker = Faker()

def generate_user ():
  # data for user registration
  username = faker.name()
  contact_info = faker.phone_number()
  email = faker.email()
  password = faker.password()
  return {"username": username, "contact_info": contact_info, "email": email, "password": password}

new_user_endpoint = "http://127.0.0.1:5000/api/users/"

for i in range(99):
  user = json.dumps(generate_user())
  status = requests.post(new_user_endpoint, data = user, headers = {"Content-Type": "application/json"})
  print(json.dumps(status.json(), indent = 2) + ", " + str(status.status_code))
  

from faker import Faker
import csv

fake = Faker()
users = []

def create_user(i):
    user = {}

    

    fakeName = fake.name()
    ind = fakeName.index(' ')
    name = fakeName[0:ind] 
    second_name = fakeName[ind+1:] 

    user['customer_id'] = i
    user['name'] = name.strip()
    user ["second_name"] = second_name.strip()
    user["address"] = fake.address()
    user["company"] = "Mondial"
    user['gender'] = "muski" 
    
    

    return user

i = 0
while ( i <  100):
    users.append(create_user(i))
    i = i + 1

fieldanames= ['customer_id', 'name', 'second_name', 'address', 'company', 'gender']
with open('users.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file,fieldnames=fieldanames)
    writer.writeheader()
    writer.writerows(users)
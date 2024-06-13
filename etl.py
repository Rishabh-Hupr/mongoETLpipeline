import json
from datetime import datetime
import pymongo

# Extract
with open('req.json', 'r') as file:
    req_data = json.load(file)

with open('application.json', 'r') as file:
    application_data = json.load(file)

with open('user.json', 'r') as file:
    user_data = json.load(file)

# Transform
# Join req and application data
joined_data = []

try:
    for req in req_data:
        for app in application_data:
            if app['req_id'] == req['req_id']:
                joined_row = {**req, **app}
                joined_data.append(joined_row)

    # Merging user data
    for row in joined_data:
        matching_user = None
        for user in user_data:
            if user['name'] == row['candidate_name']:
                row['email'] = user['email']
                row['role'] = user['role']

    # Ensuring all dates are in ISO format
    for row in joined_data:
        row['posted_date'] = datetime.strptime(row['posted_date'], '%Y-%m-%d').isoformat()
        row['applied_date'] = datetime.strptime(row['applied_date'], '%Y-%m-%d').isoformat()
except Exception as e:
    print(e)
# print(json.dumps(joined_data, indent=2))

# loading in MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["newDB"]
collection = db["etl_output"]
collection.insert_many(joined_data)
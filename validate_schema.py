from datetime import datetime
import json
from schema_validator.validator import validator


with open('models/customer.json', 'r') as j:
    schema = json.loads(j.read())

customer = {
    "_id":          123,
    "created":      datetime.now(),
    "is_active":    True,
    "fullname":     "Jorge York",
    "age":          32,
    "contact": {
        "phone":      "559-940-1435",
        "email":      "york@example.com",
        "skype":      "j.york123"
    },
    "cards": [
        {"type": "visa", "expires": "12/2029"},
        {"type": "visa"},
    ]
}

errors = validator.validate(schema, customer)
for err in errors:
    print(err['msg'])
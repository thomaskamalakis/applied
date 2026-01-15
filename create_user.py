from budilib import create_user

user_data = {
    "roles": { "app_cc3b874204d14304afbdd77f62d8eafb": "ADMIN" },
    "firstName": "Thomas",
    "lastName": "Kamalakis",
    "forceResetPassword": False,
    "email": "thkam2@hua.gr",
    "password": "hua123hua123",
    "status": "active"
}

response = create_user(user_data)
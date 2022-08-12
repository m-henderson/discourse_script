import json
def get_usernames():
    user_names = []
    with open('./users.json') as data_file:
        data = json.load(data_file)
        for v in data:
            if (v["id"] == -1) or (v["id"] == 1):
                print('not using user: owner or system')
            else:
                user_names.append(v["username"])
        print('users loaded into temp array...')
    return user_names
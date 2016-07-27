import requests
import com.xhaus.jyson.JysonCodec as json
from com.xhaus.jyson import JSONDecodeError


def get_user_list():

        usrLst = []

        url = "http://%s:%s@%s:%s/users" % (username, password, hostname, "5516")

        # try to fetch a response
        response = requests.get(url, verify=False)

        user_dict = json.loads(str(response.text))

        for u in user_dict:
            usrLst.append(u)

        return usrLst


def filter_user(users):
    newUserList = []
    excludedUsersList = excludedUsers.split(';')

    for u in users:
        if u['username'] not in excludedUsersList:
            newUserList.append(u)

    return newUserList


def delete_user(user):

    url = "http://%s:%s@%s:%s/users/%s" % (username, password, hostname, "5516", user)

    # try to fetch a response
    response = requests.delete(url, verify=False)

    print response.text


# contact the remote xlr server and grab the list of users
delete_users_list = filter_user(get_user_list())

for u in delete_users_list:
    delete_user(u['username'])

blah
# filter the list for exempt users

# loop over the filtered list to remove all users


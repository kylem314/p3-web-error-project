import requests

# borrow these definitions from model
from model import print_tester, url_prefix


# play with api on localhost, server must be running
def api_tester():


    # loop through each test condition and provide feedback
    for test in tests:
        print()
        print(f"({test[METHOD]}, {test[API]})")
        email = test[API].split("/")
        if test[METHOD] == 'get':
            response = requests.get(url + test[API])
        elif test[METHOD] == 'post':
            response = requests.post(url + test[API])
        elif test[METHOD] == 'put':
            response = requests.put(url + test[API])
        elif test[METHOD] == 'delete':
            response = requests.delete(url + test[API])
        else:
            print("unknown RESTapi method")
            continue

        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")


if __name__ == "__main__":
    api_tester()  # validates api's requires server to be running
    print_tester()
import requests,os
import datetime
import json






def creatNewTest(password) :

    url = "http://ec2-52-207-31-119.compute-1.amazonaws.com/start_new_test"
    users_fd = open("users_list.txt",'r')
    #data_base_size = os.path.getsize("users_list.txt")
    #users_list = users_fd.read(data_base_size)
    users_list = json.load(users_fd)
    print(users_list)
    response = requests.post(url,json=users_list)
    print(response.text)
    return
    creatNewTest()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    password = "1111"
    creatNewTest(password)


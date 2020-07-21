import pymongo


data = {"email":"shyam@gmail.com","password":"mychanged"}

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["expense_db"]
mycol = mydb["users"]
res=""
for i in mycol.find():
    if 'email' in i:
        if i['email']==data['email']:
            i['password']=data['password']
            print(i)
            res="success"
            break
        else:
            res="fail"
    else:
        res="fail"

print("res",res)
# input_username = data['username']
# input_password = data['password']
# print("username=>",input_username)
# print("pass=>",input_password)
# auth = ""
# ## validation
# for i in mycol.find():
#     # print(i['username'])
#     if input_username == i['username']:
#         # print("i['username']==>",i['username'])
#         if input_password == i['password']:
#             # print("i[password]==>",i['password'])
#             auth = "success"
#             break
#         else:
#             auth = "fail"
#             #break
#     else:
#         auth = "fail"
#         #break
#
# # print(auth)
#
# con_dict = {"authentication": auth}
# return HttpResponse(auth)
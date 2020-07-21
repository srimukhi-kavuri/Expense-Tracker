import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from django.core.mail import EmailMultiAlternatives
import math, random
import pymongo

mongo_conn = pymongo.MongoClient()
# db = mongo_conn[db_name["data_base"]]
from django.http import HttpResponse

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["expense_db"]





@csrf_exempt
def add_user_details(request):
    #import pdb
    #pdb.set_trace()
    #print("para",request.GET.get('name'))
    #print("data==",request.parser_context['kwargs']['name'])
    #print("request para request.POST==",request.POST)
    #print("request para==",request.GET)
    
    
    data = JSONParser().parse(request)
    print("Final Data=>", data)
    # data = JSONParser().parse(request)
    # mydict = {"name": "John", "address": "Highway 37"}
    mycol = mydb["users"]

    exist_user=""
    #### checking for duplicate user using email
    my_col = mydb['users']
    for i in my_col.find():
        print("ii==>", i)
        if data['email'] == i['email']:
            print("User is already exists")
            exist_user="True"
            break
        else:
            exist_user="False"

    if exist_user=="False":
        mycol.insert_one(data)

        con_dict = {"message": "User Created Successfully"}

    else:
        con_dict = {"message": f"Unable to create a user {data['email']} is already exists"}
    # import json
    # out=json.dumps(con_dict)
    # out1=json.loads(out)
    # print("con dic",type(con_dict))
    # print("out=>", type(out))
    # print("out1=>", type(out1))
    return JsonResponse(con_dict, safe=False)

@csrf_exempt
def add_income_details(request):
    data = JSONParser().parse(request)
    # mydict = {"name": "John", "address": "Highway 37"}
    mycol = mydb["income"]
    mycol.insert_one(data)

    con_dict = {"message": "Your income added Successfully"}
    return JsonResponse(con_dict, safe=False)


@csrf_exempt
def add_expense_details(request):
    data = JSONParser().parse(request)
    # mydict = {"name": "John", "address": "Highway 37"}
    mycol = mydb["expense"]
    mycol.insert_one(data)

    con_dict = {"message": "Your expense details added Successfully"}
    return JsonResponse(con_dict, safe=False)


###########################
### login validation######
### login validation######
@csrf_exempt
def user_validation(request):
    #import pdb
    #pdb.set_trace()
    data = JSONParser().parse(request)

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["expense_db"]
    mycol = mydb["users"]

    input_username = data['email']
    input_password = data['password']
    print("username=>",input_username)
    print("pass=>",input_password)
    auth = ""
    username=""
    email=""
    ## validation
    for i in mycol.find():
        # print(i['username'])
        if input_username == i['email']:
            # print("i['username']==>",i['username'])
            if input_password == i['password']:
                # print("i[password]==>",i['password'])
                auth = "success"
                username=i['name']
                email=i['email']
                break
            else:
                auth = "fail"
                #break
        else:
            auth = "fail"
            #break

    # print(auth)

    con_dict = {"username":username,"email":email, "authentication": auth}
    return JsonResponse(con_dict, safe=False)
    #return HttpResponse(con_dict)




###################################
#### Send OTP 2 factor Authentication###########
import requests

@csrf_exempt
def send_otp_to_email(request):
    ##############################SEND OTP TO EMAIL ################3
    
    data = JSONParser().parse(request)
    import email, smtplib, ssl

    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from os import path

    ##################################################### OTP NO GENERATOR ####+++++++++++++++++++++++++++++++++++++++++++++++
    import random as r
    otp = ""
    for i in range(4):
        otp += str(r.randint(1, 9))
    # print("Your One Time Password is ")
    # print(otp)
    #############

    subject = "OTP"
    body = "Your OTP is: {0}".format(otp)

    ################################################## MAIL SENDING#################
    
    sender_email = "mydemoproject.2020@gmail.com"
    receiver_email = data['email']
    password = "Test@123"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

    ######################################################### OTP VERIFICATION ###################
    ######## SAVE OTP #############
    import pymongo
    mongo_conn = pymongo.MongoClient()
    db = mongo_conn["expense_db"]
    col = db["otp"]
    col.update_one({"ID": "admin"}, {"$set": {"otp_data": otp}})
    #data = col.find({"ID": "admin"})

    data_item={"message": "OTP has sent on your email id" }

    return JsonResponse(data_item,safe=False)




####### Validation of OTP from email/ ################
from django.http import HttpResponse
@csrf_exempt
def my_otp_match(request):
    data = JSONParser().parse(request)
    enterted_otp=data['otp']

    #user_input = input("Enter your OTP")

    import pymongo
    mongo_conn = pymongo.MongoClient()
    db = mongo_conn["expense_db"]
    col = db["otp"]
    data = col.find({"ID": "admin"})
    db_otp = [i['otp_data'] for i in data]
    #user_input = input("Enter your otp")
    output=[]
    if enterted_otp == db_otp[0]:
        data_item = {
            "value": "success"
            
        }
        #output.append(output1)
    else:
        data_item = {
                "value": "fail"
        }
        #output.append(output1)
    return JsonResponse(data_item, safe=False)








########################### #######################

################################# ######################
#### Retrive all expenses###
##To show on table

from django.http import HttpResponse
@csrf_exempt
def display_table_data(request):
    data = JSONParser().parse(request)
    print("data",data)
    import pymongo
    current_user=data['email']
    #email = 'acm15aug@gmail.com'
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["expense_db"]
    my_col = mydb['expense']

    my_data = my_col.find({"email": current_user},{'_id':0})
    final_display_list =[]
    for x1 in my_data:
        #print(type(x1))
        final_display_list.append(x1)

    print("final==>", final_display_list)
    # data_item = {
    #             "value": final_display_list
    #     }
        #output.append(output1)
    return JsonResponse(final_display_list,safe=False)


######## Total Expence Vs Income Graph######
@csrf_exempt
def total_exp_vs_income_graph(request):
    try:
        data = JSONParser().parse(request)
        print("data",data)
        import pymongo
        current_user=data['email']
       


        #### Total income till date###
        total_income_till_date = []
        my_col = mydb['income']
        my_data = my_col.find({"email": current_user}, {'_id': 0})
        for i in my_data:
            # print(i)
            total_income_till_date.append(int(i['amount']))

        print("total income till date==>", total_income_till_date)
        #### Total expense till date###
        total_expense_till_date = []
        my_col = mydb['expense']
        my_data = my_col.find({"email": current_user}, {'_id': 0})
        for i in my_data:
            # print(i)
            total_expense_till_date.append(int(i['amount']))

        print("total_expense_till_date==>", total_expense_till_date)

        Total_Income = sum(total_income_till_date)
        Total_Expense = sum(total_expense_till_date)
        print("Final result==>", "\nTotal_Income=", Total_Income, "\nTotal Expense=", Total_Expense)


        result=[{"key":'Total Budget',
                 "value":int(Total_Income)},
                {"key":'Total Expense',
                "value":int(Total_Expense)}]


    except Exception as e:
        print("My Exception is: ",e)
        result = [{"key":'Total Budget',
                 "value":int(0)},
                 {"key":'Total Expense',
                 "value":int(0)}]

    return JsonResponse(result,safe=False)


########## Final conclusion #####

@csrf_exempt
def total_exp_vs_income_conclusion(request):
    try:
        #import pdb
        #pdb.set_trace()
        data = JSONParser().parse(request)
        print("data",data)
        import pymongo
        current_user=data['email']
        


        #### Total income till date###
        total_income_till_date = []
        my_col = mydb['income']
        my_data = my_col.find({"email": current_user}, {'_id': 0})
        for i in my_data:
            # print(i)
            total_income_till_date.append(int(i['amount']))

        print("total income till date==>", total_income_till_date)
        #### Total expense till date###
        total_expense_till_date = []
        my_col = mydb['expense']
        my_data = my_col.find({"email": current_user}, {'_id': 0})
        for i in my_data:
            # print(i)
            total_expense_till_date.append(int(i['amount']))

        print("total_expense_till_date==>", total_expense_till_date)

        Total_Income = sum(total_income_till_date)
        Total_Expense = sum(total_expense_till_date)
        print("Final result==>", "\nTotal_Income=", Total_Income, "\nTotal Expense=", Total_Expense)



        ####### Conclusion Message #######
        grand_total = Total_Income - Total_Expense
        conclusion_message = ""
        if grand_total > 0:
            conclusion_message = "Your Expenditure is Good"
        if grand_total < 0:
            conclusion_message = "Your Expenditure is Over-budget "

        result={"Total_Income":int(Total_Income),
                "Total_Expense":int(Total_Expense),
                "message":conclusion_message}


    except Exception as e:
        print("My Exception is: ",e)
        result = {"Total_Income":int(0),
                  "Total_Expense":int(0)}


    return JsonResponse(result,safe=False)




################################################## UPDATED NEW##############
######### Categariy wise report  (sending to email)
######## Monthly report (done)
######## Forgot password (done)
#### Budget table

##### Monthly report###
################## GET MONTHLY EXPENSE DETAILS ############
@csrf_exempt
def monthly_expense_userwise(request):
   
    # user_month = 'July'
    data = JSONParser().parse(request)
    current_user = data['email']
    user_month = data['month']
    ########## collect data month wise combine price by month####
    out=""
    # import pdb
    # pdb.set_trace()
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/')
    db = client.expense_db
    col = db['expense']
    user_data = col.find({"email": current_user}, {'_id': 0})
    # months={"Jan":1,"Feb":2,"March":3,"April":4,"May":5,"June":6,"July":7}
    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
              9: "September", 10: "October", 11: "November", 12: "December"}

    January, February, March, April, May, June, July, August, September, October, November, December = [], [], [], [], [], [], [], [], [], [], [], []

    for i in user_data:
        # print(i)
        import datetime
        expense_date = datetime.datetime.strptime(i['date'], "%Y-%m-%d")
        db_month_name = months[expense_date.month]
        # print("db_month_name==>",db_month_name)
        if db_month_name == 'January':
            January.append(i)
        if db_month_name == 'February':
            February.append(i)
        if db_month_name == 'March':
            March.append(i)
        if db_month_name == 'April':
            April.append(i)
        if db_month_name == 'May':
            May.append(i)
        if db_month_name == 'June':
            June.append(i)
        if db_month_name == 'July':
            July.append(i)
        if db_month_name == 'August':
            August.append(i)
        if db_month_name == 'September':
            September.append(i)
        if db_month_name == 'October':
            October.append(i)
        if db_month_name == 'November':
            November.append(i)
        if db_month_name == 'December':
            December.append(i)


    if user_month == 'January':
        print("Jan Month Data", January)
        return JsonResponse(January, safe=False)
    if user_month == 'February':
        print("February Month Data", February)
        return JsonResponse(February, safe=False)
    if user_month == 'March':
        print("March Month Data", March)
        return JsonResponse(March, safe=False)
    if user_month == 'April':
        print("April Month Data", April)
        return JsonResponse(April, safe=False)
    if user_month == 'May':
        print("May Month Data", May)
        return JsonResponse(May, safe=False)
    if user_month == 'June':
        print("June Month Data", June)
        return JsonResponse(June, safe=False)
    if user_month == 'July':
        print("July Month Data", July)
        return JsonResponse(July, safe=False)
    if user_month == 'August':
        print("August Month Data", August)
        return JsonResponse(August, safe=False)
    if user_month == 'September':
        print("September Month Data", September)
        return JsonResponse(September, safe=False)
    if user_month == 'October':
        print("October Month Data", October)
        return JsonResponse(October, safe=False)
    if user_month == 'November':
        print("November Month Data", November)
        return JsonResponse(November, safe=False)
    if user_month == 'December':
        print("December Month Data", December)
        return JsonResponse(December, safe=False)



#############################
######## Forgot password
################
###1.Verify_email for Forgot & if verified send OTP

@csrf_exempt
def verify_email_for_forgot_pass(request):
    #import pdb
    #pdb.set_trace()
    data = JSONParser().parse(request)
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/')
    db = client['expense_db']
    col = db['users']

    ### Input
    #email = "test@gmail.com"
    email=data['email']
    ########
    exist_count = col.find({"email": email}, {'_id': 0}).count()
    res={}
    if exist_count >= 1:
        print("Field value is present")
        res['verify']="success"


        ############# OTP Sending to verified email
        import email, smtplib, ssl

        from email import encoders
        from email.mime.base import MIMEBase
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from os import path

        ##################################################### OTP NO GENERATOR ####+++++++++++++++++++++++++++++++++++++++++++++++
        import random as r
        otp = ""
        for i in range(4):
            otp += str(r.randint(1, 9))
        # print("Your One Time Password is ")
        # print(otp)
        #############

        subject = "OTP"
        body = "Your OTP for forgot password request is: {0}".format(otp)

        ################################################## MAIL SENDING#################

        sender_email = "mydemoproject.2020@gmail.com"
        receiver_email = data['email']
        password = "Test@123"

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  # Recommended for mass emails

        message.attach(MIMEText(body, "plain"))

        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)

        ######################################################### OTP VERIFICATION ###################
        ######## SAVE OTP #############
        import pymongo
        mongo_conn = pymongo.MongoClient()
        db = mongo_conn["expense_db"]
        col = db["otp_forgot_pass"]
        col.update_one({"ID": "admin_forgot"}, {"$set": {"forgot_otp_data": otp}})
        # data = col.find({"ID": "admin"})

        #data_item = {"message": "OTP has sent on your email id"}
        res['message']="OTP has sent on your email id"
        ############# END OTP


    else:
        print("Field value is not present")
        res['verify']="fail"
    print(res)
    return JsonResponse(res, safe=False)

########2.Verify OTP for forgot Password
@csrf_exempt
def verify_otp_forgot_password(request):
    data = JSONParser().parse(request)
    enterted_otp=data['otp']

    #user_input = input("Enter your OTP")

    import pymongo
    mongo_conn = pymongo.MongoClient()
    db = mongo_conn["expense_db"]
    col = db["otp_forgot_pass"]
    data = col.find({"ID": "admin_forgot"})
    db_otp = [i['forgot_otp_data'] for i in data]
    #user_input = input("Enter your otp")
    output=[]
    if enterted_otp == db_otp[0]:
        data_item = {
            "verify":"success",
            "message": """OTP has been verified"""
        }
        #output.append(output1)
    else:
        data_item = {
                "verify": "fail",
                "value": """You have entered wrong OTP"""
        }
        #output.append(output1)
    return JsonResponse(data_item, safe=False)


####4. Update Password
@csrf_exempt
def update_password(request):
    data = JSONParser().parse(request)
    user_email=data['email']
    enterted_password=data['password']

    #user_input = input("Enter your OTP")

    import pymongo
    mongo_conn = pymongo.MongoClient()
    db = mongo_conn["expense_db"]
    col = db["users"]

    col.update_one({"email": user_email}, {"$set": {"password": enterted_password}})

    res={"message":"Your password has been successfully Updated"}

    return JsonResponse(res, safe=False)


######### Budget table
@csrf_exempt
def display_budget_table(request):
    #import pdb
    #pdb.set_trace()
    data = JSONParser().parse(request)
    user_email=data['email']

    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/')
    db = client['expense_db']
    col = db['income']

    ### Input
    # email = "test@gmail.com"
    #email = data['email']
    ########
    out_buget=[]
    db_data = col.find({"email": user_email}, {'_id': 0})

    for i in db_data:
        out_buget.append(i)

    return JsonResponse(out_buget, safe=False)

####### Send a report to mail

import requests

@csrf_exempt
def send_report_to_email_updated(request):
    ##############################SEND TO EMAIL ################3

    data = JSONParser().parse(request)
    import email, smtplib, ssl

    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from os import path

    ##################################################### report GENERATOR ####+++++++++++++++++++++++++++++++++++++++++++++++
    url="http://ec2-13-58-231-37.us-east-2.compute.amazonaws.com:8002/exp_app/total_exp_vs_income_conclusion/"
    response = requests.post(url, data=data)
    report_data=response.json()


    # #############
    print("REport DATA==>",report_data,type(report_data))
    all_report_data=""
    #for x in report_data:
    for k,v in report_data.items():
            all_report_data+=k+" :"+" "+str(v)+"\n"

    subject = "Expense Report"
    body = "Hi,\n Please find the following details for your Expense report:\n {0}".format(all_report_data)

    ################################################## MAIL SENDING#################

    sender_email = "mydemoproject.2020@gmail.com"
    receiver_email = data['email']
    password = "Test@123"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  #

    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)



    data_item=[{
       'type': 'text',
       'sequence': '',
       "value": "Report has been sent on your email ID"

    }]
    return JsonResponse(data_item,safe=False)







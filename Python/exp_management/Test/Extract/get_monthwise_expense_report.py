from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.expense_db
data=db.expense
jan=[]
feb=[]
march=[]
april=[]
may=[]
june=[]
july=[]
aug=[]
sep=[]
oct=[]
nov=[]
dec=[]
for i in data.find():
    date=i['date']
    #date = "2020-04-13"
    import datetime
    datee = datetime.datetime.strptime(date, "%Y-%m-%d")
    #print(type(datee.month),datee)
    if datee.month==1:
        jan.append(i)
    if datee.month==2:
        feb.append(i)
    if datee.month==3:
        march.append(i)
    if datee.month==4:
        april.append(i)
    if datee.month==5:
        may.append(i)
    if datee.month==6:
        june.append(i)
    if datee.month==7:
        july.append(i)
    if datee.month==8:
        aug.append(i)
    if datee==9:
        sep.append(i)
    if datee.month==10:
        oct.append(i)
    if datee.month==11:
        nov.append(i)
    if datee.month==12:
        dec.append(i)

# print("JAN==",jan)
# print("FEB==",feb)
# print("APRIL==",april)




# [
#     {
#         "category": "medical",
#         "value": 5001
#     },
#     {
#         "category": "shopping",
#         "value": 0
#     },
#     {
#         "category": "entertainment",
#         "value": 0
#     },
#     {
#         "category": "investment",
#         "value": 0
#     },
#     {
#         "category": "food",
#         "value": 1200
#     },
#     {
#         "category": "rent",
#         "value": 7000
#     },
#     {
#         "category": "etc",
#         "value": 1000
#     }
# ]
data=[]
all_month=[]
all_month.append(jan)
all_month.append(feb)
all_month.append(march)
all_month.append(april)
all_month.append(march)
all_month.append(may)
all_month.append(june)
all_month.append(july)
all_month.append(aug)
all_month.append(sep)
all_month.append(oct)
all_month.append(nov)
all_month.append(dec)

#print("all month==>",all_month)

months={0:"Jan",1:"Feb",2:"March",3:"April",4:"May",5:"June", 6:"July", 7:"Aug", 8:"Sep",9:"Oct", 10:"Nov", 11:"Dec"}

#print(months[0])

for d,x in enumerate(all_month):
    #print(d)
    #print(x)
    for i in x:
        # import pdb
        # pdb.set_trace()
        total_medical_expense = []  # total medical expense
        total_shopping_expense = []  # shopping
        total_entertainment_expense = []  # entertainment
        total_investment_expense = []
        total_food_expense = []
        total_rent_expense = []
        total_etc_expense = []

        if i['category'] == 'medical':
            total_medical_expense.append(int(i['price']))
        if i['category'] == 'shopping':
            total_shopping_expense.append(int(i['price']))
        if i['category'] == 'entertainment':
            total_entertainment_expense.append(int(i['price']))
        if i['category'] == 'investment':
            total_investment_expense.append(int(i['price']))
        if i['category'] == 'food':
            total_food_expense.append(int(i['price']))
        if i['category'] == 'rent':
            total_rent_expense.append(int(i['price']))
        if i['category'] == 'etc':
            total_etc_expense.append(int(i['price']))

        #print("===>",total_food_expense)
        if len(total_food_expense)>0:
            final = {}
            final['category']="Food"
            final['value']=sum(total_food_expense)
            final['month']=months[d]
            data.append(final)
            #print("data===>",data)
        if len(total_medical_expense)>0: # = []  # total medical expense
            final = {}
            final['category'] = "Medical"
            final['value'] = sum(total_medical_expense)
            final['month'] = months[d]
            data.append(final)
        if len(total_shopping_expense)>0: # = []  # total medical expense
            final = {}
            final['category'] = "Shopping"
            final['value'] = sum(total_shopping_expense)
            final['month'] = months[d]
            data.append(final)
        if len(total_entertainment_expense)>0:
            final = {}
            final['category'] = "Entertainment"
            final['value'] = sum(total_entertainment_expense)
            final['month'] = months[d]
            data.append(final)
        if len(total_investment_expense)>0:
            final = {}
            final['category'] = "Investment"
            final['value'] = sum(total_investment_expense)
            final['month'] = months[d]
            data.append(final)
        #print("before going data===>", data)
        if len(total_rent_expense)>0:
            final = {}
            # import pdb
            # pdb.set_trace()
            #print("INSIDE IF going data===>", data)
            final['category'] = "Rent"
            final['value'] = sum(total_rent_expense)
            final['month'] = months[d]
            #print("before rent data===>", data)
            data.append(final)
            #print("after rent data===>", data)

        if len(total_etc_expense)>0:
            final = {}
            final['category'] = "etc"
            final['value'] = sum(total_etc_expense)
            final['month'] = months[d]
            data.append(final)

############





res=[]
# print(final)
# res.append(final)
# print(res)
print(data)
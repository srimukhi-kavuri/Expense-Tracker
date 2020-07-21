import pymongo


#data = {"email":"shyam@gmail.com","password":"mychanged"}

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["expense_db"]
mycol = mydb["income"]
income_amount=[]
for i in mycol.find():
   if 'amount' in i:
       income_amount.append(i['amount'])

print("Total Income==>",income_amount)

expense_amount=[]

mycol2=mydb["expense"]

for x in mycol2.find():
    if "price" in x:
        #print(x['price'])
        expense_amount.append(x['price'])

print("Total expense==>",expense_amount)

total_income_amount=sum(income_amount)
total_expense_amount=sum(expense_amount)
total=total_income_amount-total_expense_amount
Financial_details={"Total Income Amount: ":total_income_amount,
                   "Total Expense Amount: ":total_expense_amount,
                   "Remaining Total":total}

print(Financial_details)
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
total_medical_expense=[] #total medical expense
total_shopping_expense=[] #shopping
total_entertainment_expense=[]#entertainment
total_investment_expense=[]
total_food_expense=[]
total_rent_expense=[]
total_etc_expense=[]
with client:
    db = client.expense_db
    data=db.expense
    for i in data.find():
        #print(i)
        if i['category']=='medical':
            total_medical_expense.append(i['price'])
        if i['category']=='shopping':
            total_shopping_expense.append(i['price'])
        if i['category']=='entertainment':
            total_shopping_expense.append(i['price'])
        if i['category']=='investment':
            total_shopping_expense.append(i['price'])
        if i['category']=='food':
            total_shopping_expense.append(i['price'])
        if i['category']=='rent':
            total_shopping_expense.append(i['price'])
        if i['category'] =='etc':
            total_shopping_expense.append(i['price'])


Medical_Expense_Total=sum(total_medical_expense)
Shopping_Expense_Total=sum(total_shopping_expense)
Entertainemt_Expense_Total=sum(total_entertainment_expense)
Investment_Expense_Total=sum(total_investment_expense)
Food_Expense_Total=sum(total_food_expense)
Rent_Expense_Total=sum(total_rent_expense)
ETC_Expense_Total=sum(total_etc_expense)

final_category_total={}
final_category_total['medical']=Medical_Expense_Total
final_category_total['shopping']=Shopping_Expense_Total
final_category_total['entertainment']=Entertainemt_Expense_Total
final_category_total['investment']=Investment_Expense_Total
final_category_total['food']=Food_Expense_Total
final_category_total['rent']=Rent_Expense_Total
final_category_total['etc']=ETC_Expense_Total
final_list=[]
for k,v in final_category_total.items():
    my_dict = {}
    my_dict['category']=k
    my_dict['value']=v
    final_list.append(my_dict)

print(final_category_total)
print(final_list)

data=[
    {
        "category": "medical",
        "value": 0
    },
    {
        "category": "shopping",
        "value": 8000
    },
    {
        "category": "entertainment",
        "value": 1500
    },
    {
        "category": "investment",
        "value": 4000
    },
    {
        "category": "food",
        "value": 1500
    },
    {
        "category": "rent",
        "value": 22000
    },
    {
        "category": "etc",
        "value": 100
    }
]


print(data)
all_report_data=""
for i in data:
    all_report_data+=i['category'].title()+" : "+str(i['value'])+"\n"

print(all_report_data)
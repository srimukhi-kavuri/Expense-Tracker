report_data=[{'category': 'medical', 'value': 601}, {'category': 'shopping', 'value': 402}, {'category': 'entertainment', 'value'
: 0}, {'category': 'investment', 'value': 0}, {'category': 'food', 'value': 1400}, {'category': 'rent', 'value': 7500}, {'category':
 'etc', 'value': 0}]
all_report_data=""
for x in report_data:
    for k,v in x.items():
        all_report_data += k + " :" + " " + str(v) + "₹" + "\n"


print(all_report_data)
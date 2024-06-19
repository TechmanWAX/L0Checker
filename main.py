# layerZero checker
import requests
import csv


url = 'https://www.layerzero.foundation/api/allocation/'
accounts_file = 'myaccs.csv'

with open(accounts_file) as accs:
    reader = csv.reader(accs)
    summ = 0
    for row in reader:
        response = requests.get(url + row[0])
        if response.status_code == 200:
            data = response.json()
            # print(data)
            if data['isEligible']:
                address = data['address']
                allo = data['zroAllocation']['asString']
                summ += float(allo)
                print(f'{address=}\t{allo=}')
print(f'{summ=}')
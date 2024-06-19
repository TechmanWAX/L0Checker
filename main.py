# layerZero checker
import requests
import csv
from random import randint


url = 'https://www.layerzero.foundation/api/allocation/'
# store wallets. One wallet address per line
accounts_file = 'myaccs.csv'
# store eligible wallets. One wallet address per line
valid_file = 'valid.csv'
# store proxies in format
# username:password@ip:port
# user:pass@10.12.13.14:8080
proxies_file = 'proxies.csv'
proxies_list = []

try:
    with open(proxies_file) as pf:
        for proxy in pf:
            proxies_list.append(proxy.strip())
except:
    print(f'Can\'t open {proxies_file} file')

with open(accounts_file) as accs:
    reader = csv.reader(accs)
    summ = 0
    valid = []
    for row in reader:
        proxies = {'https': f'http://{proxies_list[randint(0, len(proxies_list) - 1)]}'}
        response = requests.get(url + row[0], proxies=proxies)
        if response.status_code == 200:
            data = response.json()
            if data['isEligible']:
                address = data['address']
                valid.append(address)
                allo = data['zroAllocation']['asString']
                summ += float(allo)
                print(f'{address=}\t{allo=}')
print(f'{summ=}')

with open(valid_file, 'w') as val:
    writer = csv.writer(val)
    for row in valid:
        writer.writerow([row])

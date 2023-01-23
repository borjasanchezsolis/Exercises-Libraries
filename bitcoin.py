import sys
import requests


if len(sys.argv) == 2:
    try: 
        value = float(sys.argv[1]) 
    except:
        print('Command line argument is not a number')
        sys.exit(1)
else: 
    print('Missing command line argument')
    sys.exit(1)

try:
    price_list = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = price_list.json()
    bitcoin = response['bpi']['EUR']['rate_float']
    print(f'{(bitcoin * value):,.4f}€')

except requests.RequestException:
    print('Request Exception')
    sys.exit(1)
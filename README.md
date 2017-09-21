# shapeshift.io-python-api
Python REST API implementation for Shapeshift.io

## Installation 
The library is designed to run with Python 3.

First install requests package with pip install requests

Documentation for the API and more details on the api arguments can be found in this link https://info.shapeshift.io/api

## Usage
```python
s = Shapeshift() # create api object

s.rate(btc_ltc) # api call get the current rate offered by Shapeshift.
# { 'pair': 'btc_ltc', 'rate': '74.65621067'}
```

```pyhon
s.getcoins() # api call return all the available coins in Shapeshift

# {'ETH': {     'image': 'https://shapeshift.io/images/coins/ether.png',
                'imageSmall': 'https://shapeshift.io/images/coins-sm/ether.png',
                'name': 'Ether',
                'status': 'available',
                'symbol': 'ETH'},
                 ...
               ...
             ...}
```

## Available API Endpoints
###  GET Methods
* Rate - rate/
* Deposit Limit - limit/
* Market Info - marktetinfo/
* Recent Transcation List - recenttx/
* Status of deposit to address - txStat/
* Time Remaining of Fixed Amount Transaction - timeremaining/
* Get List of Supported Coins with Icon Links - getcoins/
* Get List of Transactions with a PRIVATE API KEY - txbyapikey/
* Get List of Transactions with a Specific Output Address - txbyaddress/
* Validate an address, given a currency symbol and address - validateaddress/


### POST Methods
* Normal Transaction - shift/

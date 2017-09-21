# shapeshift.io-python-api
Python REST API implementation for Shapeshift.io

## Installation 
the library is designed to run with Python 3, first install requests package e.g pip install requests

## Usage
```python
s = Shapeshift() # create api object

s.rate(btc_ltc) 
# { 'pair': 'btc_ltc', 'rate': '74.65621067'}
```

```pyhon
s.getcoins() # api call return all the available coins in Shapeshift
#'ETH': {      'image': 'https://shapeshift.io/images/coins/ether.png',
               'imageSmall': 'https://shapeshift.io/images/coins-sm/ether.png',
               'name': 'Ether',
               'status': 'available',
               'symbol': 'ETH'},
                ...
              ...
            ...

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

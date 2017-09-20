# shapeshift.io-python-api
Python REST API implementation for Shapeshift.io

# Installation 
the library is designed to run with Python 3, first install requests package e.g pip install requests

# Usage
```ruby
s = Shapeshift() # create api object
s.getcoins() # api call return all the available coins in Shapeshift
s.rate(btc_ltc) 
```
Returns


{ 'pair': 'btc_ltc',
  'rate': '74.65621067'}

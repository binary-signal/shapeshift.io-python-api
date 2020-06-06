"""
Shapeshift API Python
EvanM / September 21 2017
"""

import json
import requests


class ShapeShift:
    def __init__(self):
        self.baseurl = "https://shapeshift.io/"
        self.api_doc = "https://info.shapeshift.io/api/"

    def __str__(self):
        return "Python implementation for Shapeshift.io \n" \
               "Documentation can be found here: {}" \
               " \nVersion 1 ".format(self.api_doc)

    def __get(self, url, param):  # Get Request (Low Level API call)
        page = requests.get(url, param)
        return page.text

    def __post(self, url, param):  # Post Request (Low Level API call)
        page = requests.post(url, data=param)
        return page.text

    def __apicall_get(self, endpoint, param={}, arg=''):
        url = self.baseurl + "{}".format(endpoint)
        if arg != '':
            url = url + "{}/".format(arg)
        answer = self.__get(url, param)
        return json.loads(answer)

    def __api_call_post(self, endpoint, param={}, arg=''):
        url = self.baseurl + "{}".format(endpoint)
        if arg != '':
            url = url + "{}/".format(arg)
        answer = self.__post(url, param)
        return json.loads(answer)

    def rate(self, pair):
        """
        Gets the current rate offered by Shapeshift. This is an estimate because the rate can
        occasionally change rapidly depending on the markets. The rate is also a 'use-able' rate
        not a direct market rate. Meaning multiplying your input coin amount times the rate should
        give you a close approximation of what will be sent out. This rate does not include the
        transaction (miner) fee taken off every transaction.

        :param pair: is any valid coin pair such as btc_ltc or ltc_btc
        :return: json object


        url: shapeshift.io/limit/[pair]
        method: GET

        """
        return self.__apicall_get(endpoint='limit', param={}, arg=pair)

    def marketinfo(self, pair=''):
        """
        This gets the market info (pair, rate, limit, minimum limit, miner fee)

        :param pair: (OPTIONAL) is any valid coin pair such as btc_ltc or ltc_btc.
        The pair is not required and if not specified will return an array of all market infos.
        :return: json object

        url: shapeshift.io/marketinfo/[pair]
        method: GET
        """

        return self.__apicall_get(endpoint='marketinfo', param={}, arg=pair)

    def recenttx(self, maxtx=5):
        """
        Get a list of the most recent transactions.

        :param maxtx: is an optional maximum number of transactions to return. If [maxtx] is not
        specified this will return 5 transactions.Also, [maxtx] must be a number between 1
        and 50 (inclusive).
        :return: json object

        url: shapeshift.io/recenttx/[maxtx]
        method: GET
        """
        if maxtx > 50:
            raise ValueError('error maxtx over 50')
        return self.__apicall_get(endpoint='recenttx', param={}, arg=str(maxtx))

    def txstat(self, address):
        """
        This returns the status of the most recent deposit transaction to the address.

        :param address: is the deposit address to look up
        :return: (various depending on status)

        url: shapeshift.io/txStat/[address]
        method: GET
        """
        return self.__apicall_get(endpoint='txstat', param={}, arg=address)

    def timeremaining(self, address):
        """
        When a transaction is created with a fixed amount requested there is a 10 minute window for
        the deposit. After the 10 minute window if the deposit has not been received the transaction
        expires and a new one must be created. This api call returns how many seconds are left before
        the transaction expires. Please note that if the address is a ripple address, it will include
        the "?dt=destTagNUM" appended on the end, and you will need to use the URIEncodeComponent()
        function on the address before sending it in as a param, to get a successful response.
        If the status is expired then seconds_remaining will show 0.

        :param address: is the deposit address to look up
        :return: json object

        url: shapeshift.io/timeremaining/[address]
        method: GET
        """
        return self.__apicall_get(endpoint='timeremaining', param={}, arg=address)

    def onlinecoins(self):
        """
        This endpoint will return the ticker of all available coins.
        
        url: shapeshift.io/onlinecoins
        method: GET
        """
        return self.__apicall_get(endpoint="onlinecoins",param={})
    
    
    def offlinecoins(self):
        """
        This endpoint will return the ticker of all available coins.
        
        url: shapeshift.io/onlinecoins
        method: GET
        """
        return self.__apicall_get(endpoint="offlinecoins",param={})
    
    def validpairs(self):
        """
        This endpoint will return all valid coin pairs available on ShapeShift.
        """
        return self.__apicall_get(endpoint="validpairs",param={})
    
    def getcoins(self):
        """
        Allows anyone to get a list of all the currencies that Shapeshift currently supports at any
        given time. The list will include the name, symbol, availability status, and an icon link for
        each.
        :return: json object

        url: shapeshift.io/getcoins
        method: GET
        """
        return self.__apicall_get(endpoint='getcoins', param={})

    def txbyapikey(self, apikey):
        """
        Allows vendors to get a list of all transactions that have ever been done using a
        specific API key. Transactions are created with an affilliate PUBLIC KEY, but they
        are looked up using the linked PRIVATE KEY, to protect the privacy of our affiliates'
        account details.

        :param apikey: is the affiliate's PRIVATE api key.
        :return:

        url: shapeshift.io/txbyapikey/[apiKey]
        method: GET
        """
        return self.__apicall_get(endpoint='txbyapikey', param={}, arg=apikey)

    def txbyaddress(self, address, apikey):
        """
        Allows vendors to get a list of all transactions that have ever been sent to one of
        their addresses. The affilliate's PRIVATE KEY must be provided, and will only return
        transactions that were sent to output address AND were created using / linked to the
        affiliate's PUBLIC KEY. Please note that if the address is a ripple address and it
        includes the "?dt=destTagNUM" appended on the end, you will need to use the
        URIEncodeComponent() function on the address before sending it in as a param, to get
        a successful response.

        :param address: the address that output coin was sent to for the shift
        :param apikey:  is the affiliate's PRIVATE api key.

        :return: json object

        url: shapeshift.io/txbyaddress/[address]/[apiKey]
        method: GET
        """
        return self.__apicall_get(endpoint='txbyaddress', param={},
                                  arg="{}/{}".format(address, apikey))

    def validateaddress(self, address, coinSymbol):
        """
        Allows user to verify that their receiving address is a valid address according to a
        given wallet daemon. If isvalid returns true, this address is valid according to the
         coin daemon indicated by the currency symbol.

        :param address: the address that the user wishes to validate
        :param coinSymbol: the currency symbol of the coin
        :return: json object

        url: shapeshift.io/validateAddress/[address]/[coinSymbol]
        method: GET
        """
        return self.__apicall_get(endpoint='validateAddress', param={},
                                  arg="{}/{}".format(address, coinSymbol))

    # post requests
    def shift(self, withdrawal, pair, returnAddress=None,
              destTag=None, rsAddress=None, apiKey=None):
        """
        This is the primary data input into ShapeShift.

        :param withdrawal: the address for resulting coin to be sent to
        :param pair: what coins are being exchanged in the form [input coin]_[output coin]  ie btc_ltc
        :param returnAddress: (Optional) address to return deposit to if anything goes wrong with exchange
        :param destTag: (Optional) Destination tag that you want appended to a Ripple payment to you
        :param rsAddress: (Optional) For new NXT accounts to be funded, you supply this on NXT payment to you
        :param apiKey: (Optional) Your affiliate PUBLIC KEY, for volume tracking, affiliate payments, split-shifts, etc...
        :return: json object

        url:  shapeshift.io/shift
        method: POST
        data type: JSON

        example data: {"withdrawal":"AAAAAAAAAAAAA", "pair":"btc_ltc", returnAddress:"BBBBBBBBBBB"}
        """
        payload = {
            'withdrawal'   : withdrawal,
            'pair'         : pair,
            'returnAddress': returnAddress,
            'destTag'      : destTag,
            'rsAddress'    : rsAddress,
            'apiKey'       : apiKey}

        payload = {k: v for k, v in payload.items() if v is not None}  # filter empty values

        return self.__api_call_post(endpoint='shift', param=payload)

    def mail(self, email, txid):
        """
        This call requests a receipt for a transaction. The email address will be added to the
        conduit associated with that transaction as well. (Soon it will also send receipts to
        subsequent transactions on that conduit)

        :param email: the address for receipt email to be sent to
        :param txid: the transaction id of the transaction TO the user (ie the txid for the
                     withdrawal NOT the deposit)
        :return: json object

        url:  shapeshift.io/mail
        method: POST
        data type: JSON
        data required:

        example data {"email":"mail@example.com", "txid":"123ABC"}
        """
        payload = {
            'email': email,
            'txid' : txid}

        return self.__api_call_post(endpoint='mail', param=payload)

    def sendamount(self, amount, withdrawal, pair,
                   returnAddress=None, destTag=None, rsAddress=None,
                   apiKey=None):
        """
        This call allows you to request a fixed amount to be sent to the withdrawal address.
        You provide a withdrawal address and the amount you want sent to it. We return the amount
        to deposit and the address to deposit to. This allows you to use shapeshift as a payment
        mechanism. This call also allows you to request a quoted price on the amount of a
        transaction without a withdrawal address.

        :param amount: the amount to be sent to the withdrawal address
        :param withdrawal: the address for coin to be sent to
        :param pair: what coins are being exchanged in the form [input coin]_[output coin]
        ie ltc_btc
        :param returnAddress: (Optional) address to return deposit to if anything goes wrong with
        exchange
        :param destTag: (Optional) Destination tag that you want appended to a Ripple payment to you
        :param rsAddress: (Optional) For new NXT accounts to be funded, supply this on NXT payment
        to you
        :param apiKey: (Optional) Your affiliate PUBLIC KEY, for volume tracking, affiliate
        payments, split-shifts, etc...
        :return: json object

        url: shapeshift.io/sendamount
        method: POST
        data type: JSON

        //1. Send amount request
          Data required:
        example data {"amount":123, "withdrawal":"123ABC", "pair":"ltc_btc", returnAddress:"BBBBBBB"}

        //2. Quoted Price request
        //Note :  This request will only return information about a quoted rate
        //         This request will NOT generate the deposit address.

          Data required:

        amount  = the amount to be sent to the withdrawal address
        pair    = what coins are being exchanged in the form [input coin]_[output coin]  ie ltc_btc

        example data {"amount":123, "pair":"ltc_btc"}

        """
        payload = {
            'withdrawal'   : withdrawal,
            'pair'         : pair,
            'returnAddress': returnAddress,
            'destTag'      : destTag,
            'rsAddress'    : rsAddress,
            'apiKey'       : apiKey}

        payload = {k: v for k, v in payload.items() if v is not None}  # filter empty values

        return self.__api_call_post(endpoint='sendamount', param=payload)

    def cancelpending(self, adddress):
        """
        This call allows you to request for canceling a pending transaction by the deposit address.
        If there is fund sent to the deposit address, this pending transaction cannot be canceled.
        :param adddress: The deposit address associated with the pending transaction
        :return: json object

        url: shapeshift.io/cancelpending
        method: POST
        data type: JSON

        Example data : {address : "1HB5XMLmzFVj8ALj6mfBsbifRoD4miY36v"}
        """

        return self.__api_call_post(endpoint='cancelpending', param={'address': adddress})
    
    def orderinfo(self,order_id):
        """
        This endpoint will return information related to the Order ID in question, including status, withdraw address, deposit addresses, incoming coin, outgoing coin, all transaction hashes, all URLs, and time-based information.
        :param order_id: The order id returned in the response of a transaction
        :return: json object
        
        url: shapeshift.io/orderInfo/[order_id]
        method: GET 
        data type: JSON
        """
        
        return self.__api_call_post(endpoint='cancelpending', param={'address': adddress})

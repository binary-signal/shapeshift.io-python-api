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

    def __apicall(self, endpoint, param={}, arg=''):
        url = self.baseurl + "{}/".format(endpoint)
        if arg != '':
            url = url + "{}/".format(arg)
        answer = self.__get(url, param)
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


        url: shapeshift.io/rate/[pair]
        method: GET

        Success Output:

            {
                "pair" : "btc_ltc",
                "rate" : "70.1234"
            }
        """
        return self.__apicall(endpoint='rate', param={}, arg=pair)

    def limit(self, pair):
        """
        Gets the current deposit limit set by Shapeshift. Amounts deposited over this limit will be
        sent to the return address if one was entered, otherwise the user will need to contact
        ShapeShift support to retrieve their coins. This is an estimate because a sudden market swing
        could move the limit.

        :param pair: is any valid coin pair such as btc_ltc or ltc_btc
        :return: json object


        url: shapeshift.io/limit/[pair]
        method: GET

        Success Output:
            {
                "pair" : "btc_ltc",
                "limit" : "1.2345"
            }
        """

        return self.__apicall(endpoint='limit', param={}, arg=pair)

    def marketinfo(self, pair=''):
        """
        This gets the market info (pair, rate, limit, minimum limit, miner fee)

        :param pair: (OPTIONAL) is any valid coin pair such as btc_ltc or ltc_btc.
        The pair is not required and if not specified will return an array of all market infos.
        :return: json object

        url: shapeshift.io/marketinfo/[pair]
        method: GET

        Success Output:
            {
                "pair"     : "btc_ltc",
                "rate"     : 130.12345678,
                "limit"    : 1.2345,
                "min"      : 0.02621232,
                "minerFee" : 0.0001
            }
        """

        return self.__apicall(endpoint='marketinfo', param={}, arg=pair)

    def recenttx(self, maxtx=5):
        """
        Get a list of the most recent transactions.

        :param maxtx: is an optional maximum number of transactions to return.
                    If [maxtx] is not specified this will return 5 transactions.
                    Also, [maxtx] must be a number between 1 and 50 (inclusive).
        :return: json object
        url: shapeshift.io/recenttx/[max]
        method: GET

        Success Output:
            [
                {
                curIn : [currency input],
                curOut: [currency output],
                amount: [amount],
                timestamp: [time stamp]     //in seconds
                },
                ...
            ]
        """
        return self.__apicall(endpoint='recenttx', param={}, arg=str(maxtx))

    def tsStat(self, address):
        """
        This returns the status of the most recent deposit transaction to the address.

        :param address: is the deposit address to look up
        :return: (various depending on status)

        url: shapeshift.io/txStat/[address]
        method: GET

        Success Output:  (various depending on status)

        Status: No Deposits Received
            {
                status:"no_deposits",
                address:[address]           //matches address submitted
            }

        Status: Received (we see a new deposit but have not finished processing it)
            {
                status:"received",
                address:[address]           //matches address submitted
            }

        Status: Complete
        {
            status : "complete",
            address: [address],
            withdraw: [withdrawal address],
            incomingCoin: [amount deposited],
            incomingType: [coin type of deposit],
            outgoingCoin: [amount sent to withdrawal address],
            outgoingType: [coin type of withdrawal],
            transaction: [transaction id of coin sent to withdrawal address]
        }

        Status: Failed
        {
            status : "failed",
            error: [Text describing failure]
        }
        """
        return self.__apicall(endpoint='tsStat', param={}, arg=address)

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

        Success Output:

            {
                status:"pending",
                seconds_remaining: 600
            }

        The status can be either "pending" or "expired".
        If the status is expired then seconds_remaining will show 0.
        """
        return self.__apicall(endpoint='timeremaining', param={}, arg=address)

    def getcoins(self):
        """
        Allows anyone to get a list of all the currencies that Shapeshift currently supports at any
        given time. The list will include the name, symbol, availability status, and an icon link for
        each.
        :return: json object

        url: shapeshift.io/getcoins
        method: GET

        Success Output:

            {
                "SYMBOL1" :
                    {
                        name: ["Currency Formal Name"],
                        symbol: <"SYMBOL1">,
                        image: ["https://shapeshift.io/images/coins/coinName.png"],
                        status: [available / unavailable]
                    }
                (one listing per supported currency)
            }

        The status can be either "available" or "unavailable". Sometimes coins become temporarily unavailable during updates or
        unexpected service issues.
        """
        return self.__apicall(endpoint='getcoins', param={})


def txbyapikey(apikey):
    """

    :param apikey:
    :return:
    """
    pass


def txbyaddress(apikey, address):
    """

    :param apikey:
    :param address:
    :return:
    """
    pass


def validateaddress(address, coinSymbol):
    """

    :param address:
    :param coinSymbol:
    :return:
    """
    pass


# post requests
def shift(withdrawl, pair, returnAddress, destTag, rsAddress, apiKey):
    """

    :param withdrawl:
    :param pair:
    :param returnAddress:
    :param destTag:
    :param rsAddress:
    :param apiKey:
    :return:
    """
    pass


def mail(email, txid):
    """

    :param email:
    :param txid:
    :return:
    """
    pass


def sendamount(amount, withdrawlm, pair, returnAddress, destTag, rsAddress, apiKey):
    """

    :param amount:
    :param withdrawlm:
    :param pair:
    :param returnAddress:
    :param destTag:
    :param rsAddress:
    :param apiKey:
    :return:
    """
    pass


def cancelpending(adddress):
    """
    This call allows you to request for canceling a pending transaction by the deposit address.
    If there is fund sent to the deposit address, this pending transaction cannot be canceled.
    :param adddress:
    :return: json object
    """
    pass

ss = ShapeShift()
print(ss)
print("rate test")
pprint(ss.rate('btc_ltc'), width=1, indent=2)

# print("limit test")
# limit('btc_ltc')

# print("marketinsto test")
# marketinfo()

# print('recent transaction')
# recenttx()

# print('test tsStat')
# tsStat(address="")

# print('test timeremaining')
# timeremaining(address="")

#

pprint(ss.getcoins(), width=1, indent=20)
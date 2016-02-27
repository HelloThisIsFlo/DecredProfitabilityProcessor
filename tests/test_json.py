import json, urllib.request

def test_get_decred_market_price():
    data = urllib.request.urlopen("http://coinmarketcap-nexuist.rhcloud.com/api/dcr/price").read()
    output = json.loads(data.decode())
    print(float(output['eur']))
    assert True

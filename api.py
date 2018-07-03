import requests
import base64
from datetime import datetime
import hashlib
import json

access_token_path = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
consumer_key="GrMDfVCKLTq6POB6gi0VBGqm6doxrFCn"
consumer_secret="PUSL6g38YYaXhXGv"
response = requests.get(access_token_path, auth=("consumer_key", "consumer_secret")).text
res=json.loads(response)
access_token=res ['access_token']


url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = { "Authorization": "Bearer %s" % access_token }

BusinessShortCode=174379
passkey='bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
Timestamp=20180702153955
ps_wd = ('BusinessShortCode' + 'passkey' + 'Timestamp')
password = base64.b64encode(ps_wd.encode('utf=8'))



payload = {
  "BusinessShortCode": "174379",
  "Password": password,
  "Timestamp": "20180702153955",
  "TransactionType": "CustomerPayBillOnline",
  "Amount": "2",
  "PartyA": "254702838079",
  "PartyB": "174379",
  "PhoneNumber": "254702838079",
  "CallBackURL": "http://mpesa-requestbin.herokuapp.com/1der4d01",
  "AccountReference": "test",
  "TransactionDesc": "test"
  }

def get_access_token():
  url = self.api + self.access_token_path
  response = self.payload.get(url, auth=(self.consumer_key, self.consumer_secret))
  if response.status_code == 200:
    data = response.json()
    self.access_token = data['access_token']
    return self.access_token
  else:
    return None


response = requests.post(url, json = payload,headers=headers)

print (response.text)
import requests

access_token = "MwWYjM51oeNwUAtDtKXUCBEQT6ox"
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = { "Authorization": "Bearer %s" % access_token }
request = {
  "BusinessShortCode": "174379 ",
  "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTgwNzAyMTE1NDU1 ",
  "Timestamp": "20180702153955 ",
  "TransactionType": "CustomerPayBillOnline",
  "Amount": " 2"
  "PartyA": " 254702838079",
  "PartyB": " 174379",
  "PhoneNumber": "254702838079",
  "CallBackURL": "http://mpesa-requestbin.herokuapp.com/pufk94pu",
  "AccountReference": "fifi ",
  "TransactionDesc": "fifi "


response = requests.post(api_url, json = request, headers=headers)

print (response.text)



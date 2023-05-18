from twilio.rest import Client
import GoogleMap as Gm
import API
account_sid = API.tw_account_sid
auth_token = API.tw_auth_token
client = Client(account_sid,auth_token)


def sendEmergencyText(text):
    client.messages.create(
        body=text,
        from_='+XXXXXXXXX',
        to='+XXXXXXXXXX'
    )


def sendLocationOnPhone(location):
    client.messages.create(
        body="The Address Link is: " + Gm.search_location_in_city(location),
        from_='+XXXXXXXXXX',
        to='+XXXXXXXXXX'
    )

import requests, logging as log
from decouple import config
from requests.models import HTTPBasicAuth


API_KEY=config('API_KEY')
API_SECRET=config('API_SECRET')
URL=config('SANDBOX_URL')
SANDBOX_NUMBER=config('SANDBOX_VIRTUAL_PHONE_NUMBER')
def getdata(url,headers):
        try:
            data=requests.get(url,headers=headers)
            if (data.status_code==200):
                return data
            else:
                log.error("error connecting the Site")
                log.error("STATUS CODE:",data.status_code)
                log.error('GOT:', data.text)
                return data
        except Exception as e:
            ConnectionError(e)

def senddata(to_num,msg):
    auth=HTTPBasicAuth(API_KEY,API_SECRET)
    data={
    "from": { "type": "whatsapp", "number": SANDBOX_NUMBER },
    "to": { "type": "whatsapp", "number": to_num },
    "message": {
      "content": {
        "type": "text",
        "text": msg
      }
    }
    }
    try:
        data=requests.post(URL,auth=auth,json=data)
        log.info(data.json())
    except Exception as e:
        ConnectionError(e)
    return


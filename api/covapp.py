import logging as log
from flask import request
from api import functions, get_send
from datetime import date
from flask_restful import Resource
from decouple import config



class CovApp(Resource):
    reply_to_whatsApp=False 
    req_from_whatsApp_num=''
    def api(self,pincode='',date_search='',age_search=[18,45]):
        header={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        }
        if age_search:
            age_search=[age_search]
        else:
            age_search=[18,45]
        pincode = pincode if pincode !='' else '226010'
        date_search = date_search if date_search !='' else date.today().strftime('%d-%m-%Y')
        date_check =functions.checkdate(date_search)
        if not functions.ispincode(pincode):
            reply = "please enter a valid pincode (6 digits)"
            return reply
        if not date_check[0]:
            reply = date_check[1]
            return reply
        url=f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={pincode}&date={date_search}'
        res=get_send.getdata(url,headers=header)
        data=res.json()
        reply =''
        
        tab='  '
        for center in data['centers']:
            center_reply=''
            found_age=False
            center_reply += f"{center['name']} ({center['center_id']}) \n"
            for session in center['sessions']:
                if session['min_age_limit'] in age_search:
                    found_age= True
                    center_reply+=f"{tab}{session['available_capacity']} available for age {session['min_age_limit']}+ on {session['date']} \n"
                
            if found_age:
                reply+=center_reply       
                    
        return reply
    def get(self):
        return "NOT ALLOWED",403
    
    def post(self):
        
        note=''
        req_from_api=request.form.get("Body")
        try:
            req_from_wApp=request.get_json()['message']['content']['text']
        except:
            log. info('########################REQUEST NOT FROM WHATSAPP FOR SURE!!!!!!!')
        if req_from_api!=None:
            req=req_from_api
        elif req_from_wApp != None:
            req=req_from_wApp
            self.req_from_whatsApp_num=request.get_json()['from']['number']
            self.reply_to_whatsApp=True
        else:
            log.error("GOT A NULL REQUEST")
            return "WHAT THE HELL DID YOU SEND??",503

        req=req.split(',')
        if len(req) <2:
            reply="Should have at least one comma to separate pin & date. \n\nFormat: PIN, DATE(DD-MM-YYYY), AGE\n\nTo get this week's, all age group:\n  226001, \nGet specific date and age filter(18 OR 45):\n  226001,15-05-2021,18\n PIN & age filter:\n  226010,,18\n\n*NOTE:* Single comma will return this week's 226010 for all(TRY):\n  ,\n\n"
        else:
            pincode = req[0].strip()
            date_search=req[1].strip()
            try:
                age_filter=int(req[2].strip())
                if age_filter not in [18,45]:
                    log.info(f'WRONG AGE WAS SENT: {age_filter}')
                    age_filter=False
                    note="WRONG AGE: We know age is just a number. BUT acceptables age are 18 & 45. OR don't send age to get all slots.\nLet's see all!! \n\n"
                    if self.reply_to_whatsApp:
                        get_send.senddata(to_num=self.req_from_whatsApp_num,msg=note)
            except:
                age_filter=False
                note="No Age filter set. Let's see all!!\nTo filter age group, add one more comma and age.\nExample1: 226001,15-05-2021,18\n Example2:      ,,18\n\n"
                if self.reply_to_whatsApp:
                    get_send.senddata(to_num=self.req_from_whatsApp_num,msg=note)
            reply=self.api(pincode,date_search,age_filter)
        if reply:
            if self.reply_to_whatsApp:
                    get_send.senddata(to_num=self.req_from_whatsApp_num,msg=reply)
            reply=note+reply
            reply=reply.replace("\n","<br>")
            return reply,200
        else:
            reply="No Vaccination center is available for booking. Try some other Pincode or an earlier date"
            if self.reply_to_whatsApp:
                    get_send.senddata(to_num=self.req_from_whatsApp_num,msg=reply)
            reply=note+reply
            reply=reply.replace("\n","<br>")
            return reply,200

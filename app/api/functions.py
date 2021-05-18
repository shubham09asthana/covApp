#from datetime import date
import datetime
def ispincode(pin):
    if len(pin) != 6:
        return False
    if not pin.isnumeric():
        return False
    return True

def checkdate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d-%m-%Y')
      #  return True
    except ValueError:
        return [False,"Incorrect data format, should be DD-MM-YYYY"]

    dli=date_text.split('-')
    date1 = datetime.date(int(dli[2]),int(dli[1]),int(dli[0]))
    if date1 >=  datetime.date.today():
        return [True,"True"]
    else:
        return [False, "Date already passed"]


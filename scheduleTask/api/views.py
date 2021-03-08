from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import requests
import datetime

"""
    This is the ping endpoint view, 
    which returns status if the server is live.
"""
class PingView(View):
    def get(self,request):
        return JsonResponse({'status':'OK'})


"""
    This is the schedule view,which sends request to the URL appended to this endpoint,
    returns valid status if datetime matches with current datetime, if not then sends an error message.
"""
class ScheduleView(View):
    def get(self,request,date,url):
        DATE = date
        URL = url

        # formatting the datetime parameter on the endpoint by removing 'seconds' from timestamp
        requestDate = datetime.datetime.strptime(DATE.split('.')[0] ,'%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M')

        # formatting the current datetime by removing 'seconds' from timestamp so that it can be compared with requestDate
        currentDate = (datetime.datetime.utcnow()+datetime.timedelta(hours=5.5)).strftime('%Y-%m-%d %H:%M')

        if(requestDate == currentDate):
            data = requests.get(URL)
            status = data.status_code
            return JsonResponse({'status':status})
        else:
            errorMessage = 'Incorrect date or time'
            return JsonResponse({'error' : errorMessage})
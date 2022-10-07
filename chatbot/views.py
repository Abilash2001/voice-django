from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import random
# Create your views here.


class SearchEngine:
    qresponse = {
        ("hi","hello") : ("Hey, Thanks for visiting Voizfonica, How may I help you?","hello"),
        ("prepaid connection activated","postpaid connection activated","connection activated"): ("After you receive a new prepaid/postpaid SIM, it usually takes a few hours to get activated. Once your SIM is activated, you can enjoy all the benefits associated with your prepaid/postpaid plan.","testing")
    }
    def __init__(self) -> None:
        pass
    def find(self,message: str) -> str:
        pass

@csrf_exempt
def getResponse(request):
    if(request.method == "POST"):
        userMessage = request.POST.get('newchat')
        search = SearchEngine()
        return HttpResponse(userMessage)
    else:
        return HttpResponse("INVALID REQUEST")
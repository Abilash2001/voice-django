from re import L
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import random
# Create your views here.


class SearchEngine:
    qresponse = {
        ("hi","hello","hey") : ["Hey, Thanks for visiting Voizfonica, How may I help you?","hello","hey"],

        ("prepaid connection activate","postpaid connection activate","connection activate","sim activate"): ["After you receive a new prepaid/postpaid SIM, it usually takes a few hours to get activated. Once your SIM is activated, you can enjoy all the benefits associated with your prepaid/postpaid plan.","It often takes a few hours to get your new prepaid/postpaid SIM activated when you receive it. You can start taking use of all the perks of your prepaid/postpaid plan as soon as your SIM is enabled."],

        ("online sim activation","verification"): ["Dial 59059 to complete your tele-verification","To complete your tele-verification, dial 59059."],

        ("prepaid to postpaid","migrate"): ["Once request is made,it will take 5 hours to migrate from prepaid to postpaid ","After a request is submitted, switching from prepaid to postpaid will take five hours."],

        ("port sim","port","sim port"): ["To port mobile number online, visit the MNP page on the website and enter your area pin code and mobile number. Select a plan according to your needs and place an order to get SIM delivered to your doorstep free of cost.","Visit the MNP page on the website and enter your area pin code and mobile number to port your mobile number online. Choose a plan that suits your needs, then place an order to have a free SIM delivered to your door."],

        ("document proof","proof","verify"): ["It requires a valid Proof of Identity (POI) and Proof of Address (POA).The documents accepted are a copy of Aadhar card, Passport, Voter ID or Driving License.","A legitimate Proof of Identity (POI) and Proof of Address are necessary (POA). A copy of an Aadhar card, passport, voter ID, or driver's licence is acceptable documentation."],

        ("isd service","isd"): ["After migration from prepaid to postpaid,  ISD calling facility will be restricted. "],

        ("sim delivery","sim"): ["Once you have ordered a free SIM card online, the  delivery executive will contact you and deliver the SIM to your doorstep. Select a time slot most convenient to you. "],

        ("reschedule sim delivery","reschedule"): ["You can give the time as per your convenience and also reschedule the delivery if needed."],

        ("thanks","thank you","thank you so much"): ["Happy to help you!"],

        ("goodbye","good bye","cya","see you","good night","good morning","good afternoon"): ["✌️","😊","cya!!"],

        ("love","i love you","your so kind","kind"): ["😊","❤️"],
        
        ("how are you","howdy","doing"): ["I'm doing great thanks for asking","good"],

        ("network issue","network connectivity","network problem","recharge issue","call issue"):["Please raise a ticket in query page and we will update about the tracking status in your profile page"],

        ("vip number","fancy number"):["Voizfonica users could select VIP Number as per their choice from a range of premium mobile numbers.You can get it for free and for premium prizes."],

        ("after recharge","plan update"):["Please raise a ticket in query page and we will update about the tracking status in your profile page"],
        
        ("ok","ok gotit","got it","hmm","mmh"): ["😊","hmm...","ok","Glad you understood"]


    }
    def find(self,message: str) -> str:
        for key,values in self.qresponse.items():
            for i in key:
                if(i in message):
                    got_response = values[random.randrange(0,len(values))]
                    return got_response
        return "Unable to process, I'm sorry"

@csrf_exempt
def getResponse(request):
    if(request.method == "POST"):
        userMessage = request.POST.get('newchat')
        search = SearchEngine()
        response = search.find(userMessage)
        return HttpResponse(response)
    else:
        return HttpResponse("INVALID REQUEST")
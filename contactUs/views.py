from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist

#from .models import emailAddress,faxNumber,phoneNumber,smsNumber,telegramChannel

def contactUs(request):
#    try:
 #       email = emailAddress.objects.latest('id')
#        fax = faxNumber.objects.latest('id')
#        phone = phoneNumber.objects.latest('id')
  #      sms = smsNumber.objects.latest('id')
 #       telegram = telegramChannel.objects.latest('id')
#    except ObjectDoesNotExist:
#        email = None
#        fax = None
#        phone = None
#        sms = None
#        telegram = None
#    context = {
#        'email' : email,
#        'fax' :  fax,
#        'phone' : phone,
#        'sms' : sms,
#        'telegram' : telegram
#    }
    
    return render(request, 'contactus.html')
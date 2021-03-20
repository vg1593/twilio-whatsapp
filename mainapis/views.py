from django.shortcuts import render
from rest_framework.views import APIView
from twilio.twiml.messaging_response import MessagingResponse
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
# Create your views here.


class WhatsappApi(APIView):
    def post(self,request):
        msg = request.POST.get('Body')
        resp = MessagingResponse()
        resp.message("You said: {}".format(msg))
        return HttpResponse(resp.to_xml(), content_type='text/xml')

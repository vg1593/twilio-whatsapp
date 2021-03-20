from django.shortcuts import render
from rest_framework.views import APIView
from twilio.twiml.messaging_response import MessagingResponse
# Create your views here.


class WhatsappApi(APIView):
    def post(request):
        msg = request.form.get('Body')
        resp = MessagingResponse()
        resp.message("You said: {}".format(msg))
        return str(resp)
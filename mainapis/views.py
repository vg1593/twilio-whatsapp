from django.shortcuts import render
from rest_framework.views import APIView
from twilio.twiml.messaging_response import MessagingResponse
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
<<<<<<< HEAD
from mainapis.models import Conversation
from chatbot import generate_response
=======
>>>>>>> 931fe76a7b980e43aa8b4c21ecabbbac26c3b8a6
# Create your views here.


class WhatsappApi(APIView):
    def post(self,request):
        msg = request.POST.get('Body')
<<<<<<< HEAD
        user = request.POST.get("from")[-10:]
        conversation, created = Conversation.objects.get_or_create(sender=user)
        response,last,selection,language = generate_response(msg,conversation.last_selection,conversation.selections,conversation.language)
        conversation.message = response
        conversation.last_selection = last
        conversation.selections = selection
        conversation.language = language
        conversation.save()
        resp = MessagingResponse()
        resp.message(response)
        return HttpResponse(resp.to_xml(), content_type='text/xml')
=======
        resp = MessagingResponse()
        resp.message("You said: {}".format(msg))
        return HttpResponse(resp.to_xml(), content_type='text/xml')
>>>>>>> 931fe76a7b980e43aa8b4c21ecabbbac26c3b8a6

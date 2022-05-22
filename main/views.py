from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action, api_view, APIView, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import status
from django.http import Http404
from .models import *
from .serializer import *




class InfoView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):

        info = Info.objects.last()
        ser = InfoSerializer(info, )

        return Response(ser.data)

class SliderView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):

        slider = Slider.objects.last()
        ser = SliderSerializer(slider, )

        return Response(ser.data)


class We_OfferView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):

        we_offer = We_Offer.objects.all()
        ser = We_OfferSerializer(we_offer, many=True)

        return Response(ser.data)


class Our_AreasView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):

        our_areas = Our_Areas.objects.all()
        ser = Our_AreasSerializer(our_areas, many=True)

        return Response(ser.data)


class ReviewView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):

        review = Review.objects.all().order_by['-id']
        ser = ReviewSerializer(review, many=True)

        return Response(ser.data)


class Our_ExpertiseView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):

        expertise = Our_Expertise.objects.all().order_by['-id']
        ser = Our_ExpertiseSerializer(expertise, many=True)

        return Response(ser.data)


class Case_StudyView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):

        study = Case_Study.objects.all().order_by['-id']
        ser = Case_StudySerializer(study, many=True)

        return Response(ser.data)



class Our_TeamView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):

        team = Our_Team.objects.all()
        ser = Our_TeamSerializer(team, many=True)

        return Response(ser.data)



class BlogView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):

        blog = Blog.objects.all()
        ser = BlogSerializer(blog, many=True)

        return Response(ser.data)



class AboutView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):

        about = About.objects.all()
        ser = AboutSerializer(about, many=True)

        return Response(ser.data)




class About_Us_DetailView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):

        about_us_detail = About_Us_Detail.objects.all()
        ser = About_Us_DetailSerializer(about_us_detail, many=True)

        return Response(ser.data)




class MapView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):

        map = Map.objects.all()
        ser = MapSerializer(map, many=True)

        return Response(ser.data)


class QuestionView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        if user.type == 3:
            name = request.POST.get('name')
            surname = request.POST.get('surname')
            email = request.POST.get('email')
            number = request.POST.get('number')
            text = request.POST.get('text')
            Question.objects.create(name=name, surname=surname, email=email,
            number=number,
            text=text)
            return Response('скоро вам ответит один из наших юристов ')
        else:
            return Response('только клиенты могут отправлять смс')


class Sign_InView(APIView):

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password')
        if password == password2:
            User.objects.create(username=username, email=email, password=password, password2=password2)
            data = {
                'добро пожаловать в наш сайт'
            } 
            return Response(data)   
        else:
            data = {
                'пороли не совпали проверьте и попробуйте заново'
            }


class ChatView(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.type == 2 or user.type == 3:
            window = Window.objects.all().order_by('-id')
            ser = WindowSerializer(window, many=True)
            return Response(ser.data)

    def post(self, request):
        user = request.user
        if user.type == 2 or user.type == 3:
            sms = request.data['sms']
            user = request.data['user']
            Chat.objects.create(sms=sms, user_id=user)
            data = { 
                'user': user,
                'sms': sms
            }
            return Response(data)


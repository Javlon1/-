from .models import *
from rest_framework import serializers

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'        


class Our_AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_Areas
        fields = '__all__'        


class We_OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = We_Offer
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class Our_ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_Expertise
        fields = '__all__'



class Case_StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Case_Study
        fields = '__all__'



class Our_TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_Team
        fields = '__all__'



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'



class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class About_Us_DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_Us_Detail
        fields = '__all__'



class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class WindowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Window
        fields = '__all__'



# class Sign_inSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sign_in
#         fields = '__all__'


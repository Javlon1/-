from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main.views import *

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/info/', InfoView.as_view()),
    path('api/slider/', SliderView.as_view()),
    path('api/we-offer/', We_OfferView.as_view()),
    path('api/our-areas/', Our_AreasView.as_view()),
    path('api/review/', ReviewView.as_view()),
    path('api/our-expertise/', Our_ExpertiseView.as_view()),
    path('api/case-study/', Case_StudyView.as_view()),
    path('api/our-team/', Our_TeamView.as_view()),
    path('api/blog/', BlogView.as_view()),
    path('api/about/', AboutView.as_view()),
    path('api/about-us-detail/', About_Us_DetailView.as_view()),
    path('api/map/', MapView.as_view()),
    path('api/question/', QuestionView.as_view()),
    path('api/sign-in/', Sign_InView.as_view()),
    path('api/chat/', ChatView.as_view()),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

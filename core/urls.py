from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('meeting', views.meeting, name='meeting'),
    path('yoga', views.yoga, name='yoga'),
    path('about', views.about, name='about'),
    path('disorders', views.disorders, name='disorders'),
    path('anxiety', views.anxiety, name='anxiety'),
    path('mood', views.mood, name='mood'),
    path('psychotic', views.psychotic, name='psychotic'),
    path('eating', views.eating, name='eating'),
    path('personality', views.personality, name='personality'),
    path('neurodevelopment', views.neurodevelopment, name='neurodevelopment'),
    path('dissociative', views.dissociative, name='dissociative'),
    path('trauma', views.trauma, name='trauma'),
    path('sleep', views.sleep, name='sleep'),
    path('Substance_Disorders', views.Substance_Disorders, name='Substance_Disorders'),
    path('neurocoginitive', views.neurocoginitive, name='neurocoginitive'),
    path('somatoform', views.somatoform, name='somatoform'),
]

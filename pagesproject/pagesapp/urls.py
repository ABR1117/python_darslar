from django.urls import path
from .views import HomePageView, AboutPageView, AloqaPageView, YangilikPageView

urlpatterns=[
    path('',HomePageView.as_view(), name='home'),
    path('about/',AboutPageView.as_view(), name='about'),
    path('aloqa/',AloqaPageView.as_view(), name='aloqa'),
    path('yangilik/',YangilikPageView.as_view(),name='yangilik'),
]
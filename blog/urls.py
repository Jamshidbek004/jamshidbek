from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('reklama/',Reklama, name="reklama"),
    path('singlenews/<int:id>/',singlenews,name="singlenews"),
path('tag_detel/<int:id>/',Tag_detail,name="tag_detel"),
path('news_detail/<slug:news>',news_detail,name="news_detail"),
    path('single/>', single, name="single"),
path('contact/', contact, name="contact"),
path('category/', category, name="category"),
    path('search/',SearchResultList.as_view(), name="search"),

]
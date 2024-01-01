
from django.urls import path
from . import views
from django.urls import path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home" ),
    path('predict/', views.predict, name="predict"),
    path('predict/result/', views.result, name="result"),
    path('predict/result/recordData/', views.recordData, name="recordData"),
    path('help_projects.pdf', serve, {'document_root': settings.STATIC_ROOT, 'path': 'help_projects.pdf'}),]

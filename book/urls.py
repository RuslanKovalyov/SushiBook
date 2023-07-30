from django.urls import path
from . import views

urlpatterns = [
    path('', views.book, name='book'),
    path('Page/<str:name>', views.book, name='page'),

]
from django.contrib import admin
from django.urls import path
from sokoapp import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',         views.index, name='index'), 

    path('details/', views.details, name='details'),

    path('privacy/', views.privacy, name='privacy'),

    path('starter/', views.starter, name='starter'),

    path('terms/',   views.terms, name='terms'),

    path('services/', views.services, name='services'),

    

]

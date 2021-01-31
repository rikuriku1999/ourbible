from django.contrib import admin
from django.urls import path
from . import views
from .views import listfunc, createfunc, goodfunc, detailfunc, novelfunc, moviefunc, animefunc, comicfunc, practicalfunc, othersfunc, novelnewfunc, novelgoodfunc, movienewfunc, moviegoodfunc,animenewfunc, animegoodfunc, practicalnewfunc, practicalgoodfunc, comicnewfunc, comicgoodfunc, othersnewfunc, othersgoodfunc,newlistfunc, goodlistfunc, questionfunc, termsfunc
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView 

urlpatterns = [
    path('list/',listfunc,name='list'),
    path('create/',createfunc,name='create'),
    path('good/<int:pk>',goodfunc,name = 'good'),
    path('detail/<int:pk>',detailfunc,name='detail'),
    path('novellist/',novelfunc,name='novel'),
    path('novellist/new',novelnewfunc,name='novellistnew'),
    path('novellist/good',novelgoodfunc,name='novellistgood'),

    path('movielist/',moviefunc,name='movie'),
    path('movielist/new',movienewfunc,name='movielistnew'),
    path('movielist/good',moviegoodfunc,name='movielistgood'),

    path('animelist/',animefunc,name='anime'),
    path('animelist/new',animenewfunc,name='animelistnew'),
    path('animelist/good',animegoodfunc,name='animelistgood'),

    path('practicallist/',practicalfunc,name='practical'),
    path('practicallist/new',practicalnewfunc,name='practicallistnew'),
    path('practicallist/good',practicalgoodfunc,name='practicallistgood'),

    path('otherslist/',othersfunc,name='others'),
    path('otherslist/new',othersnewfunc,name='otherslistnew'),
    path('otherslist/good',othersgoodfunc,name='otherslistgood'),

    path('comiclist/',comicfunc,name='comic'),
    path('comiclist/new',comicnewfunc,name='comiclistnew'),
    path('comiclist/good',comicgoodfunc,name='comiclistgood'),

    path('list/new',newlistfunc,name='listnew'),
    path('list/good',goodlistfunc,name='listgood'),

    path('question',questionfunc,name='question'),
    path('terms',termsfunc,name='terms'),
]
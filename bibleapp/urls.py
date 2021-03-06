from django.contrib import admin
from django.urls import path
from . import views
from .views import listfunc, createfunc, goodfunc, detailfunc, novelfunc, moviefunc, animefunc, comicfunc, practicalfunc, othersfunc, novelnewfunc, novelgoodfunc, movienewfunc, moviegoodfunc,animenewfunc, animegoodfunc, practicalnewfunc, practicalgoodfunc, comicnewfunc, comicgoodfunc, othersnewfunc, othersgoodfunc,newlistfunc, goodlistfunc, randomlistfunc, othersrandomfunc, comicrandomfunc, animerandomfunc, movierandomfunc, practicalrandomfunc, novelrandomfunc, questionfunc, termsfunc, privacyfunc
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView 

urlpatterns = [
    path('',listfunc,name='list'),
    path('list/',listfunc,name='list'),
    path('create/',createfunc,name='create'),
    path('good/<int:pk>',goodfunc,name = 'good'),
    path('detail/<int:pk>',detailfunc,name='detail'),
    path('novellist/',novelfunc,name='novel'),
    path('novellist/new',novelnewfunc,name='novellistnew'),
    path('novellist/good',novelgoodfunc,name='novellistgood'),
    path('novellist/random',novelrandomfunc,name='novellistrandom'),

    path('movielist/',moviefunc,name='movie'),
    path('movielist/new',movienewfunc,name='movielistnew'),
    path('movielist/good',moviegoodfunc,name='movielistgood'),
    path('movielist/random',movierandomfunc,name='movielistrandom'),

    path('animelist/',animefunc,name='anime'),
    path('animelist/new',animenewfunc,name='animelistnew'),
    path('animelist/good',animegoodfunc,name='animelistgood'),
    path('animelist/random',animerandomfunc,name='animelistrandom'),

    path('practicallist/',practicalfunc,name='practical'),
    path('practicallist/new',practicalnewfunc,name='practicallistnew'),
    path('practicallist/good',practicalgoodfunc,name='practicallistgood'),
    path('practicallist/random',practicalrandomfunc,name='practicallistrandom'),

    path('otherslist/',othersfunc,name='others'),
    path('otherslist/new',othersnewfunc,name='otherslistnew'),
    path('otherslist/good',othersgoodfunc,name='otherslistgood'),
    path('otherslist/random',othersrandomfunc,name='otherslistrandom'),

    path('comiclist/',comicfunc,name='comic'),
    path('comiclist/new',comicnewfunc,name='comiclistnew'),
    path('comiclist/good',comicgoodfunc,name='comiclistgood'),
    path('comiclist/random',comicrandomfunc,name='comiclistrandom'),

    path('list/new',newlistfunc,name='listnew'),
    path('list/good',goodlistfunc,name='listgood'),
    path('list/random',randomlistfunc,name='listrandom'),

    path('question',questionfunc,name='question'),
    path('terms',termsfunc,name='terms'),
    path('privacy',privacyfunc,name='privacy'),
]
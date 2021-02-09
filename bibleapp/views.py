from django.shortcuts import render ,redirect ,get_object_or_404
from .models import Biblemodel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login ,logout
from . import forms
import random
from django.contrib.auth import get_user_model
from django.views import generic
from django.template.loader import render_to_string
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.conf import settings
from django.http import Http404, HttpResponseBadRequest
from django.contrib import messages
from django.db.models import Q

from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def questionfunc(request):
    return render(request,'question.html',)

def termsfunc(request):
    return render(request,'terms.html',)

def privacyfunc(request):
    return render(request,'privacy.html',)

def listfunc(request):
    form = forms.SearchForm(request.POST or None) 
    object_list = Biblemodel.objects.all()
    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(3):
        url = url + urllist[i] +  "/"
    url = url + "list/"
    if request.method == "POST":
        if form.is_valid():
            search = form.cleaned_data['search']
            object_list = Biblemodel.objects.filter(title__contains = search)
    else :
        object_list = Biblemodel.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'form':form,
        'numbers':numbers,
        'url':url,
    })

def randomlistfunc(request):
    form = forms.SearchForm(request.POST or None) 
    object_list = Biblemodel.objects.all()
    if request.method == "POST":
        if form.is_valid():
            search = form.cleaned_data['search']
            object_list = Biblemodel.objects.filter(title__contains = search).order_by('?')

    else :
        object_list = Biblemodel.objects.all().order_by('?')
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'numbers':numbers,
        'form':form,
    })

def goodlistfunc(request):
    form = forms.SearchForm(request.POST or None) 
    object_list = Biblemodel.objects.all()
    if request.method == "POST":
        if form.is_valid():
            search = form.cleaned_data['search']
            object_list = Biblemodel.objects.filter(title__contains = search).order_by('-good')

    else :
        object_list = Biblemodel.objects.all().order_by('-good')
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'numbers':numbers,
        'form':form,
    })
def newlistfunc(request):
    form = forms.SearchForm(request.POST or None) 
    object_list = Biblemodel.objects.all()
    if request.method == "POST":
        if form.is_valid():
            search = form.cleaned_data['search']
            object_list = Biblemodel.objects.filter(title__contains = search)
    else :
        object_list = Biblemodel.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'numbers':numbers,
        'form':form,
    })

def novelfunc(request):
    object_list = Biblemodel.objects.filter(category = '小説')

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def novelnewfunc(request):
    object_list = Biblemodel.objects.filter(category = '小説')

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def novelrandomfunc(request):
    object_list = Biblemodel.objects.filter(category = '小説').order_by("?")

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def novelgoodfunc(request):
    object_list = Biblemodel.objects.filter(category = '小説').order_by("-good")

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })

def moviefunc(request):
    object_list = Biblemodel.objects.filter(category = '映画')

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def movienewfunc(request):
    object_list = Biblemodel.objects.filter(category = '映画')

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def movierandomfunc(request):
    object_list = Biblemodel.objects.filter(category = '映画').order_by('?')

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def moviegoodfunc(request):
    object_list = Biblemodel.objects.filter(category = '映画').order_by("-good")

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })

def comicfunc(request):
    object_list = Biblemodel.objects.filter(category = '漫画')

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def comicnewfunc(request):
    object_list = Biblemodel.objects.filter(category = '漫画')

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def comicgoodfunc(request):
    object_list = Biblemodel.objects.filter(category = '漫画').order_by("-good")

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def comicrandomfunc(request):
    object_list = Biblemodel.objects.filter(category = '漫画').order_by("?")

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
    
def practicalfunc(request):
    object_list = Biblemodel.objects.filter(category = '実用書')

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def practicalnewfunc(request):
    object_list = Biblemodel.objects.filter(category = '実用書')

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def practicalgoodfunc(request):
    object_list = Biblemodel.objects.filter(category = '実用書').order_by("-good")

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def practicalrandomfunc(request):
    object_list = Biblemodel.objects.filter(category = '実用書').order_by("?")

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
    
def animefunc(request):
    object_list = Biblemodel.objects.filter(category = 'アニメ')

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def animenewfunc(request):
    object_list = Biblemodel.objects.filter(category = 'アニメ')

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def animegoodfunc(request):
    object_list = Biblemodel.objects.filter(category = 'アニメ').order_by("-good")

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def animerandomfunc(request):
    object_list = Biblemodel.objects.filter(category = 'アニメ').order_by("?")

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })

def othersfunc(request):
    object_list = Biblemodel.objects.filter(category = 'その他')

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def othersnewfunc(request):
    object_list = Biblemodel.objects.filter(category = 'その他')

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def othersgoodfunc(request):
    object_list = Biblemodel.objects.filter(category = 'その他').order_by("-good")

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })
def othersrandomfunc(request):
    object_list = Biblemodel.objects.filter(category = 'その他').order_by("?")

    url = request.build_absolute_uri()
    urllist = url.split("/")
    url = ""
    for i in range(4):
        url = url + urllist[i] + "/"
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 8)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    return render(request, 'list.html',{
        'object_list':object_list,
        'url':url,
        'numbers':numbers,
    })


def createfunc(request):
    detail = Biblemodel()
    form = forms.DetailForm(request.POST )
    if request.method == 'POST' :
        if form.is_valid():
            detail.title = form.cleaned_data['title']
            detail.content = form.cleaned_data['content']
            detail.url = form.cleaned_data['url']
            detail.sex = form.cleaned_data['sex']
            detail.author = form.cleaned_data['author']
            detail.age = form.cleaned_data['age']
            detail.category = form.cleaned_data['category']
            Biblemodel.objects.create(
                title = detail.title,
                content = detail.content,
                url = detail.url,
                sex = detail.sex,
                author = detail.author,
                age = detail.age,
                category = detail.category,
            )
            return redirect('list')
    return render(request, 'create.html',{
        'form':form,
        'detail':detail,
    })


def goodfunc(request,pk):
    bible = Biblemodel.objects.get(pk=pk)
    if not request.session.session_key:
        request.session.create()
        session_id = request.session.session_key
    else :
        session_id = request.session.session_key
    print(session_id)
    session_id = session_id[1:8]
    if session_id in bible.goodtext :
        print(bible.goodtext)
    else:
        bible.good += 1
        bible.goodtext = bible.goodtext + ' ' + session_id
        bible.save()
    return redirect('detail',pk=pk)

def detailfunc(request,pk):
    bible = Biblemodel.objects.get(pk=pk)
    return render(request,'detail.html',{
        'bible':bible,

    })



from django.http import request
from django.shortcuts import render, redirect
from book.views import book

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from users.models import Profile

def home(request):
    #feed Community
    paginator = Paginator(Profile.objects.order_by('-id').exclude(avatar="users/profile_images/default.jpg"), 10)
    try:
        people = paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        people = paginator.page(1)
    except EmptyPage:
        people = paginator.page(paginator.num_pages)

    #feed Partners
    paginator2 = Paginator(Partner.objects.order_by('-id'), 12)
    try:
        partners = paginator2.page(request.GET.get('page'))
    except PageNotAnInteger:
        partners = paginator2.page(1)
    except EmptyPage:
        partners = paginator2.page(paginator2.num_pages)

    context = {'people': people,'partners': partners}

    return render(request, 'main/home.html', context)

def index(request):
    paginator = Paginator(Profile.objects.order_by('-id').exclude(avatar="users/profile_images/default.jpg"), 10)
    try:
        people = paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        people = paginator.page(1)
    except EmptyPage:
        people = paginator.page(paginator.num_pages)
    context = {'people': people}
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

def Oops(request, exception):
    return render(request, 'main/Oops.html')

def development(request):
     return render(request, 'main/development.html')

class basics():
    def rice(request):
        return render(request, 'main/book/basics/rice.html')
    def vinegar(request):
        return render(request, 'main/book/basics/seasoning-sushi-vinegar.html')
        
class sauces():
    def teriyaki(request):
        return render(request, 'main/book/sauces/teriyaki.html')
    def ponzu(request):
        return render(request, 'main/book/sauces/ponzu.html')
    def spicy_mayo(request):
        return render(request, 'main/book/sauces/spicy-mayo.html')
    def den_miso(request):
        return render(request, 'main/book/sauces/den-miso.html')

class tools():
    def cutting_board(request):
        return render(request, 'main/book/tools/cutting-board.html')
    def hangiri(request):
        #return render(request, 'main/book/tools/hangiri.html')
        return redirect(book, name='Hangiri')#redirect from old statik pages to new book disigned by model

    def knife(request):
        return render(request, 'main/book/tools/knife.html')
    def makisu(request):
        return render(request, 'main/book/tools/makisu.html')

class kids():
    def raw_fish(request):
        #eturn render(request, 'main/book/kids/raw-fish.html')
        return redirect(book, name='Raw-Fish')#redirect from old statik pages to new book disigned by model


    def recipes(request):
        #return render(request, 'main/book/kids/recipes.html')
        return redirect(book, name='Recipes-For-Kids')#redirect from old statik pages to new book disigned by model





from .models import Partner, News, Job, SushiRoll

def partners(request):
    objs = Partner.objects.order_by('-id')
    return render(request, 'main/partners.html', { 'partners':objs })
    
def news(request):
    objs = News.objects.order_by('-id')
    return render(request, 'main/news.html', { 'news':objs })

class job():
    def all(request):
        objs = Job.objects.order_by('-id')
        return render(request, 'main/job.html', { 'job':objs })
    def israel(request):
        objs = Job.objects.filter(country='Israel').order_by('-id')
        return render(request, 'main/job.html', { 'job':objs })
    def usa(request):
        objs = Job.objects.filter(country='USA').order_by('-id')
        return render(request, 'main/job.html', { 'job':objs })

class insider():
    @login_required
    def all(request):
        objs = SushiRoll.objects.order_by('-id')
        return render(request, 'main/insider.html', { 'insider':objs })
    @login_required
    def frame(request):
        objs = SushiRoll.objects.filter(restaurant='Frame chef & Sushi Bar').order_by('-id')
        return render(request, 'main/insider.html', { 'insider':objs })
    @login_required
    def moon(request):
        objs = SushiRoll.objects.filter(restaurant='Moon Sushi Bar').order_by('-id')
        return render(request, 'main/insider.html', { 'insider':objs })
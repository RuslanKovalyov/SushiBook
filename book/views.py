from django.shortcuts import render
from django.http import request

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from users.models import Profile
from .models import Section, Page, RecipeDetails
from django.shortcuts import get_object_or_404

# from django.conf import settings #cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT #cache
from django.views.decorators.cache import cache_page #cache

# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT) #cache

# @cache_page(CACHE_TTL) #cache
def book(request, name='About'):
    s = Section.objects.order_by('name')
    ps = Page.objects.order_by('name')
    p = get_object_or_404(Page, name=name)
    d = RecipeDetails.objects.filter(page=p)
    recipe_part = list(dict.fromkeys([ part.recipe_part for part in d]))

    #feed Community
    paginator = Paginator(Profile.objects.order_by('-id').exclude(avatar="users/profile_images/default.jpg"), 10)
    try:
        people = paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        people = paginator.page(1)
    except EmptyPage:
        people = paginator.page(paginator.num_pages)

    context = {'people': people, 'page':p, 'sections':s, 'pages':ps, 'details':d, 'recipe_part':recipe_part}

    return render(request, 'book/home.html', context)
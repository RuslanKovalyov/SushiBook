from django.urls import path
from . import views
from book.views import book


urlpatterns = [
    path('', book, name='home'),
    #path('About', views.about, name='about'),
    path('Partners', views.partners, name='partners'),
    path('404', views.Oops, name='404'),
    path('Development', views.development, name='development'),
    #path('Basics/Rice', views.basics.rice, name='basics/rice'),
    #path('Basics/Seasoning-Vinegar', views.basics.vinegar, name='basics/vinegar'),
    #path('Sauces/Teriyaki', views.sauces.teriyaki, name='sauces/teriyaki'),
    #path('Sauces/Ponzu', views.sauces.ponzu, name='sauces/ponzu'),
    #path('Sauces/Spicy-Mayo', views.sauces.spicy_mayo, name='sauces/spicy-mayo'),
    #path('Sauces/Den-Miso', views.sauces.den_miso, name='sauces/den-miso'),
    #path('Tools/Cutting-Board', views.tools.cutting_board, name='tools/cutting-board'),
    path('Tools/Hangiri', views.tools.hangiri, name='tools/hangiri'),#navbar
    #path('Tools/Knife', views.tools.knife, name='tools/knife'),
    #path('Tools/Makisu', views.tools.makisu, name='tools/makisu'),
    #path('Kids/Raw-Fish', views.kids.raw_fish, name='kids/raw-fish'),
    path('Kids/Recipes', views.kids.recipes, name='kids/recipes'),#navbar
    path('News', views.news, name='news'),
    
    #path('Job', views.job.all, name='job'),
    #path('Job/Israel', views.job.israel, name='job/israel'),
    #path('Job/USA', views.job.usa, name='job/usa'),
    
    path('Insider', views.insider.all, name='insider/all'),
    #path('Insider/Frame', views.insider.frame, name='insider/frame'),
    #path('Insider/Moon', views.insider.moon, name='insider/moon'),
    
]
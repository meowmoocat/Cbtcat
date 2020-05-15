from django.urls import path

from . import views
from .levels.all_or_nothing import AllOrNothing
from .levels.catastrophising import Catastrophising
from .levels.intro import Intro
from .levels.labelling import Labelling
from .levels.mindreading import Mindreading
from .levels.overgeneralisation import Overgeneralisation

urlpatterns = [
    path('', views.tohome, name='to-home'),
    path('home/', views.index, name='index'),
    path('login/', views.user_login, name='cbtcat-login'),
    path('register/', views.UserRegisterFormView.as_view(), name='register'),
    path('links/', views.links, name='links'),
    path('1/', Intro.as_view(), name='intro'),
    path('2/', Catastrophising.as_view(), name='catastrophising'),
    path('3/', AllOrNothing.as_view(), name='all-or-nothing'),
    path('4/', Labelling.as_view(), name='labelling'),
    path('5/', Overgeneralisation.as_view(), name='overgeneralisation'),
    path('6/', Mindreading.as_view(), name='mindreading'),
    # path('shop/', shop.as_view(), name='shop'),
    # path('profile/', profile.as_view(), name='profile'),
    # path('pictures/', pictures.as_view(), name='profile'),
]

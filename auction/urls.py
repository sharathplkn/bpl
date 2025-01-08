from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('players/', views.players, name='players'),
    path('auction/<int:player_id>/', views.auction, name='auction'),
    path('clubs/', views.clubs, name='clubs'),
    path('clubs/<int:team_id>/', views.team_detail, name='team_detail'),
]
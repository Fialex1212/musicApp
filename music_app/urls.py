from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),

    #Main
    path('home/', views.home, name='home'),
    path('setting/', views.settings, name='settings'),
    path('help/', views.help, name='help'),
    path('', views.s, name='s'),

    #Auth
    path('', views.s, name='s'),

    #User
    path('you/', views.you, name='you'),
    path('<str:name>/', views.user, name='user'),
    path('you/likes/', views.you_likes, name='you_likes'),
    path('<str:name>/likes/', views.user_likes, name='user_likes'),
    path('user/following/', views.you_following, name='you_following'),
    path('<str:name>/following/', views.user_following, name='user_following'),
    path('you/<str:playlists>/', views.you_playlists, name='you_playlists'),
    path('<str:name>/<str:playlists>/', views.user_playlists, name='user_playlists'),
    path('you/tracks/', views.you_tracks, name='you_tracks'),
    path('<str:name>/tracks/', views.user_tracks, name='user_tracks'),

    path('you/upload/', views.upload, name='upload'),

    #Search


    #Errors
]
'''
all urls for my site
home/
search?q=zxc
search/sounds?q=zxc
search/people?q=zxc
search/playlists?q=zxc
you/
you/name_of_playlist/
you/following/
you/tracks/
user_name/name_fo_playlist/
user_name/following/
user_name/tracks/
settings/
help/
upload/
'''
from django.urls import path
from relax import views

urlpatterns = [
    path('', views.HomeClass.as_view(), name='home'),
    path('profile/', views.ProfilesClass.as_view(), name='profile'),
    path('about-us/', views.AboutUsClass.as_view(), name='about-us'),
    path('menu/', views.MenuClass.as_view(), name='menu'),
    path('music/', views.MusicClass.as_view(), name='music'),
    path('chat/', views.ChatClass.as_view(), name='chat'),
    path('image/', views.ImageClass.as_view(), name='image'),
    path('tools/', views.ToolsClass.as_view(), name='tools'),
]
from django.urls import path
from . import views

app_name = 'app10'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('update/<int:id>', views.update, name='update'),
    path('home/<int:id>', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('gallery/', views.galleryPage, name='gallery'),
    path('details/<int:id>', views.details, name='details')
]

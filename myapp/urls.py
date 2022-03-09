from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('image', views.image, name='image'),
    path('intro/<str:name>/<int:age>', views.intro, name='intro'),
]
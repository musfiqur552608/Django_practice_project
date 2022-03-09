from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('add/<int:a>/<int:b>', views.add, name='add'),
    path('intro/<str:name>/<int:age>', views.intro, name='intro'),
]
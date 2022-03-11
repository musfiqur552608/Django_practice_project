from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('images', views.images, name='images'),
    path('image/<str:imgname>', views.image, name='image'),
    path('intro/<str:name>/<int:age>', views.intro, name='intro'),
    path('myform', views.myform, name='myform'),
    path('submitform',views.submitform, name="submitform")
]
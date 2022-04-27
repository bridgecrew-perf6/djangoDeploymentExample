from django.urls import include, path
from wkFourApp import views

# Template tagging
app_name = 'wkFourApp'

urlpatterns = [
    path("relative/", views.relative, name = 'relative'),
    path("other/", views.other, name = 'other'), 
    path("", views.index, name='index Two')   

]



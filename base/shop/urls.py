# for each app, we need to create a urls.py file
# It's not automatically created, so we need to create it manually.

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    # view.index - is the view function that will be called when the user visits the index page
    # name='index' - is the name of the view function
]
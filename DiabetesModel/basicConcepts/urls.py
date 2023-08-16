
#it is used to interact with the rootNode or root application DiabetesModel of urls

from django.urls import path
from . import views


urlpatterns=[             #routing of different pages

    path('',views.Welcome),
    path('user',views.User)
]
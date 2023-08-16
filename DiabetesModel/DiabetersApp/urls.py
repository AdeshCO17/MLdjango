from django.urls import path
from . import views

urlpatterns=[
    path('',views.PredictModel),
  path('invoke-function/', views.invoke_function, name='invoke_function'),

    # path('home',views.home)
]
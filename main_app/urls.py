from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns =[
     path('', views.index, name='index'),
     path('accounts/signup/', views.signup, name='signup'),
     path('application/create/', login_required(views.ApplicationCreate.as_view()), name='application_create'),
]
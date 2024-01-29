from django.urls import path
from users import views as userviews

app_name = 'users'

urlpatterns = [    
    path('home/', userviews.index, name='index'),   
]
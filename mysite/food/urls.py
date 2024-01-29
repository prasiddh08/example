from django.urls import path
from food import views

app_name="food"

urlpatterns = [
    #function based index view
    #---------------------------------------------------------------
   # path('index/', views.index , name='index'),

    #class based index view
    #---------------------------------------------------------------
    path('index/', views.IndexClassView.as_view() , name='index'),

    #function based detail view
    #---------------------------------------------------------------
   # path("detail/<int:item_id>/",views.detail,name="detail"),

    #class based detail view
    #---------------------------------------------------------------
    path("detail/<int:pk>/",views.FoodDetail.as_view(),name="detail"),

    #function based create item view
    #---------------------------------------------------------------
   # path('add/', views.CreateItem, name='create_item'),

    #class based create item view
    #---------------------------------------------------------------
    path('add/', views.CreateView.as_view(), name='create_item'),

    #function based update item view
    #---------------------------------------------------------------
    path('update/<int:item_id>/',views.UpdateItem, name='update_item'),

    #function based delete item view
    #---------------------------------------------------------------
    path('delete/<int:item_id>/',views.DeleteItem,name='delete_item'),

]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create-client', views.createClient, name="create_client"),
    path('view-client/<int:pk>/', views.viewClientWallet, name="view_client"),
    path('update-client/<int:pk>/', views.updateClient, name="update_client"),
    path('delete-client/<int:pk>/', views.deleteClient, name="delete_client"),

    path('api/clients/<int:pk>/', views.ClientDetailAPIView.as_view()),

]

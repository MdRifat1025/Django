from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.Products, name='products'),
    path("signin/",views.signin,name="signin"),
    path('signup/', views.Signup, name='signup'),
]

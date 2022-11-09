from django.urls import path 
from . import views
app_name = 'km'

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.signin,name='login'),
    path('home/cart/',views.cart,name='cart'),
    path('logout',views.signout,name="logout")
]

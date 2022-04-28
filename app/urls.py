from django.urls import path
from .views import *
urlpatterns = [
    path('',store,name='store'),
    path('card',card,name='cart'),
    path('checkout',checkout,name='checkout'),
    path('login',loginPage,name='login'),
    path('register',register,name='register'),
    path('logout',logoutUser,name='logout'),
    path('update_item/',update),
    path('detail/<int:id>',product_detail,name='product-detail')
]

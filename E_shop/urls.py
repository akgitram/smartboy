"""E_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name="base"),
    path('',views.HOME,name="home"),
    path('product/',views.PRODUCT, name="product"),

    path('search/',views.SEARCH,name="search"),
    path('products/<str:id>',views.SINGLE,name="products"),
    path('contact/',views.Contact_Page,name='contact'),
    path('register/',views.REGISTER,name='register'),
    path('login/',views.LOGIN,name='login'),
    path('logout/',views.LOGOUT,name='logout'),
    path('success/', views.SUCCESS, name="success"),



     #Cart
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
	path('cart/add/<int:id>',views.cart_add,name='cart_add'),
	path('cart/checkout/',views.Checkout,name='checkout'),
    path('cart/checkout/place_order/', views.PLACE_ORDER, name='place_order'),


] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

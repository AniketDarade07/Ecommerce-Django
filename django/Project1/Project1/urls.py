from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "My Website Admin"
admin.site.site_title = "My Website Admin Portal"
admin.site.index_title = "Welcome to My Website"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("service", views.service, name='service'),
    path("main", views.main, name='main'),
    path("contact", views.contact, name='contact'),
    path("login", views.loginuser, name='login'),
    path("logout", views.logoutuser, name='logout'),
    path("index", views.index, name='index'),
    
    path("store", views.store, name='store'),
    path("cart", views.cart, name='cart'),
    path("checkout", views.checkout, name='checkout'),
    
    path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]

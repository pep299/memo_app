from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:now_page>', views.index, name='index'),
    path('post', views.post, name='post'),
    path('set_record_number', views.set_record_number, name='set_record_number'),
    path('set_order_option', views.set_order_option, name='set_order_option')
]

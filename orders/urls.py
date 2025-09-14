from django.urls import path
from .views import OrderListView, OrderCreateVIew, OrderDetailView

app_name = 'orders'


urlpatterns = [
    path('order-create/', OrderCreateVIew.as_view(), name='order_create'),
    path('', OrderListView.as_view(), name='orders_list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order_detail'),

]

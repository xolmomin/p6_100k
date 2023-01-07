from django.urls import path

from apps.views import WithdrawView, MainPageView, ProductDetailView, MarketListView, StreamPageListView
from apps.views.base import MainPageView, ProductDetailView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page_view'),
    path('product/shop/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('product/<str:slug>', ProductDetailView.as_view(), name='product_detail_view'),
    path('admin/stream', StreamPageListView.as_view(), name='stream_page_view'),
    path('admin/withdraw', WithdrawView.as_view(), name='withdraw'),
    path('admin/market', MarketListView.as_view(), name='market'),
]

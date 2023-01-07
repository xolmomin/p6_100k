from django.urls import path

from apps.views import ProfileView
from apps.views import WithdrawView, MarketListView, StreamPageListView
from apps.views.base import MainPageView, ProductDetailView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page_view'),
    path('product/shop/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('profile', ProfileView.as_view(), name='profile_page'),
    path('product/<str:slug>', ProductDetailView.as_view(), name='product_detail_view'),
    path('admin/streams', StreamPageListView.as_view(), name='stream_page_view'),
    path('admin/withdraw', WithdrawView.as_view(), name='withdraw'),
    path('admin/market', MarketListView.as_view(), name='market'),
]

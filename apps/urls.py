from django.urls import path

from apps.views import WithdrawView, MarketListView, MainPageView, ProductDetailView, StreamPageView
from apps.views import WithdrawView, MarketListView, MainPageView, ProductDetailView, ProfileView
from apps.views.base import StreamPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page_view'),
    path('product/shop/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('product/<str:slug>', ProductDetailView.as_view(), name='product_detail_view'),
    path('admin/stream', StreamPageView.as_view(), name='stream_page_view'),
    path('admin/withdraw', WithdrawView.as_view(), name='withdraw'),
    path('admin/market', MarketListView.as_view(), name='market'),
]

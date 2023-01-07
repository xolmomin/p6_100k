from django.urls import path

from apps.views import WithdrawView, MarketListView, MainPageView, ProductDetailView, StoreDetailView, \
    ProfileView, StreamPageListView

urlpatterns = [
    path('market', MarketListView.as_view(), name='market'),
    path('store/<int:pk>', StoreDetailView.as_view(), name='store'),
    path('product/shop/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('', MainPageView.as_view(), name='main_page_view'),
    path('product/shop/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('product/<str:slug>', ProductDetailView.as_view(), name='product_detail_view'),
    path('admin/stream', StreamPageListView.as_view(), name='stream_page_view'),
    path('admin/withdraw', WithdrawView.as_view(), name='withdraw'),
    path('admin/market', MarketListView.as_view(), name='market'),
]

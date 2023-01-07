from django.urls import path

from apps.views import WithdrawView, MainPageView, ProductDetailView, MarketListView

urlpatterns = [
    path('market', MarketListView.as_view(), name='market'),
    path('product/shop/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('', MainPageView.as_view(), name='main_page_view'),
    path('product/shop/<str:slug>', ProductDetailView.as_view(), name='product_detail_view'),
    path('admin/withdraw', WithdrawView.as_view(), name='product_detail_view'),
]

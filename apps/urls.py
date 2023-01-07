from django.urls import path

from apps.views import MarketListView, MainPageView
from apps.views.base import ProductDetailView

urlpatterns = [
    path('market', MarketListView.as_view(), name='market'),
    path('product/shop/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('', MainPageView.as_view(), name='main_page_view'),
]

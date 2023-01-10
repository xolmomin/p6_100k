from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from apps.views import (ProfileView, AdminProductDetailView, ProductDetailView, MainPageView, WithdrawView,
                        MarketListView, StreamPageListView, AdminPageView, ContactsView)
from apps.views import StoreDetailView
from apps.views.product_handbook import CategoryDetail

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page_view'),
    path('product/shop/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('profile/', ProfileView.as_view(), name='profile_page'),
    path('product/<str:slug>', ProductDetailView.as_view(), name='product_detail_view'),
    path('store/<int:pk>', StoreDetailView.as_view(), name='store'),
    path('category/', CategoryDetail.as_view(), name='category_detail'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('admin-page', AdminPageView.as_view(), name='admin_page'),
    path('admin/streams', csrf_exempt(StreamPageListView.as_view()), name='stream_page_view'),
    path('admin/withdraw', csrf_exempt(WithdrawView.as_view()), name='withdraw'),
    path('admin/market', MarketListView.as_view(), name='market'),
    path('admin/product/<int:pk>', AdminProductDetailView.as_view(), name='admin_product_detailview'),
]

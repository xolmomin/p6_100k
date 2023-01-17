from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from apps.bot import UpdateBot
from apps.views import (ExploreProductsView, CategoryDetail, DistrictsView, OrderView, GetStreamView,
                        StreamDeleteView, SearchPageView, FavoriteView, SettingsView, AdminStatisticsPage,
                        FavoriteListView, ProfileView, AdminProductDetailView, ProductDetailView, MainPageView,
                        WithdrawView, OperatorPageView, MyOrderPageView, MarketListView, StreamPageListView,
                        AdminPageView, ContactsView, StoreDetailView, ProfileLoginView)

operator_urls = [
    path('operator/', OperatorPageView.as_view(), name='operator'),
    path('operator/my-order', MyOrderPageView.as_view(), name='my_order')
]

admin_urls = [
    path('admin-page', AdminPageView.as_view(), name='admin_page'),
    path('admin/profile/get-destricts', csrf_exempt(DistrictsView.as_view()), name='get_districts'),
    path('admin/streams', StreamPageListView.as_view(), name='stream_page_view'),
    path('admin/delete-stream', StreamDeleteView.as_view(), name='stream_deleteview'),
    path('admin/withdraw', csrf_exempt(WithdrawView.as_view()), name='withdraw'),
    path('admin/market', MarketListView.as_view(), name='market'),
    path('admin/product/<int:pk>', AdminProductDetailView.as_view(), name='admin_product_detailview'),
    path('admin/statistics', AdminStatisticsPage.as_view(), name='admin_statistics'),
]

base_urls = [
    path('', MainPageView.as_view(), name='main_page_view'),
    path('search', csrf_exempt(SearchPageView.as_view()), name='search_page_view'),
    path('product/shop/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('explore', ExploreProductsView.as_view(), name='explore'),
    path('favorites', csrf_exempt(FavoriteListView.as_view()), name='favorite'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('login', ProfileLoginView.as_view(), name='login'),
    path('store/<int:pk>', StoreDetailView.as_view(), name='store'),
    path('category', CategoryDetail.as_view(), name='category_detail'),
    path('contacts', ContactsView.as_view(), name='contacts'),
    path('shop/favorite', FavoriteView.as_view(), name='favorite'),
    path('settings', SettingsView.as_view(), name='settings'),
    path('profile/', ProfileView.as_view(), name='profile_page'),
    path('order/', OrderView.as_view(), name='order'),
    path('stream/<int:pk>', GetStreamView.as_view(), name='get_stream_view'),

    path('bot', csrf_exempt(UpdateBot.as_view()), name='bot'), ]

urlpatterns = operator_urls + admin_urls + base_urls

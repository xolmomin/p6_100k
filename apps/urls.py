from django.urls import path

from apps.views import WithdrawView, MainPageView, ProductDetailView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page_view'),
    path('product/<str:slug>', ProductDetailView.as_view(), name='product_detail_view'),
    path('admin/withdraw', WithdrawView.as_view(), name='product_detail_view'),
]

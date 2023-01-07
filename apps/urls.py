from django.urls import path, include

from apps.views.base import MainPageView, ProductDetailView, StreamPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page_view'),
    path('product/<str:slug>', ProductDetailView.as_view(), name='product_detail_view'),
    path('admin/stream', StreamPageView.as_view(), name='stream_page_view'),
]

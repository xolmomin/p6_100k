from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from apps.bot import UpdateBot
from apps.views.base import MainPageView, ProductDetailView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page_view'),
    path('product/<str:slug>', ProductDetailView.as_view(), name='product_detail_view'),
    path('bot/', csrf_exempt(UpdateBot), name='bot'),
]

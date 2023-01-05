from django.urls import path
from apps.views.base import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
]

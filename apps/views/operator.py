from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, TemplateView, FormView

from apps.models import ProductOrders, Stream


class OperatorPageView(ListView):
    template_name = 'apps/operator/main_page.html'
    queryset = ProductOrders.objects.filter(status=ProductOrders.OrderStatus.YANGI)
    context_object_name = 'orders'


class MyOrderPageView(ListView):
    template_name = 'apps/operator/my_order.html'
    model = ProductOrders

    def post(self, request, *args, **kwargs):
        user = request.POST['user']
        stream = request.POST['stream']
        ProductOrders.objects.filter(stre)
        return redirect('my_order')

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, FormView

from apps.forms.base import CreateCommentForm
from apps.models import Product, Comment

from django.views.generic import TemplateView


class MainPageView(TemplateView):
    queryset = Product.objects.all()
    template_name = 'apps/main_page.html'



class ProductDetailView(FormView, DetailView):
    template_name = 'apps/product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'post'
    form_class = CreateCommentForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['comment'] = Comment.objects.all()
        return context

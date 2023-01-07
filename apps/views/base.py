from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, FormView, ListView

from apps.forms.base import CreateCommentForm
from apps.models import Product, Comment, Stream

from django.views.generic import TemplateView


class MainPageView(TemplateView):
    queryset = Product.objects.all()
    template_name = 'apps/main_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['products'] = Product.objects.all()[:6]


class ProductDetailView(FormView, DetailView):
    template_name = 'apps/product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'post'
    form_class = CreateCommentForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['comment'] = Comment.objects.all()
        return context


def completed(request, *args, **kwargs):
    stream = Stream.objects.get(id=id)
    stream.is_area = not stream.is_area
    stream.save()

    return JsonResponse({'status': 200})


# class StreamPageView(LoginRequiredMixin, ListView):
class StreamPageView(ListView):
    template_name = 'apps/admin/stream.html'
    model = Stream
    queryset = Stream.objects.all()
    context_object_name = 'streams'
    paginate_by = 9

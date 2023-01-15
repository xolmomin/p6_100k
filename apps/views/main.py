from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, FormView, TemplateView

from apps.forms import OrderForm
from apps.models import Product, Category, Contact, Favorite


class MainPageView(ListView, FormView):
    template_name = 'apps/index.html'
    queryset = Category.objects.all()
    context_object_name = 'categories'
    form_class = OrderForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['products'] = Product.objects.all()[:8]
        return context


class SearchPageView(View):
    def post(self, request, *args, **kwargs):
        data = []
        for product in Product.objects.all()[:10]:
            data.append(model_to_dict(product, fields=('id', 'title', 'description')))
        return JsonResponse(data, safe=False)


class ExploreProductsView(ListView):
    template_name = 'apps/explore.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        if category := self.request.GET.get('sort'):
            return qs.filter(category__slug=category)
        return qs


class FavoriteView(LoginRequiredMixin, ListView):
    template_name = 'apps/favorite.html'
    queryset = Favorite


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/profile.html'

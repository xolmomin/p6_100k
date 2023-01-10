from django.http import JsonResponse
from django.views.generic import ListView

from apps.models import Product, Stream, Category, Contact


class MainPageView(ListView):
    template_name = 'apps/index.html'
    queryset = Category.objects.all()
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['products'] = Product.objects.all()[:6]
        return context


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


class ContactsView(ListView):
    template_name = 'apps/contacts.html'
    model = Contact


def completed(request, *args, **kwargs):
    stream = Stream.objects.get(id=id)
    stream.is_area = not stream.is_area
    stream.save()

    return JsonResponse({'status': 200})

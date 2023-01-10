from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import ListView, DetailView, TemplateView

from apps.models import Stream, Store, Product, Category


class MainPageView(TemplateView):
    queryset = Product.objects.all()
    template_name = 'apps/main_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['products'] = Product.objects.all()[:6]
        context['categories'] = Category.objects.all()
        return context


class StreamPageListView(ListView):
    template_name = 'apps/admin/stream.html'
    model = Stream
    queryset = Stream.objects.all()
    context_object_name = 'streams'
    paginate_by = 9

    def post(self, request, *args, **kwargs):
        stream = Stream.objects.filter(id=int(request.POST['id'])).first()
        stream.is_area = not stream.is_area
        stream.save()
        return super().post(self, request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['url'] = get_current_site(self.request)
        return context


class StoreDetailView(DetailView):
    template_name = 'apps/store_detail.html'
    model = Store
    context_object_name = 'store'

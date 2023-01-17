from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Case, Value, When
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, UpdateView

from apps.forms.products import UpdateStreamForm
from apps.models import Stream, Store, Product, Category


class MainPageView(TemplateView):
    queryset = Product.objects.all()
    template_name = 'apps/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['products'] = Product.objects.all()[:6]
        context['categories'] = Category.objects.all()
        return context


class StreamPageListView(LoginRequiredMixin, ListView, UpdateView):
    template_name = 'apps/admin/stream.html'
    queryset = Stream.objects.order_by('id')
    form_class = UpdateStreamForm
    object = Stream
    context_object_name = 'streams'
    paginate_by = 18

    def get(self, request, *args, **kwargs):
        # id = int(request.GET['id'])
        # Stream.objects.filter(id=id).delete()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # self.get_object()
        id = int(request.POST['id'])
        Stream.objects.filter(id=id).update(is_area=Case(
            When(is_area=True, then=Value(False)),
            default=Value(True)
        ))
        return super().post(self, request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['url'] = get_current_site(self.request)
        return context


class StreamDeleteView(TemplateView):
    model = Stream
    context_object_name = 'stream'
    success_url = reverse_lazy('stream_page_view')

    def get(self, request, *args, **kwargs):
        id = int(request.GET['id'])
        Stream.objects.filter(id=id).delete()
        return super().get(request, *args, **kwargs)


class StoreDetailView(DetailView):
    template_name = 'apps/store_detail.html'
    model = Store
    context_object_name = 'store'

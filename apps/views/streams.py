from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Case, Value, When
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView

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


class StreamPageListView(LoginRequiredMixin, ListView):
    template_name = 'apps/admin/stream.html'
    queryset = Stream.objects.all()
    context_object_name = 'streams'
    paginate_by = 18


class StreamUpdateView(UpdateView):
    form_class = UpdateStreamForm
    queryset = Stream.objects.all()
    object = Stream
    fields = ('is_area',)

    # update qilish
    def put(self, *args, **kwargs):
        self.get_object().is_area = not self.get_object().is_area
        return super().put(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        id = int(request.POST['id'])
        Stream.objects.filter(id=id).update(is_area=Case(
            When(is_area=True, then=Value(False)),
            default=Value(True)
        ))
        return super().post(self, request, *args, **kwargs)


class StreamDeleteView(DeleteView):
    model = Stream
    context_object_name = 'stream'
    success_url = reverse_lazy('stream_page_view')

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        return super().delete(request, *args, **kwargs)



class StoreDetailView(DetailView):
    template_name = 'apps/store_detail.html'
    model = Store
    context_object_name = 'store'

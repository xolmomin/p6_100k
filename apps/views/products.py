from django.db.models import F
from django.http import JsonResponse
from django.views.generic import FormView, DetailView

from apps.forms import CreateCommentForm
from apps.models import Product, Comment, Region, Stream


class ProductDetailView(FormView, DetailView):
    template_name = 'apps/product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'
    form_class = CreateCommentForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['comment'] = Comment.objects.all()
        context['regions'] = Region.objects.all()
        return context


def completed(request, *args, **kwargs):
    # stream = Stream.objects.get(id=id)
    # stream.is_area = not stream.is_area
    # stream.save()
    Stream.objects.filter(id=id).update(is_area=~F('is_area'))
    return JsonResponse({'status': 200})

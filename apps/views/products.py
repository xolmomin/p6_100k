import json
import urllib
from urllib.parse import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView, DetailView, ListView

from apps.forms import CreateCommentForm, OrderForm
from apps.models import Product, Comment, Category, Stream
from apps.models.users import Favorite
from apps.views import MainPageView


class GetStreamView(View):
    def get(self, request, *args, **kwargs):
        _id = kwargs.get('pk')
        stream = Stream.objects.filter(id=_id).first()
        if stream.product:
            slug = stream.product.slug
            redirect_url = reverse('product_detail', args=(slug,))
            parameters = urlencode({'stream': stream.pk})
            return redirect(f'{redirect_url}?{parameters}')
        return redirect('main_page_view')


class ProductDetailView(FormView, DetailView):
    template_name = 'apps/product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'
    form_class = CreateCommentForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['comment'] = Comment.objects.filter(product__slug=self.request.path.split('/')[-1])
        return context

    def get(self, request, *args, **kwargs):
        stream_id = self.request.GET.get('stream')
        if stream_id:
            Stream.objects.filter(pk=stream_id).update(views=F('views') + 1)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)
        data = {
            'product': product,
            'name': request.POST.get('name'),
            'content': request.POST.get('content'),
            'rate': request.POST.get('rate')
        }
        form = self.form_class(data)
        if form.is_valid():
            form.save()
        return redirect('product_detail', slug)


class ProductOrderView(MainPageView, FormView):
    template_name = 'apps/index.html'
    form_class = OrderForm
    success_url = reverse_lazy('order')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CategoryDetail(ListView):
    template_name = 'apps/category_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        qs = self.get_queryset()
        context['categories'] = Category.objects.all()
        context['products'] = qs
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        if category := self.request.GET.get('category'):
            return qs.filter(category__slug=category)
        return qs


class FavoriteListView(LoginRequiredMixin, ListView):
    model = Stream
    template_name = 'apps/favorite.html'

    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        id = body['id']
        b = True
        if id:
            try:
                Favorite.objects.get(product_id=id).delete()
            except:
                pr = Favorite.objects.create(product_id=id, user=request.user)
                b = False
        return JsonResponse({'b': b})

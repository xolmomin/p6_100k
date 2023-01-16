import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, ListView

from apps.forms import CreateCommentForm, OrderForm
from apps.models import Product, Comment, Category, Stream
from apps.models.users import Favorite
from apps.views import MainPageView


class ProductDetailView(FormView, DetailView):
    template_name = 'apps/product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'
    form_class = CreateCommentForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['comment'] = Comment.objects.filter(product__slug=self.request.path.split('/')[-1])
        return context

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


class GetStreamView(DetailView):
    pk_url_kwarg = 'pk'
    model = Stream

    def render_to_response(self, context, **response_kwargs):
        return super().render_to_response(context, **response_kwargs)


class FavoriteListView(ListView):
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

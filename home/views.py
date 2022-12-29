from http.client import HTTPResponse # Jquery Ajax İle aramada Otomatik tamamlama fonksiyonu için import
import json # Jquery Ajax İle aramada Otomatik tamamlama fonksiyonu için import
from django.shortcuts import render, redirect
from product.models import *
from home.models import *
from home.forms import *
from order.models import *
from django.contrib import messages
from django.db.models import Q
from django.views.generic.edit import FormView
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.

def index(request):
    current_user=request.user
    setting = Setting.objects.get(pk=1) 
    category = Category.objects.all()
    category_list = Category.objects.all()[:6]
    just_came = Product.objects.all()[:8]
    trending_products = Product.objects.all()[:8]
    randomproducts = Product.objects.all().order_by('?')[:8]
    request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
    return render(request, 'index.html', context={
        'setting':setting,
        'category':category,
        'just_came':just_came,
        'trending_products':trending_products,
        'category_list':category_list,
        'randomproducts':randomproducts
    })

def about(request):
    setting = Setting.objects.get(pk=1) 
    category = Category.objects.all()
    return render(request, 'about.html', context={
        'setting':setting,
        'category':category
    })

def referance(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    return render(request, 'referance.html', context={
        'setting':setting,
        'category':category
    })


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/submit/'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        email = form.cleaned_data['email']

        mail = EmailMessage(
            f'{name}, Tarafından Mesaj Gönderildi',
            f'Konu: {subject}\n\nEmail: {email}\n\nMesaj: {message}\n\n',
            f'"YENİ MESAJ" <{email}>', # email'in kimden (from) geldiğini yazdık.
            [settings.EMAIL_ADMIN], # email'in kime (to) gideceğini belirledik.
                reply_to=[f'{email}'], # gmail'de yanıtlama yapıldığında otomatik olarak mesaj gönderenin email adresini seçtirdik.
        )
        mail.send()
        form.save()
        messages.success(self.request, 'Mesajınız başarıyla gönderildi.')
        return super().form_valid(form)


# Search
def search_product(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    products = Product.objects.all()
    query = ''
    if request.method == 'GET':
        query = request.GET.get('query')
        products = products.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(category__title__icontains=query) |
            Q(keywords__icontains=query) |
            Q(detail__icontains=query)
            ).distinct()
    return render(request, 'search.html', context={
        'products':products,
        'category':category,
        'query':query,
        'setting':setting
    })

# def search_product(request):
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             category = Category.objects.all()
#             query = form.cleaned_data['query']
#             products = Product.objects.filter(
#                 Q(title__icontains=query)|
#                 Q(category__title__icontains=query)|
#                 Q(keywords__icontains=query)|
#                 Q(description__icontains=query)|
#                 Q(detail__icontains=query)
#             ).distinct()
#             return render(request, 'search.html', context={
#                 'category':category,
#                 'products':products
#             })
#     return redirect('search')


# Jquery Ajax İle aramada Otomatik tamamlama fonksiyonu
def product_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        product = Product.objects.filter(
                Q(title__icontains=q)|
                Q(category__title__icontains=q)|
                Q(keywords__icontains=q)|
                Q(description__icontains=q)|
                Q(detail__icontains=q)
            ).distinct()
        results = []
        for rs in product:
            product_json = {}
            product_json = rs.title + "," + rs.keywords + "," + rs.description + "," + rs.detail
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HTTPResponse(data, mimetype)


def faq(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    faq = Faq.objects.all().order_by('ordernumber')
    return render(request, 'faq.html', context={
        'setting':setting,
        'category':category,
        'faq':faq
    })
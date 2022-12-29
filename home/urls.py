from django.urls import path
from home.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('search/', search_product, name='search'),
    path('search_auto/', product_search_auto, name='product_search_auto'),
    path('referance/', referance, name='referance'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('submit/', TemplateView.as_view(template_name='success_submit.html'), name='submit'),
    path('sss/', faq, name='faq'),
]
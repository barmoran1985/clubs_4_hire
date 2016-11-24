from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.all_products, name='rental'),
    url(r'^(?P<id>\d+)/$', views.product_details, name='details')
]

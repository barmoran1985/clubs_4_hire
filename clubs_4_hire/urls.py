"""clubs_4_hire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as accounts_urls
from hello import views as hello_views
from django.views.static import serve
from settings import MEDIA_ROOT

from products import views as product_views
from django.conf.urls import url, include
from rental import views as paypal_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', hello_views.get_index, name='index'),
    url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'', include(accounts_urls)),
    url(r'^rental/', product_views.all_products, name='rental'),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel)
]


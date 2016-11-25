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
from django.contrib import admin
from accounts import urls as accounts_urls
from hello import views as hello_views
from django.views.static import serve
from settings import MEDIA_ROOT

from django.conf.urls import url, include
from rental import views as paypal_views
from blog import views as blog_views
from products import urls as products_urls
from cart import urls as cart_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', blog_views.top_post1, name='index'),
    url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'', include(accounts_urls)),
    url(r'^rental/', include(products_urls)),
    url(r'cart/', include(cart_urls)),
    url(r'^paypal-return', paypal_views.paypal_return, name='return'),
    url(r'^paypal-cancel', paypal_views.paypal_cancel, name='cancel')
]


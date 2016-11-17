from django.conf.urls import url, include
from paypal.standard.ipn import urls as paypal_urls
from rental import views as paypal_views

urlpatterns = [
    url(r'^JD8FJB88ashssa8HJHS&^&**HJHJgchgkj/', include(paypal_urls)),

]

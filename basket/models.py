from __future__ import unicode_literals

from django.db import models

# Create your models here.


# class Basket(models.Model):
#
#     product =
#     price =
#     name =
#






# class Post(models.Model):
#
#     author = models.ForeignKey(User)
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     created_date = models.DateTimeField(
#         default=timezone.now
#     )
#     published_date = models.DateTimeField(
#         blank=True, null=True
#     )
#     views = models.IntegerField(default=0) #records how often a post is seen
#
#     tag = models.CharField(max_length=30, blank=True, null=True)
#
#     image = models.ImageField(upload_to="images", blank=True, null=True)


# class Product(models.Model):
#
#     name = models.CharField(max_length=254, default='')
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     image = models.ImageField(upload_to="images", default='no_product.png')
#
#     @property
#     def paypal_form(self):
#         paypal_dict = {
#             "business": settings.PAYPAL_RECEIVER_EMAIL,
#             "amount": self.price,
#             "currency": "EUR",
#             "item_name": self.name,
#             "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
#             "notify_url": settings.PAYPAL_NOTIFY_URL,
#             "return_url": "%s/paypal-return" % settings.SITE_URL,
#             "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
#         }
#
#         return PayPalPaymentsForm(initial=paypal_dict)
#
#     def __unicode__(self):
#         return self.name
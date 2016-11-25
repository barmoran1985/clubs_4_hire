from django.views.decorators.csrf import csrf_exempt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.template.loader import render_to_string
from django.template.loader import get_template
from django.template import Context
from products.models import Product
from django.shortcuts import render, get_object_or_404

# Create your views here.


# def rd_email(user, product):
#     prod = get_object_or_404(Product, pk=5)
#     str = render_to_string("email.html", {'user': user, 'product': product})
#     me = "barmoran5@gmail.com"
#     you = "barmoran5@gmail.com"
#     msg = MIMEMultipart('alternative')
#     msg['Subject'] = "Clubs4Hire-Your Invoice"
#     msg['From'] = me
#     msg['To'] = "barmoran5@gmail.com"
#     part1 = str
#     msg.attach(part1)
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.ehlo()
#     s.starttls()
#     s.ehlo()
#     s.login('barmoran5@gmail.com', 'mafiaethos')
#     s.sendmail(me, you, msg)
#     return s.quit()
#
#
# def html_mail(request, id):
#     product = get_object_or_404(Product, pk=id)
#     me = "barmoran5@gmail.com"
#     you = "barmoran5@gmail.com"
#     msg = MIMEMultipart('alternative')
#     msg['Subject'] = "Clubs4Hire-Your Invoice"
#     msg['From'] = me
#     msg['To'] = you
#     part1 = render_to_string('../rental/templates/invoice.txt', {'product': product})
#     part2 = render_to_string('../rental/templates/invoice.html', {'product': product})
#     msg.attach(part1)
#     msg.attach(part2)
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#     s.ehlo()
#     s.starttls()
#     s.ehlo()
#     s.login('barmoran5@gmail.com', 'mafiaethos')
#     s.sendmail(me, you, msg)
#     return s.quit()


@csrf_exempt
def paypal_return(request):
    args = {'post': request.POST, 'get': request.GET}
    # rd_email(request.user, 5)
    return render(request, 'paypal_return.html', args)


def paypal_cancel(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal_cancel.html', args)








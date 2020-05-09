import hashlib

from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import loader

from APP.models import Cart
from AXF.settings import EMAIL_HOST_USER, SERVER_PORT, SERVER_HOST

'''
# 修改全局的时区配置
set global time_zone = '+8:00';
flush privileges;
'''
'''
(Django2) E:\workspace\AXF>cd D:\Redis-x64-3.2.100
(Django2) E:\workspace\AXF>d:
(Django2) D:\Redis-x64-3.2.100>redis-server.exe redis.windows.conf
'''


def hash_str(source):
    return hashlib.new('sha512', source.encode('utf-8')).hexdigest()


def send_email_activate(username, receive, u_token):
    subject = 'AXF Activate'
    message = 'Hello'
    from_email = EMAIL_HOST_USER
    recipient_list = [receive, ]
    data = {
        'username': username,
        'activate_url': 'http://{}:{}/axf/activate/?u_token={}'.format(SERVER_HOST, SERVER_PORT, u_token)
    }
    html_message = loader.get_template('user/activate.html').render(data)
    send_mail(subject=subject, message="", html_message=html_message, from_email=from_email,
              recipient_list=recipient_list)


def get_total_price():
    carts = Cart.objects.filter(c_is_select=True)
    total = 0
    for cart in carts:
        total += cart.c_goods_num * cart.c_goods.price

    return "{:.2f}".format(total)


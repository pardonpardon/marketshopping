from django.conf.urls import url
from django.urls import path

from APP import views

app_name = '[APP]'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('market/', views.market, name='market'),
    url(r'^marketwithparams/(?P<typeid>\d+)/(?P<childcid>\d+)/(?P<order_rule>\d+)/', views.market_with_params,
        name='market_with_params'),
    path('cart/', views.cart, name='cart'),
    path('mine/', views.mine, name='mine'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('checkuser/', views.check_user, name='check_user'),
    path('activate/',views.activate,name='activate'),
    path('addtocart/',views.add_to_cart,name='add_to_cart'),
    path('changecartstate/',views.change_cart_state,name='change_cart_state'),
    path('subshopping/',views.sub_shopping,name='sub_shopping'),
    path('allselect/',views.all_select,name='allselect'),
    path('makeorder/',views.make_order,name='make_order'),
    path('orderdetail/',views.order_detail,name='order_detail'),
    path('orederlistnotpay/',views.oreder_list_not_pay,name='oreder_list_not_pay'),
    path('payed/',views.payed,name='payed'),
    path('alipay/',views.alipay,name='alipay'),

]


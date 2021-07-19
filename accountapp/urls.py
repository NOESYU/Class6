from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    #name설정한 이유가 path 스펠링 틀릴경우 있으니 name으로 가라 하게끔
    path('create/', AccountCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    #pk번째 account객체의 detail을 보겠다. key값 고유번호 느낌
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
]
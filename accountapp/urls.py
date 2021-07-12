from django.urls import path

from accountapp.views import hello_world

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    #name설정한 이유가 path 스펠링 틀릴경우 있으니 name으로 가라 하게끔
]
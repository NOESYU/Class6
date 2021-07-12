from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == 'POST':
        temp = request.POST.get('input_text')

        new_hello_world = HelloWorld() #새로운객체만들고
        new_hello_world.text = temp
        new_hello_world.save() #DB안에 저장하고 아래서 불러오는건 저장된걸 불러옴

        #원래대로 했으면 새로고침할때마다 DB에 넘겨준 데이터가 추가되었었음.
        #리다이렉트 -> accountapp의 hello_world name을 가진걸 찾아 reverse로 주소추적
        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    elif request.method == 'GET':
        hello_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_list' : hello_list})





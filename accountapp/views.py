from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == 'POST':
        temp = request.POST.get('input_text')

        new_hello_world = HelloWorld() #새로운객체만들고
        new_hello_world.text = temp
        new_hello_world.save() #DB안에 저장하고 아래서 불러오는건 저장된걸 불러옴

        #이제 단일객체 읽는게 아닌 모든 객체 불러읽기 get는 단일 all은 전체
        hello_list = HelloWorld.objects.all() #db에 저장된 내용들을 all가져옴
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_list': hello_list})

    elif request.method == 'GET':
        hello_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_list' : hello_list})





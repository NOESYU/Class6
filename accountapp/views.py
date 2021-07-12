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
        return render(request, 'accountapp/hello_world.html',
                      context={'new_hello_world': new_hello_world})

    elif request.method == 'GET':
        return render(request, 'accountapp/hello_world.html',
                      context={'text':'Get Method'})





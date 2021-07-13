from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld

#function based view
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


#class based view
class AccountCreateView(CreateView):
    model = User #쟝고 기본제공 계정모델
    form_class = UserCreationForm #쟝고 기본제공 폼
    success_url = reverse_lazy('accountapp:hello_world')
    #class 에서 reverse_lazy로 사용해야함. 객체가 생성 이후 필요할때 불러야 하므로
    template_name = 'accountapp/create.html'


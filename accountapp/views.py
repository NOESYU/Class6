from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld

#function based view
def hello_world(request):
    # authenticated 안되면 login 페이지로 redirect되게
    if request.user.is_authenticated:
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

    else:
        return HttpResponseRedirect(reverse('accountapp:login'))

#class based view #CRUD 패턴
class AccountCreateView(CreateView):
    model = User #쟝고 기본제공 계정모델
    form_class = UserCreationForm #쟝고 기본제공 폼
    success_url = reverse_lazy('accountapp:hello_world')
    #class 에서 reverse_lazy로 사용해야함. 객체가 생성 이후 필요할때 불러야 하므로
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user' #어떤 이름으로 접근할 것인지
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    # authenticated 안되면 login 페이지로 redirect되게, get/post 방식 둘 다 아래 delete view도
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))
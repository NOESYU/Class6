from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorator import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld

#function based view
#login authenticated 관련 decorator -> django에 구현되어있음

#디폴트 login_url로 안했으면 login_url 입력해주면 됨. 입력안해주면 not found 뜸
@login_required(login_url=reverse_lazy('accountapp:login'))
def hello_world(request):
    # authenticated 안되면 login 페이지로 redirect되게
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


#django 에서 decorator 넘겨줄때 단일도 가능한데 list 로도 가능함
#login_required는 리다이렉트 해줘야하는데 aor 는 아니니까 login_url 안 넣어줘도 됨
has_ownership = [login_required(login_url=reverse_lazy('accountapp:login')),
                 account_ownership_required]

# 클래스내에서 만들어진 메소드에 적용하기 위해
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.pk}) #accountapp에서는 그 자체로 target_user

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

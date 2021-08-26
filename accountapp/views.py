from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorator import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld

#function based view
#login authenticated 관련 decorator -> django에 구현되어있음

#디폴트 login_url로 안했으면 login_url 입력해주면 됨. 입력안해주면 not found 뜸
from articleapp.models import Article


#class based view #CRUD 패턴
class AccountCreateView(CreateView):
    model = User #쟝고 기본제공 계정모델
    form_class = UserCreationForm #쟝고 기본제공 폼
    success_url = reverse_lazy('articleapp:list')
    #class 에서 reverse_lazy로 사용해야함. 객체가 생성 이후 필요할때 불러야 하므로
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user' #어떤 이름으로 접근할 것인지
    template_name = 'accountapp/detail.html'

    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list, **kwargs)


# django 에서 decorator 넘겨줄때 단일도 가능한데 list 로도 가능함
# login_required는 리다이렉트 해줘야하는데 aor 는 아니니까 login_url 안 넣어줘도 됨
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
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/delete.html'

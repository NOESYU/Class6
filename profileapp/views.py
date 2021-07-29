from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# 데코레이터로 접근 제한하기
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    #오버라이딩
    def form_valid(self, form): #폼에 형식이맞게 들어왔는지 이런거 다 검사하고 난 다음에 실행됨.
        form.instance.user = self.request.user # 유저와맞는지 서버에서 받아와 비교
        # form은 image, nickname, message만 갖고있으니까 instance에 있는 user와 비교
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

# 데코레이터는 접근제한하는게 detail페이지가 아니라 권한없는 사람의 update페이지 접근을 막음.
@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    def get_success_url(self): # Mypage 띄우고싶은데 이전방법으로는 pk값을 바로 할수없어서 self.object.user = target_user
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

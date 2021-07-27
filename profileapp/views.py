from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    #오버라이딩
    def form_valid(self, form): #폼에 형식이맞게 들어왔는지 이런거 다 검사하고 난 다음에 실행됨.
        form.instance.user = self.request.user # 유저와맞는지 서버에서 받아와 비교
        # form은 image, nickname, message만 갖고있으니까 instance에 있는 user와 비교
        return super().form_valid(form)
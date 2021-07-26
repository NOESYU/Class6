from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm): #쟝고 기본 제공 모델폼 상속
    class Meta:
        model = Profile # Profile 모델 가져온것
        # 유저정보는 서버내에서 직접 요청한 사람이랑 맞는지 확인하게 하고 직접받는 필드는 3개만 받음
        fields = ['image', 'nickname', 'message'] # 입력을 받을 필드 3개
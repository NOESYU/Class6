# update form에서는 아이디 수정이 노출안되게 해야함 -> usercreationform은 노출됨
from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # 부모 클래스에 init을 가져옴 -> 부모에서 하는거 그대로 다 이용
        #usercreationform 의 field 중 username(id입력) 하는 것의 disabled 설정
        self.fields['username'].disabled = True
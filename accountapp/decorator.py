# 이제 자기 페이지 아닌 남의 delete, update에 접근못하게
# 요청한 유저와 target 유저가 동일한지 확인
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        # 디비에서 target user 직접 빼오기 단일객체니까 get 사용 kwagrs에 주소창의 pk값 있음
        target_user = User.objects.get(pk=kwargs['pk'])

        if target_user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return decorated
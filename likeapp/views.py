from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    def get(self, request, *args, **kwargs):
        user = request.user
        article = Article.objects.get(pk=kwargs['article_pk']) # DB의 article객체에서 get으로 하나 뽑아옴

        like_record = LikeRecord.objects.filter(user=user,
                                                article=article)

        if like_record.exists(): # 이미 좋아요상태면 게시글 디테일로 그냥 돌아가라고
            return HttpResponseRedirect(reverse('articleapp:detail',
                                                kwargs={'pk':kwargs['article_pk']}))
        else:
            LikeRecord(user=user, article=article).save() # 어떤유저가 어떤게시글에 좋아요한지 기록
            article.like += 1  # 좋아요수 올리고
            article.save()  # 디비에 저장

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk':kwargs['article_pk']})
from django.db import models
from django.urls import reverse

# Create your models here.    
# 블로그 글 (제목, 작성일, 대표 이미지, 내용, 분류)
class Post(models.Model):
    title = models.CharField(max_length = 200)  # 제목
    subtitle = models.CharField(max_length = 200)  # 서브 제목
    writer = models.CharField(max_length = 200) # 작성자
    content = models.TextField()    # ?
    createDate = models.DateTimeField(auto_now_add = True)  # 작성 날짜
    updateDate = models.DateTimeField(auto_now_add = True)  # 업데이트 날짜

    def __str__(self):
        return self.title
    
    # 1번 글의 경우 -> post/1
    def get_absolute_url(self):
        return reverse("post", args = [str(self.id)])

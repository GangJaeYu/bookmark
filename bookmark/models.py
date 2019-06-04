from django.db import models
from django.urls import reverse

class Bookmark(models.Model):
    site_name = models.CharField(max_length = 100)
    url = models.URLField('Site URL')

    # 클래스의 오브젝트를 출력할 때 나타날 내용을 결정하는 메서드
    def __str__(self):
        # 객체 출력시 나타나는 값
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    # BookmarkUpdateview에서 success_url 대신 사용
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

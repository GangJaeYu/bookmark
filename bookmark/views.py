from django.shortcuts import render
from django.views.generic.list import ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.views.generic.detail import DetailView

from .models import Bookmark

class BookmarkListView(ListView):
    """
	ListView 디폴트 지정 속성
	1) 컨텍스트 변수 : object_list
	2) 템플릿 파일 : bookmark_list.html (모델명소문자_list.html)
	"""
    model = Bookmark
    paginate_by = 3

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    # generic view에서는 reverse_lazy 사용
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateview(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

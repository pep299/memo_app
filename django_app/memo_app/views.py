from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Memo
from .forms import PostForm

def index(request, now_page=1):
    memos = Memo.objects.all()
    #TODO 一旦レコード件数仮置き
    record_number = 10
    page = Paginator(memos, record_number)
    params = {
        'form': PostForm(),
        'page': page.get_page(now_page)
    }
    print(dir(page.get_page(now_page)))
    for i in page.get_page(now_page):
        print(i)
    return render(request, 'memo_app/index.html', params)

def post(request):
    PostForm(request.POST, instance = Memo()).save()
    return redirect(to='/')
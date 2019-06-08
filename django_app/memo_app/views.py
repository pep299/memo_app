from django.shortcuts import render, redirect
from .models import Memo
from .forms import PostForm

def index(request):
    memos = Memo.objects.all()
    params = {
        'memos': memos,
        'form': PostForm(),
    }
    return render(request, 'memo_app/index.html', params)

def post(request):
    PostForm(request.POST, instance = Memo()).save()
    return redirect(to='/')
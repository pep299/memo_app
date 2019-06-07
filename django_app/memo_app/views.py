from django.shortcuts import render
from .models import Memo

def index(request):
    memos = Memo.objects.all()
    params = {
        'memos': memos,
    }
    return render(request, 'memo_app/index.html', params)
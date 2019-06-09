from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Memo
from .forms import PostForm, RecordNumberForm

SESSION_KEY_RECORD_NUMBER = 'record_number'
DEFALUT_RECORD_NUMBER = 10

def index(request, now_page=1):
    memos = Memo.objects.all()
    # レコード件数
    record_number = \
            request.session[SESSION_KEY_RECORD_NUMBER] \
            if 'record_number' in request.session else \
            DEFALUT_RECORD_NUMBER
    record_number_form = RecordNumberForm()
    record_number_form.initial = {'record_number': str(record_number)}

    #TODO ソート順

    page = Paginator(memos, record_number)

    params = {
        'form': PostForm(),
        'page': page.get_page(now_page),
        'record_number_form': record_number_form
    }
    return render(request, 'memo_app/index.html', params)

def set_record_number(request):
    request.session[SESSION_KEY_RECORD_NUMBER] = request.POST['record_number']
    return redirect(to='/')

def post(request):
    PostForm(request.POST, instance = Memo()).save()
    return redirect(to='/')
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from .models import Memo
from .forms import PostForm, RecordNumberForm, OrderOptionForm

SESSION_KEY_RECORD_NUMBER = 'record_number'
SESSION_KEY_ORDER_OPTION = 'order_option'
DEFALUT_RECORD_NUMBER = 10
DEFALUT_ORDER_OPTION = 'desc'

def index(request, now_page=1):
    # レコード件数
    record_number = \
            request.session[SESSION_KEY_RECORD_NUMBER] \
            if 'record_number' in request.session else \
            DEFALUT_RECORD_NUMBER
    record_number_form = RecordNumberForm()
    record_number_form.initial = {'record_number': str(record_number)}

    # ソート順
    order_option = \
            request.session[SESSION_KEY_ORDER_OPTION] \
            if 'order_option' in request.session else \
            DEFALUT_ORDER_OPTION
    order_option_form = OrderOptionForm()
    order_option_form.initial = {'order_option': order_option}

    # メモ一覧取得
    memos = \
            Memo.objects.filter(user=request.user).order_by('update_datetime').reverse() \
            if 'desc' == order_option else \
            Memo.objects.filter(user=request.user).order_by('update_datetime')
    page = Paginator(memos, record_number)

    params = {
        'form': PostForm(),
        'page': page.get_page(now_page),
        'record_number_form': record_number_form,
        'order_option_form': order_option_form,
    }
    return render(request, 'memo_app/index.html', params)

def set_record_number(request):
    request.session[SESSION_KEY_RECORD_NUMBER] = request.POST['record_number']
    return redirect(to='/')

def set_order_option(request):
    request.session[SESSION_KEY_ORDER_OPTION] = request.POST['order_option']
    return redirect(to='/')

def post(request):
    form = PostForm(request.POST, instance=Memo())
    if form.is_valid():
        user = get_user_model().objects.get(id=request.user.id)
        memo = Memo(content=request.POST.get('content'), user=user)
        memo.save()
    else:
        print(form.errors)

    return redirect(to='/')
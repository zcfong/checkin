from django.shortcuts import render
from .models import ContactSeat, Active
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


def index(request):
    active = request.GET.get('active')
    exists = Active.objects.filter(title=active).exists()
    status = 0
    if not exists:
        active = '该活动不存在!'
        status = 1

    context = {
        'active': active,
        'status': status
    }
    return render(request, 'index.html', context)


def query(request):
    active = request.GET.get('active')
    guest = request.GET.get('guest')
    queryset = ContactSeat.objects.filter(active__title=active)
    queryset = queryset.filter(guest__startswith=guest). \
        values('pk', 'guest', 'seat', )

    resp = {
        'stat': 1,
        'result': list(queryset)
    }
    return JsonResponse(resp, safe=False)


@require_http_methods(['PUT', ])
def sign(request, pk):
    ContactSeat.objects.filter(pk=pk).update(is_sign=True)

    resp = {
        'stat': 1,
        'result': '签到成功'
    }
    return JsonResponse(resp, safe=False)

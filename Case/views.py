import datetime
from django.http import JsonResponse
from .models import OrderBookHistory, OrderBookSellHistory
from .getData import getDataProcess
from dateutil.relativedelta import relativedelta


def getData(request):
    if request.method == "POST":
        getDataProcess()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error'})


def getDaily(request, day=1):
    d = datetime.date.today() - datetime.timedelta(days=int(day))
    buyData = OrderBookHistory.objects.filter(date__gt=d)
    sellData = OrderBookSellHistory.objects.filter(date__gt=d)

    return JsonResponse({'status': 'ok', 'data': {'buyData': _parse(buyData), 'sellData': _parse(sellData)}})


def getWeekly(request, week=1):
    weeks = datetime.date.today() - datetime.timedelta(weeks=int(week))
    buyData = OrderBookHistory.objects.filter(date__gt=weeks)
    sellData = OrderBookSellHistory.objects.filter(date__gt=weeks)

    return JsonResponse({'status': 'ok', 'data': {'buyData': _parse(buyData), 'sellData': _parse(sellData)}})


def getMonthly(request, month=1):
    date = datetime.date.today() - relativedelta(months=int(month))
    buyData = OrderBookHistory.objects.filter(date__gt=date)
    sellData = OrderBookSellHistory.objects.filter(date__gt=date)

    return JsonResponse({'status': 'ok', 'data': {'buyData': _parse(buyData), 'sellData': _parse(sellData)}})


def getYears(request, years=1):
    date = datetime.date.today() - relativedelta(years=int(years))
    buyData = OrderBookHistory.objects.filter(date__gt=date)
    sellData = OrderBookSellHistory.objects.filter(date__gt=date)

    return JsonResponse({'status': 'ok', 'data': {'buyData': _parse(buyData), 'sellData': _parse(sellData)}})


def _parse(data):
    volume = 0
    minValue = []
    maxValue = []
    for a in data:
        volume += a.total
        minValue.append(a.minFiled)
        maxValue.append(a.maxFiled)

    return {'min': min(minValue), 'max': max(maxValue), 'volume': volume}

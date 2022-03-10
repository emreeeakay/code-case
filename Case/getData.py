import json
import requests
from django.http import JsonResponse
from .models import OrderBookHistory, OrderBookSellHistory


def getDataProcess():
    url = "https://www.bitexen.com/api/v1/order_book/BTCTRY/"
    r = requests.get(url)
    content = json.loads(r.content)['data']
    buyersOrders = _dataProcess(content['buyers'])
    sellerOrders = _dataProcess(content['sellers'])

    data = OrderBookHistory()
    data.maxFiled = max(buyersOrders['prices'])
    data.minFiled = min(buyersOrders['prices'])
    data.total = sum(buyersOrders['prices'])
    data.average = _calculateAverage(buyersOrders['prices'])
    data.save(data)

    sellData = OrderBookSellHistory()
    sellData.maxFiled = max(sellerOrders['prices'])
    sellData.minFiled = min(sellerOrders['prices'])
    sellData.total = sum(sellerOrders['prices'])
    sellData.average = _calculateAverage(sellerOrders['prices'])
    sellData.save()
    print('cron work ')
    return JsonResponse({'status': 'ok'})


def _dataProcess(prices):
    price = []
    amount = []
    for data in prices:
        price.append(float(data['orders_price']))
        amount.append(float(data['orders_total_amount']))

    return {'prices': price, 'amount': amount}


def _calculateAverage(prices):
    return sum(prices) / len(prices)

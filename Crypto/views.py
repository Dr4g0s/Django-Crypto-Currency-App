from django.shortcuts import render
import requests, json
# Create your views here.

def crypto(request):
    price = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX,BNB,BSV,XMR,DASH,XTZ,ATOM,LINK,NEO,ETC&tsyms=USD,EUR").json()
    api = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN").json()
    context = {
        "api"   : api,
        "price" : price,
    }
    return render(request, "crypto/index.html", context)

def prices(request):
    if request.method == 'POST':
        result = request.POST.get('result')
        if not result:
            price = "Not Found"
        else:
            result = result.upper()
            api    = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD,EUR".format(result))
            price  = api.json()
        return render(request, 'crypto/prices.html', {'prices' : price})
    return render(request, 'crypto/prices.html', {'prices' : None})

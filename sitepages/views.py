from django.shortcuts import render

# Create your views here.
def index(request):
      return render(request, "index.html")

def about(request):
      return render(request, "about.html")

# оплата услуг
def oplata_main(request):
      return render(request, "oplata_uslug/index.html")

# Сотовая связь

def oplata_mobile(request):
      return render(request, "oplata_uslug/mobile/index.html")

def oplata_mobile_template(request, operator):
      step = "number"

      number, payout = "", ""

      if request.method == "POST":
            payout = request.POST.get("payout")

            step = "kvitanc"
      elif request.method == "GET":
            if request.GET.get("number1") and request.GET.get("number2") and request.GET.get("number3") and request.GET.get("number4"):
                  number1 = request.GET.get("number1")
                  number2 = request.GET.get("number2")
                  number3 = request.GET.get("number3")
                  number4 = request.GET.get("number4")

                  number = f"+7 ({number1}) {number2} {number3} {number4}"
                  step = "balance"

      return render(request, "oplata_uslug/mobile/topup.html", context={"step":step, "number": number, "payout": payout, "operator": operator})

def oplata_mobile_mts(request):
      return oplata_mobile_template(request, "МТС Россия")

def oplata_mobile_beelinerus(request):
      return oplata_mobile_template(request, "Билайн")

def oplata_mobile_tele2(request):
      return oplata_mobile_template(request, "Tele-2 Россия")

def oplata_mobile_megafon(request):
      return oplata_mobile_template(request, "Мегафон")

# Интернет и телефония

def oplata_internet_template(request, operator):
      step = "number"

      number, payout = "", ""

      if request.method == "POST":
            payout = request.POST.get("payout")

            step = "kvitanc"
      elif request.method == "GET":
            if request.GET.get("lic"):
                  number = request.GET.get("lic")
                  step = "balance"

      return render(request, "oplata_uslug/internet/topup.html", context={"step":step, "number": number, "payout": payout, "operator": operator})

def oplata_internet(request):
      return render(request, "oplata_uslug/internet/index.html")

def oplata_internet_rostelekom(request):
      return oplata_internet_template(request, "Ростелеком")

def oplata_internet_mts(request):
      return oplata_internet_template(request, "МТС Россия")

def oplata_internet_beeline(request):
      return oplata_internet_template(request, "Билайн")

def oplata_internet_beelinewifi(request):
      return oplata_internet_template(request, "Билайн WIFI")

def oplata_internet_domru(request):
      return oplata_internet_template(request, "Дом.RU")

def oplata_internet_megafon(request):
      return oplata_internet_template(request, "Мегафон")

# Телевидение
def oplata_tv_template(request, operator):
      step = "number"

      number, payout = "", ""

      if request.method == "POST":
            payout = request.POST.get("payout")

            step = "kvitanc"
      elif request.method == "GET":
            if request.GET.get("lic"):
                  number = request.GET.get("lic")
                  step = "balance"

      return render(request, "oplata_uslug/tv/topup.html", context={"step":step, "number": number, "payout": payout, "operator": operator})

def oplata_tv(request):
      return render(request, "oplata_uslug/tv/index.html")

def oplata_tv_ntv(request):
      return oplata_tv_template(request, "НТВ")

# Банковские услуги

def oplata_bank(request):
      return render(request, "oplata_uslug/bank/index.html")

def oplata_bank_template(request, operator):
      step = "number"

      number, payout = "", ""

      if request.method == "POST":
            payout = request.POST.get("payout")

            step = "kvitanc"
      elif request.method == "GET":
            if request.GET.get("card"):
                  number = request.GET.get("card")
                  step = "balance"

      return render(request, "oplata_uslug/bank/topup.html", context={"step":step, "number": number, "payout": payout, "operator": operator})

def oplata_bank_mc(request):
      return oplata_bank_template(request, "Mastercard")

def oplata_bank_visa(request):
      return oplata_bank_template(request, "Visa")

def oplata_bank_rosselhoz(request):
      return oplata_bank_template(request, "Россельхозбанк")

def oplata_bank_beeline(request):
      return oplata_bank_template(request, "Билайн Банк")

def oplata_bank_mir(request):
      return oplata_bank_template(request, "Мир")

def oplata_bank_zarubezh(request):
      return oplata_bank_template(request, "Зарубежная карта")

def oplata_bank_per(request):
      return render(request, "oplata_uslug/bank/per/index.html")

def oplata_games(request):
      return render(request, "oplata_uslug/games/index.html")

def oplata_games_steam(request):
      step = "number"
      number, payout = "", ""
      currency = request.GET.get("currency")
      showcurrency = "хз"

      if currency == "tenge":
            showcurrency = "₸"
      else:
            showcurrency = "₽"

      nextstep = request.GET.get("nextstep")
      if nextstep == "balance":
            step = "balance"
      elif nextstep == "success":
            payout = request.GET.get("payout")
            step = "success"

      return render(request, "oplata_uslug/games/steam.html", context={"step":step, "number": number, "payout": payout, "showcurrency": showcurrency, "currency": currency, "operator": "Steam"})

def oplata_games_wowgold(request):
      step = "number"
      number, payout = "", ""

      nextstep = request.GET.get("nextstep")
      if nextstep == "balance":
            step = "balance"
      elif nextstep == "success":
            payout = request.GET.get("payout")
            step = "success"

      return render(request, "oplata_uslug/games/topup.html", context={"step":step, "number": number, "payout": payout, "operator": "WOW Gold"})

def oplata_games_robux(request):
      step = "number"
      number, payout = "", ""

      nextstep = request.GET.get("nextstep")
      if nextstep == "balance":
            step = "balance"
      elif nextstep == "success":
            payout = request.GET.get("payout")
            step = "success"

      return render(request, "oplata_uslug/games/topup.html", context={"step":step, "number": number, "payout": payout, "operator": "Robux"})
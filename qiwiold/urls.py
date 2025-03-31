"""
URL configuration for qiwiold project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from sitepages import views

urlpatterns = [
    path('', views.index),
    re_path(r'^about', views.about),

    # операторы
    re_path(r'^oplata_uslug/mts_dom', views.oplata_internet_mts),
    re_path(r'^oplata_uslug/beeline_dom', views.oplata_internet_beeline),
    re_path(r'^oplata_uslug/beeline_wifi', views.oplata_internet_beelinewifi),
    re_path(r'^oplata_uslug/beeline_bank', views.oplata_bank_beeline),
    re_path(r'^oplata_uslug/megafon_dom', views.oplata_internet_megafon),
    re_path(r'^oplata_uslug/mts', views.oplata_mobile_mts),
    re_path(r'^oplata_uslug/beeline', views.oplata_mobile_beelinerus),
    re_path(r'^oplata_uslug/tele2', views.oplata_mobile_tele2),
    re_path(r'^oplata_uslug/megafon', views.oplata_mobile_megafon),
    re_path(r'^oplata_uslug/rostelekom', views.oplata_internet_rostelekom),
    re_path(r'^oplata_uslug/domru', views.oplata_internet_domru),
    re_path(r'^oplata_uslug/ntv', views.oplata_tv_ntv),
    re_path(r'^oplata_uslug/mastercard', views.oplata_bank_mc),
    re_path(r'^oplata_uslug/visa', views.oplata_bank_visa),
    re_path(r'^oplata_uslug/rosselhoz', views.oplata_bank_rosselhoz),
    re_path(r'^oplata_uslug/mir', views.oplata_bank_mir),
    re_path(r'^oplata_uslug/zarubezh', views.oplata_bank_zarubezh),
    re_path(r'^oplata_uslug/steam', views.oplata_games_steam),
    re_path(r'^oplata_uslug/wowgold', views.oplata_games_wowgold),
    re_path(r'^oplata_uslug/robux', views.oplata_games_robux),

    re_path(r'^oplata_uslug/category/mobile', views.oplata_mobile),
    re_path(r'^oplata_uslug/category/internet', views.oplata_internet),
    re_path(r'^oplata_uslug/category/tv', views.oplata_tv),
    re_path(r'^oplata_uslug/category/bank/per', views.oplata_bank_per),
    re_path(r'^oplata_uslug/category/bank', views.oplata_bank),
    re_path(r'^oplata_uslug/category/games', views.oplata_games),

    # оплата услуг
    re_path(r'^oplata_uslug', views.oplata_main),
]

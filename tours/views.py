from random import sample

from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404

from data import tours, departures


def main_view(request):
    tours_temp = {key: tours[key] for key in sample(list(tours), 6)}
    context = {"tours": tours_temp, "departures": departures}
    return render(request, "tours/index.html", context=context)


def departure_view(request, departure):
    temp = {key: value for key, value in tours.items() if value["departure"] == departure}
    if not temp:
        raise Http404
    min_price = min(temp.values(), key=lambda key: key["price"])["price"]
    max_price = max(temp.values(), key=lambda key: key["price"])["price"]
    min_nights = min(temp.values(), key=lambda key: key["nights"])["nights"]
    max_nights = max(temp.values(), key=lambda key: key["nights"])["nights"]
    information = {"min_price": min_price, "max_price": max_price, "min_nights": min_nights, "max_nights": max_nights}
    return render(request, "tours/departure.html",
                  {'departures': departures, 'tours': temp, 'departure': departures[departure][2:],
                   "information": information})


def tour_view(request, pk):
    if pk not in tours:
        raise Http404
    context = {"tour": tours[pk], "departures": departures, "pk": pk,
               "departure": departures[tours[pk]['departure']][2:]}
    return render(request, "tours/tour.html", context=context)


def custom_handler_404(request, exception):
    return HttpResponseNotFound('<center><h1>Ничего не нашлось! Ошибка 404!</h1></center>')


def custom_handler_500(request):
    return HttpResponseNotFound('<center><h1>Вы сломали сервер! Ошибка 500!</h1></center>')

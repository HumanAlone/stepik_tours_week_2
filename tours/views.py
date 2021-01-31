from django.shortcuts import render
from django.http import HttpResponseNotFound


# Create your views here.
def main_view(request):
    return render(request, "tours/index.html")


def departure_view(request, departure):
    return render(request, "tours/departure.html")


def tour_view(request, id):
    return render(request, "tours/tour.html")


def custom_handler_404(request, exception):
    return HttpResponseNotFound('<center><h1>Ничего не нашлось! Ошибка 404!</h1></center>')


def custom_handler_500(request):
    return HttpResponseNotFound('<center><h1>Вы сломали сервер! Ошибка 500!</h1></center>')

from data import departures


def departure_processor(request):
    return {"departures": departures}

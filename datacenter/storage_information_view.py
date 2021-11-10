from datacenter.models import Visit
from django.shortcuts import render


def viewing_storage_information(request):
    """
    Функция отображения посетителей красной зоны
    """
    non_closed_visits = Visit.objects.filter(leaved_at=None)
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

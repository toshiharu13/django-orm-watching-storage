from datacenter.models import Visit
from django.shortcuts import render


def viewing_passcard_info(request, passcode):
    """
    Функция отображения информации пропуска сотрудника
    """
    list_of_visits = Visit.objects.filter(passcard__passcode=passcode)
    name_of_employee = list_of_visits[0].passcard.owner_name
    context = {
        'list_of_visits': list_of_visits,
        'name': name_of_employee,
    }
    return render(request, 'passcard_info.html', context)

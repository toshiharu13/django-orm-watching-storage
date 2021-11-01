from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    """
    Функция отображения информации пропуска сотрудника
    """
    passcard = Visit.objects.filter(passcard__passcode=passcode)
    name = passcard[0].passcard.owner_name
    context = {
        'passcard': passcard,
        'name': name,
    }
    return render(request, 'passcard_info.html', context)

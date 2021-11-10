from datacenter.models import Passcard
from django.shortcuts import render


def take_active_passcards(request):
    """
    Функция отображения сотрудников с актуальным пропуском
    """
    all_active_passcards = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': all_active_passcards,
    }
    return render(request, 'active_passcards.html', context)

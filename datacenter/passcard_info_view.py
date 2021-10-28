from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = Visit.objects.filter(passcard__passcode=passcode)
    name = passcard[0].passcard.owner_name

    this_passcard_visits = [
        {
            'entered_at': passcard,
            'duration': '25:03',
            'is_strange': False
        },
    ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits,
        'name':name
    }
    return render(request, 'passcard_info.html', context)

from django.db import models
from django.utils.timezone import localtime


def format_duration(duration):
    delta_sec = duration
    hours = delta_sec // 3600
    minutes = (delta_sec - (hours * 3600)) // 60
    seconds = delta_sec - (hours * 3600) - (minutes * 60)
    return f'{int(hours)}:{int(minutes)}:{int(seconds)}'


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self):
        time_in = self.entered_at
        now = localtime()
        delta = now - time_in
        return format_duration(delta.total_seconds())

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )

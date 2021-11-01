from django.db import models
from django.utils.timezone import localtime


def format_duration(duration):
    delta_sec = duration
    hours = delta_sec // 3600
    minutes = (delta_sec - (hours * 3600)) // 60
    seconds = delta_sec - (hours * 3600) - (minutes * 60)
    return f'{int(hours)}:{int(minutes)}:{int(seconds)}'


def get_duration(visit, time_out=None):
    if time_out:
        delta = time_out - visit
    else:
        delta = localtime() - visit
    return delta.total_seconds()


def long_or_not(delta_sec):
    if delta_sec > 3600:
        return True
    return False


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

    def get_duration_in(self):
        time_in = self.entered_at
        if self.leaved_at:
            time_out = self.leaved_at
            delta_sec = get_duration(time_in, time_out)
        else:
            delta_sec = get_duration(time_in)
        return format_duration(delta_sec)

    def is_visit_long_in(self):
        time_in = self.entered_at
        if self.leaved_at:
            time_out = self.leaved_at
            delta_sec = get_duration(time_in, time_out)
        else:
            delta_sec = get_duration(time_in)
        return long_or_not(delta_sec)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved='leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )

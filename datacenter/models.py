from django.db import models
from django.utils.timezone import localtime


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
        time_out = self.leaved_at
        if time_out:
            delta = time_out - time_in
        else:
            delta = localtime() - time_in
        return int(delta.total_seconds())

    def is_visit_long_in(self):
        delta_sec = self.get_duration_in()
        return delta_sec > 3600

    def format_duration(self):
        delta_sec = self.get_duration_in()
        hours = delta_sec // 3600
        minutes = (delta_sec - (hours * 3600)) // 60
        seconds = delta_sec - (hours * 3600) - (minutes * 60)
        return f'{int(hours)}:{int(minutes)}:{int(seconds)}'

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved='leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )

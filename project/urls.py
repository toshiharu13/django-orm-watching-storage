from datacenter.active_passcards_view import take_active_passcards
from datacenter.passcard_info_view import viewing_passcard_info
from datacenter.storage_information_view import viewing_storage_information
from django.conf.urls import url


urlpatterns = [
    url(r'^$', take_active_passcards, name='active_passcards'),
    url(r'^storage_information$', viewing_storage_information, name='storage_information'),
    url(r'^passcard_info/(?P<passcode>[\w\-]+)/$', viewing_passcard_info, name='passcard_info'),
]

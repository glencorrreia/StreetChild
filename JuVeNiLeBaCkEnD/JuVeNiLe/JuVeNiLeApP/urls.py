
from django.conf.urls import url
from .views import *


urlpatterns =[
    url(r'^login/$', loginView),
    url(r'^logout/$', logoutView),
    url(r'^register/$', register_user),
    url(r'^child/register/$', register_child),
    url(r'^make/prediction/$', getLogisticPrediction),
    url(r'^verify/otp/$', verifyOtp),
    url(r'^resend/otp/$', resendOtp),
]



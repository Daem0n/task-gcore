from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^register/$', views.UserRegister.as_view()),
    url(r'^sign_in/$', views.UserSignIn.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
    url(r'^locations/$', views.LocationList.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)$', views.LocationDetail.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)/visit$', views.LocationVisit.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)/ratio$', views.LocationRatio.as_view()),
    url(r'^visits/$', views.VisitList.as_view()),
    url(r'^visits/(?P<pk>[0-9]+)$', views.VisitDetail.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/ratio$', views.UserRatio.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

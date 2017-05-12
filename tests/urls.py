from django.conf.urls import include, url
from django.contrib import admin

from tests.views import TestViewHeader, TestViewQueryParam


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', TestViewHeader.as_view(), name="test-view"),
    url(r'^test_param/$', TestViewQueryParam.as_view(), name="test-view-param"),
]

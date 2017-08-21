# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, RetailersList
from .views import PromotionList
from .views import task_list
from .views import Test

from .views import getMan
urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    url(r'^promotionlist/$', PromotionList.as_view(), name="create"),
    url(r'^checkPost/',task_list),
    url(r'^filter/',Test),
    url(r'^book/',getMan),
    url(r'^retailerslist',RetailersList.as_view()),
    
}

urlpatterns = format_suffix_patterns(urlpatterns)

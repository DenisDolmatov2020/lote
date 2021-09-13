from django.urls import path
from number.views import NumberList, NumberUpdateView


urlpatterns = [
    path('', NumberList.as_view(), name='list-numbers'),
    path('update/', NumberUpdateView.as_view(), name='number-update')
]

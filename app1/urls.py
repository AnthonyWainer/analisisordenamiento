from django.conf.urls import url
from .views import index
from .burbuja import burbu
from .quickSort import quick
from .heapsort import heap

urlpatterns = [
    url(r'^$', index.as_view()),
    url(r'^burbu$', burbu),
    url(r'^quick$', quick),
    url(r'^heap$', heap),
]

from django.urls import path
from .views import *
urlpatterns = [
    path("memory",  MemoryInfoView.as_view(),name="memory"),
    path("cpu", CpuInfoView.as_view(),name="cpu"),
    path("hard",HardInfoView.as_view(),name='hard'),
]
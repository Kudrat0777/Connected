from django.urls import path
from .views import HomeView, ServicesView, ContactView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("services/", ServicesView.as_view(), name="services"),
    path("contact/", ContactView.as_view(), name="contact"),
]
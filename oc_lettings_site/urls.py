from django.contrib import admin
from . import views
from lettings.views import letting, lettings_index
from profiles.views import profile, profiles_index
from django.urls import path


def trigger_error(request):
    division_by_zero = 1 / 0
    return division_by_zero


urlpatterns = [
    path("", views.index, name="index"),
    path('sentry-debug/', trigger_error),
    path("lettings/", lettings_index, name="lettings_index"),
    path("lettings/<int:letting_id>/", letting, name="letting"),
    path("profiles/", profiles_index, name="profiles_index"),
    path("profiles/<str:username>/", profile, name="profile"),
    path("admin/", admin.site.urls),
]

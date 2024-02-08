from django.urls import path
from .views import submit_user_profile_form

app_name = 'user_profiles'

urlpatterns = [
    path('edit_profile/', submit_user_profile_form, name='edit_profile')
]
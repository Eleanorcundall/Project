from django.urls import path
from .views import submit_user_profile_form, user_profile_view, other_user_profile_view

app_name = 'user_profile'

urlpatterns = [
    path('edit_profile/', submit_user_profile_form, name='edit_profile'),
    path('user_profile/', user_profile_view, name='user_profile'),
    path('user/<int:user_id>/', other_user_profile_view, name='other_user_profile')
]
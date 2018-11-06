from django.urls import path
from .views import get_or_post_data_in_stack,retrieve_stack,insert_at_stack

urlpatterns = [
    path('stack', get_or_post_data_in_stack),
    path('stack/insert_at',insert_at_stack),
    path('stack/<int:pk>', retrieve_stack),

]

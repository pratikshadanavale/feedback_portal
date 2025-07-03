from django.urls import path
from . import views
from .views import EmployeeListView, FeedbackListView, FeedbackCreateView
urlpatterns = [
    path('', views.home, name = 'home'),
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('feedbacks/', FeedbackListView.as_view(), name = 'feedback_list'),
    path('submit/', FeedbackCreateView.as_view(), name = 'submit_feedback'),
]




# from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Smart Feedback Portal")


from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Employee,Feedback
from django.utils.decorators import method_decorator
from .utils import log_access
from .services import FeedbackService


@method_decorator(log_access , name='dispatch')
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'

@method_decorator(log_access , name='dispatch')
class FeedbackListView(ListView):
    model = Feedback
    template_name = 'feedback_list.html'
    context_object_name = 'feedbacks'

@method_decorator(log_access , name='dispatch')
class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['employee','comment','subject']
    template_name = 'feedback/submit_feedback.html'
    success_url = reverse_lazy('feedback_list')

    def form_valid(self, form):
        service = FeedbackService()
        service.create_feedback(form.cleaned_data)  # ✅ OOP Logic Delegation
        return super().form_valid(form)

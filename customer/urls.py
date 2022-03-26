from django.urls import path
from . import views

urlpatterns = [
    path('list-all/', views.CustomerListView.as_view()),
    path('signup/', views.CustomerSignupView.as_view()),
    path('order-history/', views.CustomerOrderSummaryView.as_view()),
    path('feedback/list-all/', views.CustomerFeedbackView.as_view()),
    path('profile/update/', views.CustomerProfileUpdateView.as_view()),
]

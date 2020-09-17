from django.urls import path
from api import views

urlpatterns = [
    path('benefactor-list/', views.benefactorShow, name="benefactor-list"),
    path('benefactor-create/', views.benefactorCreate, name="benefactor-create"),
    path('benefactor-detail/<str:pk>/', views.benefactorRead, name="benefactor-read"),
    path('benefactor-update/<str:pk>/', views.benefactorUpdate, name="benefactor-update"),
    path('benefactor-delete/<str:pk>/', views.benefactorDelete, name="benefactor-delete"),

    path('medic-report-list/', views.medicReportShow, name="medicReport-list"),
    path('medic-report-create/', views.medicReportCreate, name="medicReport-create"),
    path('medic-report-detail/<str:pk>/', views.medicReportRead, name="medicReport-read"),
    path('medic-report-update/<str:pk>/', views.medicReportUpdate, name="medicReport-update"),
    path('medic-report-delete/<str:pk>/', views.medicReportDelete, name="medicReport-delete"),

    path('beneficiary-list/', views.beneficiaryShow, name="beneficiary-list"),
    path('beneficiary-create/', views.beneficiaryCreate, name="beneficiary-create"),
    path('beneficiary-detail/<str:pk>/', views.beneficiaryRead, name="beneficiary-read"),
    path('beneficiary-update/<str:pk>/', views.beneficiaryUpdate, name="beneficiary-update"),
    path('beneficiary-delete/<str:pk>/', views.beneficiaryDelete, name="beneficiary-delete"),
]
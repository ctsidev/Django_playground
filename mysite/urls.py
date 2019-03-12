from django.urls import path
from django.views.generic import RedirectView

from mysite.core import views


urlpatterns = [
    path('', RedirectView.as_view(url='/project/1/'), name='index'),
    # path('project/1/', views.ProjectFormView.as_view(template_name='project.html'), name='project'),
    path('project/2/', views.ProjectFormView.as_view(template_name='project.html'), name='project'),
    path('project/3/', views.ProjectFormView.as_view(template_name='project.html'), name='project'),
    path('project/4/', views.ProjectFormView.as_view(), name='project'),
    path('project/1/', views.ProjectFormView.as_view(), name='project'),
    path('demographic/1/', views.DemographicFormView.as_view(template_name='demographic.html'), name='demographic'),

    path('encounter/1/', views.EncounterFormView.as_view(template_name='encounter.html'), name='encounter'),
    path('success/', views.SuccessView.as_view(), name='success'),
]

# from django import forms
from django.contrib.auth.models import User
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
	)
from .forms import ProjectFieldForm, DemographicFieldForm, EncounterFieldForm
# AddressForm, CrispyAddressForm, CustomFieldForm, DemographicsElementsForm, EncountersElementsForm
from .models import Project

# class AddressFormView(FormView):
# 	form_class = AddressForm
# 	success_url = reverse_lazy('success')


# class CrispyAddressFormView(FormView):
# 	form_class = CrispyAddressForm
# 	success_url = reverse_lazy('success')
# 	template_name = 'crispy_form.html'


class ProjectFormView(FormView):
	model = Project 
	form_class = ProjectFieldForm
	success_url = reverse_lazy('success')
	template_name = 'crispy_form.html'

	# def form_valid(self, form):
	# 	# form.instance.investigator = self.request.user
	# 	return super().form_valid(form)


class DemographicFormView(FormView):
	form_class = DemographicFieldForm
	success_url = reverse_lazy('success')
	template_name = 'crispy_form.html'

class EncounterFormView(FormView):
	form_class = EncounterFieldForm
	success_url = reverse_lazy('success')
	template_name = 'crispy_form.html'

class SuccessView(TemplateView):
	template_name = 'success.html'

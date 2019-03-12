from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field
from datetime import date

from flatpickr import DatePickerInput

from .models import Project
REQUEST_TYPE_CHOICES = (
        ('', 'Choose...'),
        ('Specialized Counts', 'Specialized Counts'),
        ('Limited Data Set', 'Limited Data Set'),
        ('De-Identified Dataset', 'De-Identified Dataset'),
        ('Identified Dataset', 'Identified Dataset'),
    )

class ProjectForm(forms.Form):
    title = forms.CharField()
    irb = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': '##-######'}))
    irb_approved = forms.BooleanField(required=False)
    description = forms.CharField(max_length=200) 
    investigator = forms.CharField(max_length=100)
    investigator_phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '###-###-####'}))
    investigator_email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    requestor = forms.CharField(max_length=100)
    requestor_phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '###-###-####'}))
    requestor_email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    deadline_date = forms.DateField(widget=DatePickerInput())
    # email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    # password = forms.CharField(widget=forms.PasswordInput())
    # address_1 = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}))
    # address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'}))
    # city = forms.CharField()
    request_type = forms.ChoiceField(choices=REQUEST_TYPE_CHOICES)
    chart_review = forms.BooleanField(required=False)
    recruitment = forms.BooleanField(required=False)

    class Meta:
        model = Project
        fields = [  'title','irb','description','investigator','investigator_phone','investigator_email',
    'requestor','requestor_phone','requestor_email','chart_review',
    'request_type', 
    'date_deadline',
    ]
class EncounterForm(forms.Form):
    study_id = forms.BooleanField(initial=True, help_text='Study ID is a study-specific one-way hash of the unique research identifier assigned to every UCLA patient. The Study ID is used implicitly in each table below to represent the patient identity.')    
    encounter_id = forms.BooleanField(initial=True, help_text='Study ID is a study-specific one-way hash of the unique research identifier assigned to every UCLA patient. The Study ID is used implicitly in each table below to represent the patient identity.')    
    epic_encounter_type = forms.BooleanField(initial=True, help_text='The encounter type represented in Care Connect. E.g. "Office Visit"')        
    encounter_date = forms.BooleanField(initial = False, help_text = 'Date of the patients first encounter based on the investigators criteria')
    encounter_age = forms.BooleanField(initial=False)
    
    admit_date_time = forms.BooleanField(initial=False, help_text='Start day for multi-day encounters, without time of day')            
    discharge_date_time = forms.BooleanField(initial=False, help_text='End day for multi-day encounters, without time of day') 

    hospital_discharge_disposition = forms.BooleanField(initial=False, help_text='The disposition of the patient when discharged from the hospital, only applies to multi-day hospital encounters.')    
    ed_disposition = forms.BooleanField(initial=False, help_text='The disposition of the patient when discharged from the ED, only applies to patients who were in ED')   
    
    pcornet_visit_type = forms.BooleanField(initial=True, help_text = 'Standardized visit types defined by PCORnet, including "Ambulatory Visit", "Inpatient", etc.')    
    visit_provider_id = forms.BooleanField(initial=False)    
    epic_department_name = forms.BooleanField(initial=False)    
    department_specialty = forms.BooleanField(initial=False, help_text = 'The designated medical specialty of the department where the encounter took place')    
    length_of_stay = forms.BooleanField(initial = False, help_text = 'Calculated days from admit to discharge')
    location = forms.BooleanField(initial=False)    
    
    epic_encounter_type_criteria = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'The encounter type represented in Care Connect. E.g. "Office Visit'}))

    encounter_date_criteria = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': '2013 to present time'}))
    pcornet_visit_type_criteria = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Standardized visit types defined by PCORnet. E.g. "Ambulatory Visit"'}))
    epic_department_name_criteria = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'ICU'}))
    department_specialty_criteria = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Urology'}))
    location_criteria = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Ronald Reagan'}))

class DemographicForm(forms.Form):
    study_id = forms.BooleanField(initial=True, help_text='Study ID is a study-specific one-way hash of the unique research identifier assigned to every UCLA patient. The Study ID is used implicitly in each table below to represent the patient identity.')    
    age = forms.BooleanField(initial=False, help_text='Age at the time of the data extraction. (draft)')        
    sex = forms.BooleanField(initial=False)
    race = forms.BooleanField(initial=False, help_text='Race calculated conforming to PSCANNER data model. (draft)')            
    ethnicity = forms.BooleanField(initial=False, help_text='Ethnicity calculated conforming to PSCANNER data model. (draft)') 
    vital_status = forms.BooleanField(initial=False, help_text='Vital status is not known deceased or deceased status in EHR. Note only in-hospital death is recorded, for the most part.')
    neighborhood_adi_category = forms.BooleanField(initial=False, help_text='ADI calculated by the University of Wisconsin. (draft)')   
    current_pcp_id = forms.BooleanField(initial=False)    
    last_visit_encounter_year = forms.BooleanField(initial=False)    


class ProjectFieldForm(ProjectForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0'),
                Column('irb', css_class='form-group col-md-3 mb-0'),
                Column(CustomCheckbox('irb_approved'), css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),

            'description',

            'investigator',
            Row(
                Column('investigator_phone', css_class='form-group col-md-6 mb-0'),
                Column('investigator_email', css_class='form-group col-md-4 mb-0'),
                # Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            'requestor',
            Row(
                Column('requestor_phone', css_class='form-group col-md-6 mb-0'),
                Column('requestor_email', css_class='form-group col-md-4 mb-0'),
                # Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('request_type', css_class='form-group col-md-4 mb-0'),
                Column(CustomCheckbox('chart_review'), css_class='form-group col-md-2 mb-0'),
                Column(CustomCheckbox('recruitment'), css_class='form-group col-md-4 mb-0'),
                Column('deadline_date', css_class='form-group col-md-2 mb-0'),
                # Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save')
        )
class DemographicFieldForm(DemographicForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                
                Column(CustomCheckbox('study_id'), css_class='form-group col-md-1 mb-0')
                # Column('study_id_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                
                Column(CustomCheckbox('age'), css_class='form-group col-md-1 mb-0')
                # Column('age_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                
                Column(CustomCheckbox('sex'), css_class='form-group col-md-1 mb-0')
                # Column('sex_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                Column(CustomCheckbox('race'), css_class='form-group col-md-1 mb-0')
                # Column('race_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            
            Row(
                
                Column(CustomCheckbox('ethnicity'), css_class='form-group col-md-1 mb-0')
                # Column('ethnicity_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                
                Column(CustomCheckbox('vital_status'), css_class='form-group col-md-1 mb-0')
                # Column('vital_status_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                
                Column(CustomCheckbox('neighborhood_adi_category'), css_class='form-group col-md-1 mb-0')
                # Column('neighborhood_adi_category_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                
                Column(CustomCheckbox('current_pcp_id'), css_class='form-group col-md-1 mb-0')
                # Column('current_pcp_id_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                
                Column(CustomCheckbox('last_visit_encounter_year'), css_class='form-group col-md-1 mb-0')
                # Column('last_visit_encounter_year_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Submit('submit', 'Save')
        )

class EncounterFieldForm(EncounterForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                
                Column(CustomCheckbox('study_id'), css_class='form-group col-md-1 mb-0')
                # Column('study_id_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                
                Column(CustomCheckbox('encounter_id'), css_class='form-group col-md-1 mb-0')
                # Column('age_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                
                Column(CustomCheckbox('epic_encounter_type'), css_class='form-group col-md-1 mb-0'),
                Column('epic_encounter_type_criteria', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                Column(CustomCheckbox('encounter_date'), css_class='form-group col-md-1 mb-0'),
                Column('encounter_date_criteria', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
             Row(
                Column(CustomCheckbox('encounter_age'), css_class='form-group col-md-1 mb-0')
                # Column('race_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            
            Row(
                
                Column(CustomCheckbox('admit_date_time'), css_class='form-group col-md-1 mb-0')
                # Column('ethnicity_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                
                Column(CustomCheckbox('discharge_date_time'), css_class='form-group col-md-1 mb-0')
                # Column('vital_status_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                
                Column(CustomCheckbox('ed_disposition'), css_class='form-group col-md-1 mb-0')
                # Column('neighborhood_adi_category_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                
                Column(CustomCheckbox('pcornet_visit_type'), css_class='form-group col-md-8 mb-0'),
                Column('pcornet_visit_type_criteria', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                
                Column(CustomCheckbox('visit_provider_id'), css_class='form-group col-md-8 mb-0')
                # Column('last_visit_encounter_year_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                
                Column(CustomCheckbox('epic_department_name'), css_class='form-group col-md-8 mb-0'),
                Column('epic_department_name_criteria', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                
                Column(CustomCheckbox('department_specialty'), css_class='form-group col-md-8 mb-0'),
                Column('department_specialty_criteria', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Row(
                
                Column(CustomCheckbox('location'), css_class='form-group col-md-8 mb-0')
                # Column('last_visit_encounter_year_description', css_class='form-group col-md-4 mb-0')
                ,css_class='form-row'),
            Submit('submit', 'Save')
        )
class CustomCheckbox(Field):
    template = 'custom_checkbox.html'

from django.forms import ModelForm
from .models import Company, Job, Application, Interview

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'

class InterviewForm(ModelForm):
    class Meta:
        model = Interview
        fields = '__all__'

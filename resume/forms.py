from django import forms
from django.forms import inlineformset_factory
from .models import Resume, Education, Experience, Skill
from .models import Template

# In forms.py
class ResumeForm(forms.ModelForm):
    template = forms.ModelChoiceField(
        queryset=Template.objects.all(),
        required=False,
        label='Select a template'
    )
    
    class Meta:
        model = Resume
        fields = ['name', 'email', 'phone', 'summary', 'template']
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 4, 'class': 'w-full p-2 border rounded'}),
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
        }

EducationFormSet = inlineformset_factory(
    Resume, Education,
    fields=('degree', 'institute', 'year'),
    extra=1, can_delete=True
)

ExperienceFormSet = inlineformset_factory(
    Resume, Experience,
    fields=('job_title', 'company', 'duration', 'description'),
    extra=1, can_delete=True
)

SkillFormSet = inlineformset_factory(
    Resume, Skill,
    fields=('name',),
    extra=1, can_delete=True
)

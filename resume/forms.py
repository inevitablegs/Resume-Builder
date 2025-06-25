from django import forms
from django.forms import inlineformset_factory
from .models import Resume, Education, Experience, Skill

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'email', 'phone', 'summary']
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 4})
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

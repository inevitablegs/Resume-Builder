from django import forms
from django.forms import inlineformset_factory
from .models import Resume, Education, Experience, Skill, Template


class ResumeForm(forms.ModelForm):
    template = forms.ModelChoiceField(
        queryset=Template.objects.all(),
        required=False,
        label='Select a template',
        widget=forms.Select(attrs={'class': 'w-full p-2 border rounded'})
    )

    class Meta:
        model = Resume
        fields = ['name', 'email', 'phone', 'summary', 'template']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-2 border rounded'}),
            'phone': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'summary': forms.Textarea(attrs={'rows': 4, 'class': 'w-full p-2 border rounded'}),
        }


EducationFormSet = inlineformset_factory(
    Resume,
    Education,
    fields=('degree', 'institute', 'year'),
    extra=1,
    can_delete=True,
    widgets={
        'degree': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
        'institute': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
        'year': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
    }
)

ExperienceFormSet = inlineformset_factory(
    Resume,
    Experience,
    fields=('job_title', 'company', 'duration', 'description'),
    extra=1,
    can_delete=True,
    widgets={
        'job_title': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
        'company': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
        'duration': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
        'description': forms.Textarea(attrs={'class': 'w-full p-2 border rounded'}),
    }
)

SkillFormSet = inlineformset_factory(
    Resume,
    Skill,
    fields=('name',),
    extra=1,
    can_delete=True,
    widgets={
        'name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
    }
)

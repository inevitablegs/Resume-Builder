from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeForm, EducationFormSet, ExperienceFormSet, SkillFormSet
from .models import Resume
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Template
import os   
from django.conf import settings

def home(request):
    return render(request, 'resume/home.html')

def resume_form(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save()
            edu_formset = EducationFormSet(request.POST, instance=resume)
            exp_formset = ExperienceFormSet(request.POST, instance=resume)
            skill_formset = SkillFormSet(request.POST, instance=resume)
            if edu_formset.is_valid() and exp_formset.is_valid() and skill_formset.is_valid():
                edu_formset.save()
                exp_formset.save()
                skill_formset.save()
                return redirect('preview_resume', resume_id=resume.id)
    else:
        form = ResumeForm()
        edu_formset = EducationFormSet()
        exp_formset = ExperienceFormSet()
        skill_formset = SkillFormSet()

    return render(request, 'resume/form.html', {
        'form': form,
        'edu_formset': edu_formset,
        'exp_formset': exp_formset,
        'skill_formset': skill_formset
    })
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from .models import Resume, Template

def preview_resume(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    
    # Determine which template to use
    if hasattr(resume, 'template') and resume.template:
        # Use the selected template if available
        template_file = f"resume/{resume.template.template_file}"
    else:
        # Fall back to default preview template
        template_file = 'resume/preview.html'
    
    return render(request, template_file, {
        'resume': resume,
        'is_preview': True  # Add this flag for template customization
    })

from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

def download_pdf(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    
    # Debug template selection
    template_file = 'resume/template_pdf.html'  # Force specific template for testing
    print(f"Rendering template: {template_file}")
    
    context = {
        'resume': resume,
        'request': request  # Make sure request is available in template
    }
    
    try:
        html_string = render_to_string(template_file, context)
        print("HTML Output:", html_string[:500])  # Print first 500 chars
        
        font_config = FontConfiguration()
        pdf_bytes = HTML(
            string=html_string,
            base_url=request.build_absolute_uri('/'),
            encoding='utf-8'
        ).write_pdf(
            stylesheets=[
                CSS(string='''
                @page { size: A4; margin: 1cm; }
                body { font-family: "Times New Roman", serif; }
                ''',
                font_config=font_config)
            ]
        )
        
        response = HttpResponse(pdf_bytes, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{resume.name}_resume.pdf"'
        return response
        
    except Exception as e:
        print(f"PDF Generation Error: {str(e)}")
        return HttpResponse(f"Error generating PDF: {str(e)}", status=500)

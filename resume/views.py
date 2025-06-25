from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResumeForm, EducationFormSet, ExperienceFormSet, SkillFormSet
from .models import Resume
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

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

def preview_resume(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    return render(request, 'resume/preview.html', {'resume': resume})

def download_pdf(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    template = get_template('resume/preview.html')
    html = template.render({'resume': resume})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response

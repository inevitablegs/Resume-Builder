from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    summary = models.TextField()

    def __str__(self):
        return self.name

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    year = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.degree} at {self.institute}"

class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# In models.py
class Template(models.Model):
    name = models.CharField(max_length=100)
    preview_image = models.ImageField(upload_to='template_previews/')
    template_file = models.CharField(max_length=100)  # Path to template HTML file
    is_premium = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    
# In models.py
class ResumeSection(models.Model):
    SECTION_CHOICES = [
        ('summary', 'Summary'),
        ('experience', 'Experience'),
        ('education', 'Education'),
        ('skills', 'Skills'),
        ('projects', 'Projects'),
        ('certifications', 'Certifications'),
    ]
    
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    section_type = models.CharField(max_length=20, choices=SECTION_CHOICES)
    order = models.PositiveIntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
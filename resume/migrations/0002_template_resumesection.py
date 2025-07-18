# Generated by Django 5.2.3 on 2025-07-11 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('preview_image', models.ImageField(upload_to='template_previews/')),
                ('template_file', models.CharField(max_length=100)),
                ('is_premium', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ResumeSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_type', models.CharField(choices=[('summary', 'Summary'), ('experience', 'Experience'), ('education', 'Education'), ('skills', 'Skills'), ('projects', 'Projects'), ('certifications', 'Certifications')], max_length=20)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_visible', models.BooleanField(default=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.resume')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]

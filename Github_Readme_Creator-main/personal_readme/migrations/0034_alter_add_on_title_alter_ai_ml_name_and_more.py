# Generated by Django 4.1.1 on 2022-10-27 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_readme', '0033_alter_personal_readme_add_ons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_on',
            name='title',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='ai_ml',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='automation',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='backend_language',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='bass',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='blockchain',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='data_visualization',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='database',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='devops',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='framework',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='frontend_language',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='game_engine',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='mobile_app_devlopment',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='others',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='personal_readme',
            name='about_me',
            field=models.CharField(blank=True, max_length=9000),
        ),
        migrations.AlterField(
            model_name='personal_readme',
            name='github',
            field=models.CharField(blank=True, max_length=900),
        ),
        migrations.AlterField(
            model_name='personal_readme',
            name='name',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='personal_readme',
            name='project2',
            field=models.CharField(blank=True, max_length=9000),
        ),
        migrations.AlterField(
            model_name='personal_readme',
            name='project3',
            field=models.CharField(blank=True, max_length=9000),
        ),
        migrations.AlterField(
            model_name='personal_readme',
            name='project4',
            field=models.CharField(blank=True, max_length=9000),
        ),
        migrations.AlterField(
            model_name='personal_readme',
            name='project5',
            field=models.CharField(blank=True, max_length=9000),
        ),
        migrations.AlterField(
            model_name='personal_readme',
            name='work_status',
            field=models.CharField(blank=True, max_length=90),
        ),
        migrations.AlterField(
            model_name='programming_language',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='software',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='static_site_gen',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='systemchoice',
            name='name',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='testing',
            name='name',
            field=models.CharField(max_length=900),
        ),
    ]

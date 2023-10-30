# Generated by Django 4.1.1 on 2022-09-17 13:06

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('personal_readme', '0028_alter_personal_readme_add_ons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_readme',
            name='add_ons',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Display', 'Display'), ('github', 'github'), ('skills', 'skills'), ('stats', 'stats'), ('streak', 'streak')], max_length=500, null=True),
        ),
    ]

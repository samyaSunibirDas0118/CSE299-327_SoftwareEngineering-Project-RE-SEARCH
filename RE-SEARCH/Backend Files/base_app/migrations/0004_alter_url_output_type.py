# Generated by Django 3.2.9 on 2021-12-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0003_alter_url_output_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='output_type',
            field=models.CharField(choices=[('html', 'Textual Data'), ('.pdf', 'PDF'), ('.txt', 'TXT'), ('.docx', 'DOC')], max_length=20),
        ),
    ]
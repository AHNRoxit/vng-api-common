# Generated by Django 2.0.13 on 2019-05-22 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audittrails', '0006_audittrail_toelichting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audittrail',
            name='toelichting',
            field=models.TextField(blank=True, help_text='Toelichting waarom de handeling is uitgevoerd', verbose_name='toelichting'),
        ),
    ]

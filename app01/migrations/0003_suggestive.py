# Generated by Django 2.1.1 on 2018-11-28 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_studentlogin_teacherlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestive_content', models.CharField(max_length=200)),
                ('submit_data', models.CharField(max_length=64)),
                ('submit_person', models.ForeignKey(on_delete='id', to='app01.Student')),
            ],
        ),
    ]

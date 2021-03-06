# Generated by Django 2.1.7 on 2019-03-21 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('grade', models.IntegerField()),
                ('aam', models.IntegerField()),
                ('wam', models.IntegerField()),
                ('Credit_attemp', models.IntegerField()),
                ('Credit_passed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('faculty', models.CharField(max_length=200)),
                ('email_ini', models.EmailField(max_length=254)),
                ('email_per', models.EmailField(max_length=254)),
                ('mobile_num', models.IntegerField()),
                ('course', models.CharField(max_length=200)),
                ('course_code', models.CharField(max_length=200)),
                ('course_type', models.CharField(max_length=200)),
                ('course_type_name', models.CharField(max_length=200)),
                ('citizen_type', models.CharField(max_length=200)),
                ('citizen_country', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('last_enrol_date', models.DateField()),
                ('address', models.DateField()),
                ('attend_mode', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('semester', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Student'),
        ),
        migrations.AddField(
            model_name='grade',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Unit'),
        ),
    ]

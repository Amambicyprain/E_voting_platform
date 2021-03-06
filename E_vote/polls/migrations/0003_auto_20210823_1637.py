# Generated by Django 3.2.3 on 2021-08-23 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_candidate_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='Choice_text',
            new_name='candidate_name',
        ),
        migrations.AddField(
            model_name='choice',
            name='candidate_date_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='candidate_email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='candidate_role',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='candidate_status',
            field=models.CharField(choices=[('Married', '1'), ('Single', '2'), ('Divorced', '3'), ('Widowed', '4'), ('Complicated', '5')], default=2, max_length=20),
        ),
        migrations.AddField(
            model_name='choice',
            name='candidate_tel',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='choice',
            name='carrier_history',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='choice',
            name='candidate_image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]

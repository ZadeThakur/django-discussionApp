# Generated by Django 2.2.5 on 2019-10-29 20:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0002_postsmodel_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='replyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=30)),
                ('reply', models.CharField(max_length=1000)),
                ('replyTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts_app.postsModel')),
            ],
        ),
    ]

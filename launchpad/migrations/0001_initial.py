# Generated by Django 4.0 on 2022-03-04 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostedCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('address', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostedMetadata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_id', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('animation_url', models.FileField(blank=True, default=None, upload_to='hyperdrive-hosted-collections/animation')),
                ('image', models.ImageField(blank=True, null=True, upload_to='hyperdrive-hosted-collections/image')),
                ('attributes_str', models.TextField(blank=True, default='{}')),
                ('external_url', models.URLField(blank=True, null=True)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='launchpad.hostedcollection')),
            ],
            options={
                'verbose_name_plural': 'Hosted metadata',
                'unique_together': {('collection', 'token_id')},
            },
        ),
    ]

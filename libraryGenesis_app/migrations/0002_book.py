from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryGenesis_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publish_date', models.DateField()),
                ('price', models.IntegerField()),
                ('days_avaliable', models.IntegerField()),
                ('about', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('users', models.ManyToManyField(related_name='books', to='libraryGenesis_app.User')),

                ('title', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=45)),
                ('author', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),

            ],
        ),
    ]

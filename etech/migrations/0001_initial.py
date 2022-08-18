# Generated by Django 4.1 on 2022-08-18 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Şəkil ölçüsü: 545X470', upload_to='image/about/%Y/%m/%d/', verbose_name='Şəkil')),
                ('title', models.CharField(max_length=60, verbose_name='Haqqımda başlıq')),
                ('text', models.TextField(verbose_name='Haqqımda mətn')),
                ('about_quote_title_1', models.TextField(verbose_name='Haqqımda sitat 1 başlıq')),
                ('about_quote_1', models.TextField(verbose_name='Haqqımda sitat 1')),
                ('about_quote_title_2', models.TextField(verbose_name='Haqqımda sitat 2 başlıq')),
                ('about_quote_2', models.TextField(verbose_name='Haqqımda sitat 2')),
                ('quote_title_1', models.TextField(verbose_name='Sitat başlıq-1')),
                ('quote_1', models.TextField(verbose_name='Sitat-1')),
                ('quote_title_2', models.TextField(verbose_name='Sitat başlıq-2')),
                ('quote_2', models.TextField(verbose_name='Sitat-2')),
                ('quote_title_3', models.TextField(verbose_name='Sitat başlıq-3')),
                ('quote_3', models.TextField(verbose_name='Sitat-3')),
                ('quote_title_4', models.TextField(verbose_name='Sitat başlıq-4')),
                ('quote_4', models.TextField(verbose_name='Sitat-4')),
                ('quote_title_5', models.TextField(verbose_name='Sitat başlıq-5')),
                ('quote_5', models.TextField(verbose_name='Sitat-5')),
                ('quote_title_6', models.TextField(verbose_name='Sitat başlıq-6')),
                ('quote_6', models.TextField(verbose_name='Sitat-6')),
                ('happy_clients', models.PositiveBigIntegerField(default=0, verbose_name='Məmnun müştəri sayı')),
                ('projects', models.PositiveBigIntegerField(default=0, verbose_name='Layihə sayı')),
                ('hours_of_support', models.PositiveBigIntegerField(default=0, verbose_name='Dəstək saatları')),
                ('hard_workers', models.PositiveBigIntegerField(default=0, verbose_name='Aktiv işləyənlər')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Kateqoriya adı')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slaq')),
            ],
            options={
                'verbose_name': 'Kateqoriya',
                'verbose_name_plural': 'Kateqoriya',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='image/logo/%Y/%m/%d/')),
                ('address', models.CharField(max_length=250, verbose_name='Ünvan')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_1', models.CharField(blank=True, max_length=60, null=True, verbose_name='Telefon 1')),
                ('phone_2', models.CharField(blank=True, max_length=60, null=True, verbose_name='Telefon 2')),
                ('soc_link_1', models.URLField(blank=True, null=True, verbose_name='1.Sosial şəbəkə url')),
                ('soc_icon_1', models.CharField(blank=True, max_length=20, verbose_name='1.Sosial şəbəkə ikon')),
                ('soc_link_2', models.URLField(blank=True, null=True, verbose_name='2.Sosial şəbəkə url')),
                ('soc_icon_2', models.CharField(blank=True, max_length=20, verbose_name='2.Sosial şəbəkə ikon')),
                ('soc_link_3', models.URLField(blank=True, null=True, verbose_name='3.Sosial şəbəkə url')),
                ('soc_icon_3', models.CharField(blank=True, max_length=20, verbose_name='3.Sosial şəbəkə ikon')),
                ('soc_link_4', models.URLField(blank=True, null=True, verbose_name='4.Sosial şəbəkə url')),
                ('soc_icon_4', models.CharField(blank=True, max_length=20, verbose_name='4.Sosial şəbəkə ikon')),
            ],
            options={
                'verbose_name': 'Əlaqə',
                'verbose_name_plural': 'Əlaqə',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(help_text='Ikinları bu saytdan götürün: icons.getbootstrap.com - MƏSƏLƏN (bi-5-circle)', max_length=100, verbose_name='Xidmət ikon')),
                ('name', models.CharField(max_length=100, verbose_name='Xidmət adı')),
                ('text', models.TextField(verbose_name='Xidmət açıqlama')),
                ('delay', models.PositiveBigIntegerField(blank=True, default=0, help_text='Hər xidmətə 100 vahid artırmaq lazımdır.', verbose_name='Xidmət üçün animasiya.')),
            ],
            options={
                'verbose_name': 'Xidmət',
                'verbose_name_plural': 'Xidmət',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Slayder başlıq')),
                ('text', models.TextField(verbose_name='Slayder mətn')),
                ('image', models.ImageField(help_text='Slayder üçün şəkil ölçüsü: 1920X1080', upload_to='image/slider/%Y/%m/%d/', verbose_name='Slayder şəkil')),
                ('css_selector', models.CharField(blank=True, max_length=60, verbose_name='Css selektor')),
            ],
            options={
                'verbose_name': 'Slayder',
                'verbose_name_plural': 'Slayder',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Ad')),
                ('profession', models.CharField(max_length=60, verbose_name='Vəzifə')),
                ('image', models.ImageField(upload_to='image/team/%Y/%m/%d/', verbose_name='Şəkil')),
                ('soc_link_1', models.URLField(blank=True, null=True, verbose_name='1.Sosial şəbəkə url')),
                ('soc_icon_1', models.CharField(blank=True, max_length=20, verbose_name='1.Sosial şəbəkə ikon')),
                ('soc_link_2', models.URLField(blank=True, null=True, verbose_name='2.Sosial şəbəkə url')),
                ('soc_icon_2', models.CharField(blank=True, max_length=20, verbose_name='2.Sosial şəbəkə ikon')),
                ('soc_link_3', models.URLField(blank=True, null=True, verbose_name='3.Sosial şəbəkə url')),
                ('soc_icon_3', models.CharField(blank=True, max_length=20, verbose_name='3.Sosial şəbəkə ikon')),
                ('soc_link_4', models.URLField(blank=True, null=True, verbose_name='4.Sosial şəbəkə url')),
                ('soc_icon_4', models.CharField(blank=True, max_length=20, verbose_name='4.Sosial şəbəkə ikon')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Team',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Layihənin adı')),
                ('client', models.CharField(max_length=60, verbose_name='Müştəri')),
                ('project_date', models.DateField(verbose_name='Layihənin təhvil tarixi')),
                ('project_url', models.URLField(verbose_name='Layihə url')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Layihə məzmun')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Layihənin yükləmə tarixi')),
                ('published', models.BooleanField(default=False, verbose_name='Aktivlik')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etech.category', verbose_name='Layihənin kateqoriyası')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='İstifadəçi')),
            ],
            options={
                'verbose_name': 'Layihə',
                'verbose_name_plural': 'Layihə',
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/portfolio/%Y/%m/%d/', verbose_name='Şəkil')),
                ('portfolio', models.ForeignKey(help_text='Portfolio üçün şəkil ölçüsü 800X600', on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_images', to='etech.portfolio', verbose_name='Layihə')),
            ],
            options={
                'verbose_name': 'Layihə şəkli',
                'verbose_name_plural': 'Layihə şəkli',
            },
        ),
    ]

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Kateqoriya adı')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slaq')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriya'
        ordering = ['id']


class About(models.Model):
    image = models.ImageField(upload_to='image/about/%Y/%m/%d/', verbose_name='Şəkil', help_text='Şəkil ölçüsü: 545X470')
    title = models.CharField(max_length=60, verbose_name='Haqqımda başlıq')
    text = models.TextField(verbose_name='Haqqımda mətn')
    about_quote_1 = models.TextField(verbose_name='Haqqımda sitat 1')
    about_quote_2 = models.TextField(verbose_name='Haqqımda sitat 2')
    quote_1 = models.TextField(verbose_name='Sitat-1')
    quote_2 = models.TextField(verbose_name='Sitat-2')
    quote_3 = models.TextField(verbose_name='Sitat-3')
    quote_4 = models.TextField(verbose_name='Sitat-4')
    quote_5 = models.TextField(verbose_name='Sitat-5')
    quote_6 = models.TextField(verbose_name='Sitat-6')
    happy_clients = models.PositiveBigIntegerField(default=0, verbose_name='Məmnun müştəri sayı')
    projects = models.PositiveBigIntegerField(default=0, verbose_name='Layihə sayı')
    hours_of_support = models.PositiveBigIntegerField(default=0, verbose_name='Dəstək saatları')
    hard_workers = models.PositiveBigIntegerField(default=0, verbose_name='Aktiv işləyənlər')

    def __str__(self):
        return f"About"

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
        ordering = ['title']


class Services(models.Model):
    icon = models.CharField(max_length=100, verbose_name='Xidmət ikon', help_text='Ikinları bu saytdan götürün: icons.getbootstrap.com - MƏSƏLƏN (bi-5-circle)')
    name = models.CharField(max_length=100, verbose_name='Xidmət adı')
    text = models.TextField(verbose_name='Xidmət açıqlama')
    delay = models.PositiveBigIntegerField(verbose_name='Xidmət üçün animasiya.', default=0, blank=True, help_text='Hər xidmətə 100 vahid artırmaq lazımdır.')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Xidmət'
        verbose_name_plural = 'Xidmət'
        ordering = ['name']


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='İstifadəçi')
    title = models.CharField(max_length=250, verbose_name='Layihənin adı')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Layihənin kateqoriyası')
    client = models.CharField(max_length=60, verbose_name='Müştəri')
    project_date = models.DateField(verbose_name='Layihənin təhvil tarixi')
    project_url = models.URLField(verbose_name='Layihə url')
    text = models.TextField(null=True, blank=True, verbose_name='Layihə məzmun')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Layihənin yükləmə tarixi')
    published = models.BooleanField(default=False, verbose_name='Aktivlik')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Layihə'
        verbose_name_plural = 'Layihə'
        ordering = ['-create_date']


class Image(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, verbose_name='Layihə',
                                  related_name="portfolio_images", help_text='Portfolio üçün şəkil ölçüsü 800X600')
    image = models.ImageField(upload_to='image/portfolio/%Y/%m/%d/', verbose_name='Şəkil')

    def __str__(self):
        return f"{self.image}"

    class Meta:
        verbose_name = 'Layihə şəkli'
        verbose_name_plural = 'Layihə şəkli'


class Team(models.Model):
    name = models.CharField(max_length=60, verbose_name='Ad')
    profession = models.CharField(max_length=60, verbose_name='Vəzifə')
    image = models.ImageField(upload_to='image/team/%Y/%m/%d/', verbose_name='Şəkil')
    soc_link_1 = models.URLField(null=True, blank=True, verbose_name='1.Sosial şəbəkə url')
    soc_icon_1 = models.CharField(max_length=20, blank=True, verbose_name='1.Sosial şəbəkə ikon')
    soc_link_2 = models.URLField(null=True, blank=True, verbose_name='2.Sosial şəbəkə url')
    soc_icon_2 = models.CharField(max_length=20, blank=True, verbose_name='2.Sosial şəbəkə ikon')
    soc_link_3 = models.URLField(null=True, blank=True, verbose_name='3.Sosial şəbəkə url')
    soc_icon_3 = models.CharField(max_length=20, blank=True, verbose_name='3.Sosial şəbəkə ikon')
    soc_link_4 = models.URLField(null=True, blank=True, verbose_name='4.Sosial şəbəkə url')
    soc_icon_4 = models.CharField(max_length=20, blank=True, verbose_name='4.Sosial şəbəkə ikon')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'


class Contact(models.Model):
    logo = models.ImageField(upload_to='image/logo/%Y/%m/%d/')
    address = models.CharField(max_length=250, verbose_name='Ünvan')
    email = models.EmailField(verbose_name='Email')
    phone_1 = models.CharField(max_length=60, verbose_name='Telefon 1', null=True, blank=True)
    phone_2 = models.CharField(max_length=60, verbose_name='Telefon 2', null=True, blank=True)
    soc_link_1 = models.URLField(null=True, blank=True, verbose_name='1.Sosial şəbəkə url')
    soc_icon_1 = models.CharField(max_length=20, blank=True, verbose_name='1.Sosial şəbəkə ikon')
    soc_link_2 = models.URLField(null=True, blank=True, verbose_name='2.Sosial şəbəkə url')
    soc_icon_2 = models.CharField(max_length=20, blank=True, verbose_name='2.Sosial şəbəkə ikon')
    soc_link_3 = models.URLField(null=True, blank=True, verbose_name='3.Sosial şəbəkə url')
    soc_icon_3 = models.CharField(max_length=20, blank=True, verbose_name='3.Sosial şəbəkə ikon')
    soc_link_4 = models.URLField(null=True, blank=True, verbose_name='4.Sosial şəbəkə url')
    soc_icon_4 = models.CharField(max_length=20, blank=True, verbose_name='4.Sosial şəbəkə ikon')

    def __str__(self):
        return f"{self.address}"

    class Meta:
        verbose_name = 'Əlaqə'
        verbose_name_plural = 'Əlaqə'


class Slider(models.Model):
    title = models.CharField(max_length=250, verbose_name='Slayder başlıq')
    text = models.TextField(verbose_name='Slayder mətn')
    image = models.ImageField(upload_to='image/slider/%Y/%m/%d/', verbose_name='Slayder şəkil',
                              help_text='Slayder üçün şəkil ölçüsü: 1920X1080')
    css_selector = models.CharField(max_length=60, verbose_name='Css selektor', blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Slayder'
        verbose_name_plural = 'Slayder'
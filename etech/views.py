from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .forms import PortfolioForm, ImageForm
from .models import Category, About, Services, Portfolio, Team, Contact, Image, Slider


class IndexView(ListView):
    model = Portfolio
    template_name = 'etech/index.html'
    context_object_name = 'portfolios'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['abouts'] = About.objects.all()
        context['categories'] = Category.objects.all()
        context['services'] = Services.objects.all()
        context['teams'] = Team.objects.all()
        context['contacts'] = Contact.objects.all()
        context['sliders'] = Slider.objects.all()
        return context


class Detail(DetailView):
    model = Portfolio
    template_name = 'etech/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def create_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        files = request.FILES.getlist("image")

        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            for i in files:
                Image.objects.create(portfolio=f, image=i)

            return redirect('index')
    else:
        form = PortfolioForm
        image_form = ImageForm()
        contacts = Contact.objects.all()
        context = {
            'form': form,
            'image_form': image_form,
            'contacts': contacts
        }
        return render(request, 'etech/portfolio.html', context=context)


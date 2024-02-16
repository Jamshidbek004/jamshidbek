from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import ListView
# return redirect('user_profile')

from .models import News, Category,Magazin,Follow_us,Get_in_touch,Telfon
from .forms import ContactForm, emailForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    yangiliklar = News.objects.all()
    follow = Follow_us.objects.all()
    form1 = emailForm(request.POST or None)
    if request.method == "POST" and form1.is_valid():
        form1.save()
    rasmlar = Magazin.objects.all()
    categorya = Category.objects.all()
    get = Get_in_touch.objects.all()
    populyar = News.objects.filter(korishlarsoni=10)
    context = {
        "rasm": rasmlar,
        "yangilik": yangiliklar,
        "form": form1,
        "category": categorya,
        "follow": follow,
        "get": get,
        "populyar": populyar,
    }
    return render(request, "index.html", context=context)
def Reklama(request):
    return render(request, "Reklama.html", context={})
def single(request):
    yangiliklar2 = News.objects.all()
    yangiliklar = News.objects.all()
    rasmlar = Magazin.objects.all()
    categorya1 = Category.objects.all()
    get = Get_in_touch.objects.all()
    populyar = News.objects.filter(korishlarsoni=10)
    form4 = emailForm(request.POST or None)
    form5 = CommentForm(request.POST or None)
    if request.method == "POST" and form4.is_valid():
        form4.save()
    if request.method == "POST" and form5.is_valid():
        form5.save()
    categorya = Category.objects.all()
    context = {
        "form2": form4,
        "form3": form5,
        "yangilik": yangiliklar,
        "yangilik2": yangiliklar2,
        "kategorya1" : categorya1,
        "category": categorya,
        "rasm": rasmlar,
        "get": get,
        "populyar": populyar

    }
    return render(request, "single.html", context=context)
@login_required
def singlenews(request,id=id):
    yangilik = get_object_or_404(News, id=id)
    categorya = Category.objects.all()
    yangiliklar2 = News.objects.all()
    rasmlar = Magazin.objects.all()
    get = Get_in_touch.objects.all()
    populyar = News.objects.filter(korishlarsoni=10)
    post = get_object_or_404(News, id=id)
    if post:
        post.korishlarsoni = post.korishlarsoni + 1
        post.save()
    form = CommentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    context = {
        "detel": yangilik,
        "form": form,
        "kategorya": categorya,
        "yangilikLar": yangiliklar2,
        "rasm": rasmlar,
        "get": get,
        "populyar": populyar
    }
    return render(request, "singlenews.html", context=context)
def category(request):
    yangiliklar1 = News.objects.all()
    categorya5 = Category.objects.all()
    rasmlar = Magazin.objects.all()
    get = Get_in_touch.objects.all()
    yangiliklar = News.objects.all()
    populyar = News.objects.filter(korishlarsoni=10)
    categorya = Category.objects.all()
    form2 = emailForm(request.POST or None)
    if request.method == "POST" and form2.is_valid():
        form2.save()
    context = {
        "yangilik1": yangiliklar1,
        "categorya": categorya5,
        "category": categorya,
        "form": form2,
        "rasm": rasmlar,
        "get": get,
        "populyar": populyar,
        "yangilik": yangiliklar,
    }
    return render(request, "category.html", context=context)
def contact(request):
    rasmlar = Magazin.objects.all()
    get = Get_in_touch.objects.all()
    yangiliklar = News.objects.all()
    populyar = News.objects.filter(korishlarsoni=10)
    categorya = Category.objects.all()
    form2 = emailForm(request.POST or None)
    form3 = ContactForm(request.POST or None)
    if request.method == "POST" and form2.is_valid():
        form2.save()
    if request.method == "POST" and form3.is_valid():
        form3.save()
    context = {

        "form": form2,
        "form1": form3,
        "yangilik": yangiliklar,
        "category": categorya,
        "rasm": rasmlar,
        "get": get,
        "populyar": populyar
    }
    return render(request, "contact.html", context=context)

class SearchResultList(ListView):
    model = News
    template_name = 'search_result.html'
    context_object_name = 'barcha_yangiliklar'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.objects.filter(
            Q(nom__icontains=query) | Q(kontent__icontains=query)

        )

def news_detail(request, news):
    news = get_object_or_404(News, slug=news)
    comments = news.comments.filter()
    new_comment = None
    if request.method == "POST":
        comment_form = ContactForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = news
            new_comment.user = request.user
            new_comment.save()
    else:
        comment_form = ContactForm()

    context = {
        "news": news,
        'comments':comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request,'news_detail.html', context=context)

def Tag_detail(request,id=id):
    news = News.objects.filter(kategory=id)
    categorya = Category.objects.all()
    context = {
        "tag_detel": news,
        "categorya": categorya,
    }
    return render(request, 'tag_detel.html', context=context)
def tel(request):
    y = Telfon.objects.all()
    context = {
        "tel": y
    }
    return render(request,"tel.html",context=context)

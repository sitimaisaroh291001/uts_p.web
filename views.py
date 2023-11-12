from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member

def index(request):
    context = {
        'member_list' : Member.object.all()
    }
    return render(request, "members/index.html", context)

def add(request):
    return render(request, "members/form.html")

def save(request):
    buku = Book(
        judul = request.POST['judul']
        publish = request.POST['publish']
    )
    buku.save()

    return HttpResponseRedirect(reverse('members.index'))
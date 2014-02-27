# Create your views here.
#roster/views.py

from django.shortcuts import render
from roster.models import Player
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
  return render(request, "roster/home.html")

def player(request, pk):
  #player = Player.objects.order_by('?')[0]
  player = get_object_or_404(Player, id=pk)
  return render(request, "roster/player.html", {'player': player})

def playerList(request):
   
    player_list = Player.objects.all()
    paginator = Paginator(player_list, 25)
    page = request.GET.get('page')
    try:
        players= paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        players = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        players = paginator.page(paginator.num_pages)

    return render(request, 'roster/player_list.html', {"players": players})

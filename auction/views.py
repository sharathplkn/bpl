from django.shortcuts import render, redirect
from .models import team, player
import random
from django.core.paginator import Paginator
from .forms import AuctionForm
from django.shortcuts import get_object_or_404

def home(request):
    teams = team.objects.all()
    players = player.objects.all()
    context = {
        'teams': teams,
        'players': players,
    }
    return render(request, 'auction/home.html', context)

def clubs(request):
    clubs = team.objects.all()
    return render(request, 'auction/clubs.html', {'clubs': clubs})

def team_detail(request, team_id):
    team_obj = get_object_or_404(team, id=team_id)
    players = team_obj.players.all()  # Assuming you want to display players of the team
    return render(request, 'auction/team_detail.html', {'team': team_obj, 'players': players})

def players(request):
    players_list = player.objects.all()  # Query all players
    paginator = Paginator(players_list, 18)  # Show 6 players per page
    page_number = request.GET.get('page')  # Get current page number from GET params
    players = paginator.get_page(page_number)  # Get the players for the current page

    return render(request, 'auction/player.html', {'players': players})



def auction(request, player_id):
    teams = team.objects.all()  # Fetch all teams to display their remaining purse
    current_player = get_object_or_404(player, id=player_id)

    if request.method == 'POST':
        form = AuctionForm(request.POST)
        if form.is_valid():
            selected_team = form.cleaned_data.get('team')
            price = form.cleaned_data.get('price')

            if selected_team and price and selected_team.purse_remaining >= price:
                current_player.team = selected_team
                current_player.base_price = price
                current_player.save()
                selected_team.purse_remaining -= price
                selected_team.save()

            return redirect('players')  # Redirect back to the player cards page after the auction

    else:
        form = AuctionForm()

    return render(request, 'auction/auction.html', {
        'player': current_player,
        'form': form,
        'teams': teams,
    })

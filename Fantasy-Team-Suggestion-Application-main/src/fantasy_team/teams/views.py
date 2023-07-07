from django.shortcuts import render, redirect
# from .forms import TeamsForm
from .models import Player
import pandas as pd

# Create your views here.
from django.contrib import messages
df = pd.read_csv('merged_data_for_janhavi.csv')

def Display(request):
    if(request.method=='POST'):
        team1 = request.POST['team1']
        team2 = request.POST['team2']
        print(team1, team2)
        if(team1==team2):
            messages.error(request,'same teams cannot be selected')
            return redirect('home')
        print(request.POST)

        df1 = df[df['team_name']==team1]
        df2 = df[ df['team_name']==team2]
        newdf = pd.concat([df1,df2],axis=0)
        newdf = newdf.sort_values(by=['fantasy_points'],ascending=False)
        print(newdf)
        topPlayers = []
        for i in range(1,11,1):
            print(newdf.iloc[i] )
            topPlayers.append(newdf.iloc[i])
        print(topPlayers)


        # topPlayers = Player.objects.filter(TeamName__in=[team1, team2]).distinct()
        # topPlayers = topPlayers.order_by("-FantasyPoints")[:11]
        context = {
            "players": topPlayers,
        }
        return render(request, "template.html", context)
    return redirect('home')

# def LoadCSV(request):
#   data = pd.read_csv('merged_data_for_janhavi.csv', sep=',')
#   for i in range(len(data)):
#     player = Player(Name=data.iloc[i][2], TeamName=data.iloc[i][1], FantasyPoints=float(data.iloc[i][3]))
#     player.save()
#   return render(request, "dataload.html", {"players": Player.objects.all()})

def Menu(request):
    # form = TeamsForm(request.POST or None)
    # message = None
    # if request.POST:
    #     if form.is_valid():
    #         team1 = form.cleaned_data["Team1"]
    #         team2 = form.cleaned_data["Team2"]
    #         return redirect("recommend", team1=team1, team2=team2)
    #     else: message = form.errors
    # else:
    #     form = TeamsForm(None)
    #     return render(request, "menu.html", {"form": form})
    # print(form.Team1)
    # context = {
    #     "form": form,
    #     "msg" : message,
    # }
    context ={}
    # print(context)
    return render(request, "menu.html", context)

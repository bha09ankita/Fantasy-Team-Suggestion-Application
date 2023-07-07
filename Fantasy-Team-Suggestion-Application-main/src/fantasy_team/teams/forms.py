from django import forms
from .models import Player

teamchoices = (
  ("Chennai Super Kings", "Chennai Super Kings"),
  ("Mumbai Indians", "Mumbai Indians"),
)

def TeamChoices():
  team = ()
  n = 0
  try:
    teams = Player.objects.values('TeamName').distinct()
    for t in teams:
      n = n + 1
      team = (*team, (t['TeamName'], t['TeamName']))
  except:
    team = None
  return team

class TeamsForm(forms.Form):

  Team1 = forms.ChoiceField(
    required=True,
    widget=forms.Select(choices=TeamChoices()),
  )
  Team2 = forms.ChoiceField(
    required=True,
    widget=forms.RadioSelect,
    choices=TeamChoices(),
  )

  class Meta:
    fields = ["Team1", "Team2"]

  def clean(self):
    super(TeamsForm, self).clean()
    team1 = self.cleaned_data.get("Team1")
    team2 = self.cleaned_data.get("Team2")
    if team1==team2: self.errors["teams"] = self.error_class(["Both choice cannot be same. Please chose 2 different teams."])
    return self.cleaned_data
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TeamForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from account.models import Account
from lead.models import Lead
from client.models import Client
from django.contrib import messages

User = get_user_model()

# Create your views here.
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.manager = request.user
            team.save()

            team_manager = team.manager
            team_manager_acc = get_object_or_404(Account, user=team_manager)
            team_manager_acc.team = team
            team_manager_acc.save()
            if team.member1:
                user1 = team.member1
                acc1 = get_object_or_404(Account, user=user1)
                acc1.team = team
                acc1.save()
            if team.member2:
                user2 = team.member2
                acc2 = get_object_or_404(Account, user=user2)
                acc2.team = team
                acc2.save()
            if team.member3:
                user3 = team.member3
                acc3 = get_object_or_404(Account, user=user3)
                acc3.team = team
                acc3.save()
            if team.member4:
                user4 = team.member4
                acc4 = get_object_or_404(Account, user=user4)
                acc4.team = team
                acc4.save()
            return redirect('home') 
    else:
        form = TeamForm()
    return render(request, 'team/create_team.html', {'form': form})
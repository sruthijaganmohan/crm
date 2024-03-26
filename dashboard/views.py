from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from lead.models import Lead
from client.models import Client
from team.models import Team
from account.models import Account

# Create your views here.
@login_required
def dashboard(request):
    acc = get_object_or_404(Account, user=request.user)
    team = acc.team
    my_leads = Lead.objects.filter(created_by=request.user, converted_to_client=False).order_by('-created_at')[0:5]
    my_clients = Client.objects.filter(created_by=request.user).order_by('-created_at')[0:5]
    leads = Lead.objects.filter(team=team, converted_to_client=False).order_by('-created_at')
    clients = Client.objects.filter(team=team).order_by('-created_at')
    return render(request, 'dashboard/dashboard.html', {'leads':leads, 'clients':clients, 'my_leads':my_leads, 'my_clients':my_clients})
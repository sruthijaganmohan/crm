from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddLeadForm, AddCommentForm
from .models import Lead, Comment
from account.models import Account
from client.models import Client
from team.models import Team

# Create your views here.
@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by=request.user, converted_to_client=False)
    return render(request, 'lead/leads_list.html', {'leads':leads})

@login_required
def view_lead(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    team = lead.team
    comments = Comment.objects.filter(team=team)
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_by = request.user
            comment.lead = lead
            comment.team = lead.team
            comment.save()
            messages.success(request, "Successfully added comment")
            return redirect('dashboard')
    else:
        form = AddCommentForm()
    return render(request, 'lead/view_lead.html', {'lead':lead, 'comments':comments, 'form':form})

@login_required
def add_lead(request):
    if request.method == "POST":
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            acc = get_object_or_404(Account, user=request.user)
            lead.team = acc.team
            lead.save()
            messages.success(request, "Successfully created lead")
            return redirect('leads_list')
    else:
        form = AddLeadForm()
    return render(request, 'lead/add_lead.html', {'form':form})

@login_required
def delete_lead(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()
    messages.success(request, "Successfully deleted lead")
    return redirect('leads_list')

@login_required
def update_lead(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    if request.method == "POST":
        form = AddLeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated lead")
            return redirect('leads_list')
    else:
        form = AddLeadForm(instance=lead)
    return render(request, 'lead/update_lead.html', {'form':form})

@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    acc = get_object_or_404(Account, user=request.user)
    lead.team = acc.team
    client = Client.objects.create(name=lead.name, email=lead.email, description=lead.description, team=lead.team, created_by=request.user)
    lead.converted_to_client = True
    lead.save()
    messages.success(request, "Lead converted to client")
    return redirect('leads_list')



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddClientForm, AddCommentForm, ContactForm
from .models import Client, Comment
from team.models import Team
from account.models import Account
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
@login_required
def clients_list(request):
    clients = Client.objects.filter(created_by=request.user)
    return render(request, 'client/clients_list.html', {'clients':clients})

@login_required
def view_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    team = client.team
    comments = Comment.objects.filter(team=team)
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_by = request.user
            comment.client = client
            comment.team = client.team
            comment.save()
            messages.success(request, "Successfully added comment")
            return redirect('dashboard')
    else:
        form = AddCommentForm()
    return render(request, 'client/view_client.html', {'client':client, 'comments':comments, 'form':form})

@login_required
def add_client(request):
    if request.method == "POST":
        form = AddClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.created_by = request.user
            acc = get_object_or_404(Account, user=request.user)
            client.team = acc.team
            client.save()
            messages.success(request, "Successfully created client")
            return redirect('clients_list')
    else:
        form = AddClientForm()
    return render(request, 'client/add_client.html', {'form':form})

@login_required
def delete_client(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    client.delete()
    messages.success(request, "Successfully deleted client")
    return redirect('clients_list')

@login_required
def update_client(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    if request.method == "POST":
        form = AddClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated client")
            return redirect('clients_list')
    else:
        form = AddClientForm(instance=client)
    return render(request, 'client/update_client.html', {'form':form})

@login_required
def contact_client(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.subject = request.POST['subject']
            contact.email = client.email
            contact.content = request.POST['content']
            contact.save()
            send_mail(
                contact.subject,
                contact.content,
                'settings.EMAIL_HOST_USER',
                [contact.email],
                fail_silently=False
            )
    else:
        form = ContactForm()
    return render(request, 'client/contact_client.html', {'form':form})
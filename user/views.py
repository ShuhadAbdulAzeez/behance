from multiprocessing import context
from django.shortcuts import render,redirect
from . forms import CustomCreationForm
from django.contrib.auth import login

def registerUser(request):
    form = CustomCreationForm()
    
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            print("login successful")
            
            login(request, user)
            return redirect("home")
        else:
            print("login unsuccessful")
    
    context = {'form': form}
    
    return render(request, 'signup.html', context)
        
    

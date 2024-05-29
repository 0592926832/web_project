from django.shortcuts import render
from webdjango.models import MyModel
from django.contrib import messages

def create_view(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('email_address') and request.POST.get('password'): 
           saverecord=MyModel()
           saverecord.username=request.POST.get('username')
           saverecord.email_address=request.POST.get('email_address')
          # saverecord.id=request.POST.get('id')
           saverecord.password=request.POST.get('password')
           saverecord.save()
           messages.success(request,'record saved successfully!')
           return render(request, 'regester.html')
    else:
           return render(request, 'regester.html')
     
      #  username=request.POST['username']
      #  email_address=request.POST['email_address']
      #  id=request.POST['id']
      #  password=request.POST['password']

      #  new_registration=MyModel(username=username, email_address=email_address,id=id, password=password)
       # new_registration.save()



    ##    form = MyModel(request.POST)
       # if form.is_valid():
       #     form.save()
       #     return redirect('success')
  #  else:
   #     form = MyModel()
  #  return render(request, 'C:\xampp\htdocs\mango\View\regester.html', {'form': form})

#def success_view(request):
   # 

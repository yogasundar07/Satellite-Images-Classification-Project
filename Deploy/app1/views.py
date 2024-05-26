from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from . forms import CreateUserForm, UserImageForm
from django.contrib import messages
from . models import UserImageModel
import numpy as np
from PIL import Image, ImageOps
from tensorflow import keras
import matplotlib.pyplot as plt
from PIL import Image,ImageOps
plt.rcParams['figure.figsize'] = (12, 12)
plt.rcParams['axes.grid'] = False


def register(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('loginpage')

    context = {'form':form}
    return render(request, 'Register.html', context)


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request, 'log_in.html', context)


def logoutusers(request):
    return redirect('log_in.html')

def Home(request):
    return render(request, 'Home.html')

def landingpage(request):
    return render(request, 'landing.html')

def problem_statement(request):
    return render(request, '5_problem_statement.html')

def model(request):
    print("HI")
    if request.method == "POST":
        form = UserImageForm(files=request.FILES)
        if form.is_valid():
            print('HIFORM')
            form.save()
        obj = form.instance
        #('obj',obj)
        result1 = UserImageModel.objects.latest('id')
        models = keras.models.load_model('C:/Users/yogas/Desktop/ITPDL05 - SATELIGHT/ITPDL05 - SATELIGHT/Deploy/app1/keras_model.h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open("C:/Users/yogas/Desktop/ITPDL05 - SATELIGHT/ITPDL05 - SATELIGHT/Deploy/media/" + str(result1)).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        classes = ['cloudy','desert','green_area','shipsnet','water','wildfire']
        prediction = models.predict(data)
        idd = np.argmax(prediction)
        a = (classes[idd])
        if a == 'cloudy':
            a = 'cloudy'
        elif a == 'desert':
            a = 'desert'
        elif a == 'green_area':
            a = 'green_area'
        elif a == 'shipsnet':
            a = 'shipsnet'
        elif a == 'water':
            a = 'water'
        elif a == 'wildfire':
            a = 'wildfire'
        else:
            a = 'Give correct Images'
        
        # obj = UserImageModel.label
        return render(request, 'output.html',{'form':form,'obj':obj,'predict':a})
    else:
        form = UserImageForm()
    return render(request, 'model.html',{'form':form})



def model_database(request):
    models = UserImageModel.objects.all()
    return render(request, 'model_database.html', {'models':models})
    
def Domain_result(request):
    return render(request,'Domain_result.html')
    

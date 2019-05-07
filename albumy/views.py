from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Album, UserData
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, get_user_model, login, logout

def index(req):

    albumy = Album.objects.all()[2:100]
    tiles = ['Albumy','Wykonawcy','Ceny','Promocje']
    images=['vinyl.jpg', 'nutki.jpg', 'brs.jpg', 'gitar.jpg']
    aha ={
        'a': {
            'tiles': 'Albumy',
            'images': 'vinyl.jpg'
        },
        'b': {
            'tiles': 'Wykonawcy',
            'images': 'nutki.jpg'
        },
        'c': {
            'tiles': 'Ceny',
            'images': 'gitar.jpg'
        },
        'd': {
            'tiles': 'Zespoly',
            'images': 'brs.jpg'
        }
    }
    
    context={
        'tiles': tiles,
        'albums': albumy,
        'images':images,
        'aha' :aha,
        'is_logged': False
    }
    return render(req, 'albumy/index.html',context)


def indexForLogged(req):
    albumy = Album.objects.all()[2:100]
    user = UserData.objects.order_by('-pk')[0]
    tiles = ['Albumy', 'Wykonawcy', 'Ceny', 'Promocje']
    images = ['vinyl.jpg', 'nutki.jpg', 'brs.jpg', 'gitar.jpg']
    aha = {
        'a': {
            'tiles': 'Albumy',
            'images': 'vinyl.jpg'
        },
        'b': {
            'tiles': 'Wykonawcy',
            'images': 'nutki.jpg'
        },
        'c': {
            'tiles': 'Ceny',
            'images': 'gitar.jpg'
        },
        'd': {
            'tiles': 'Zespoly',
            'images': 'brs.jpg'
        }
    }

    context = {
        'tiles': tiles,
        'albums': albumy,
        'images': images,
        'aha': aha,
        'is_logged': True,
        'user': user,
    }
    return render(req, 'albumy/index.html', context)

def registration(req):
    cntx = {'form' :RegisterForm }
    return render(req, 'albumy/register.html', cntx)


def logging(req):
    cntx = {'form': LoginForm}
    return render(req, 'albumy/login.html', cntx)

def status(req):
    st = {'good': 'Congratulations!',
           'bad': 'Sorry, you fucked up'}

    return render(req, 'albumy/status.html', st)

def addUser(req):
    form = RegisterForm(req.POST)

    if form.is_valid():
        register = UserData(
            name = form.cleaned_data['name'],
            last_name = form.cleaned_data['last_name'],
            nick = form.cleaned_data['nick'],
            email = form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )
        register.save()
    return redirect('/albumy/status')


def checkIfUsername(nik):
        for x in UserData.objects.all():
            if x.nick == nik:
                return True
        return False


def checkIfPass(pas):
        for x in UserData.objects.all():
            if x.password == pas:
                return True
        return False
if checkIfPass('adven'):
    print("taaaaaaaaaaaaaa  HASLO")    
if checkIfUsername('adven997'):
    print("taa USER")
    
def getUser(req):
    form = LoginForm(req.POST)

    if form.is_valid():
        nick=form.cleaned_data.get('nick')
        password=form.cleaned_data.get('password')
        user = checkIfUsername(nick)
        pasw = checkIfPass(password)
        if user == True or pasw==True:
            return redirect('/albumy/status')
        else:
            return redirect('/')\
            # raise form.ValidationError('lipton')

    else:
        print('nieeen neiee nieee')
        return redirect('/logging')
    # cntx = {'form': form}
    # return render(req, 'albumy/login.html', cntx)

# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Posts

# def index(req):
#     # return HttpResponse('HELLO THERE GEN KENOBI')

#     posts = Posts.objects.all()[:10]
#     context ={
#         'title': 'Latest POsts',
#         'posts': posts
#     }

#     return render(req, 'posts/index.html',context)


# def details(req, id):
#     post = Posts.objects.get(id=id)

#     context={
#         'post': post
#     }

#     return render(req, 'posts/details.html', context)

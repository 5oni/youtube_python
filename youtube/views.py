from django.shortcuts import render,redirect
from .forms import loginView,registerView,NewVideo,CommentForm
from django.views.generic.base import View ,HttpResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from .models import  Video,Comment,Channel
import random,string
from django.db.models import F


from django.contrib.auth import get_user_model
from django_email_verification import send_email
import time
class Homeview(View):
    template1="youtube/index.html"
    
    # print(most_recent_videos)
    def get(self,request):
        most_recent_videos=Video.objects.all().order_by("-datetime")
        username=request.user    
        return render(request,self.template1,{'username':username,'most_recent_videos':most_recent_videos})
   


class loginview(View):
    template_name="youtube/login.html"
    def get(self,request):
        form=loginView()
        print(form)
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form=loginView(request.POST)
        print("going in")
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            print("In form",username,password)
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                print("in user")
                login(request, user)
                return redirect('/')     
        form=loginView()
        return render(request,self.template_name,{"wrong":1,"form":form})



class registerview(View):
    template_name="youtube/register.html"
    def get(self,request):
        form=registerView()
        return render(request,self.template_name,{'form':form,'wrong':0})
    def post(self,request):
        form=registerView(request.POST)
        if form.is_valid():
            print("YES")
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            email=form.cleaned_data["email"]
            
            new_user=get_user_model().objects.create(username=username,email=email)
            new_user.set_password(password)
            
            send_email(new_user)
            try:
                channel=Channel(user=new_user)
                channel.save()
                # send_mail(subject="check",message="Success !",from_email=None,recipient_list=[email,])
            except:
                print("error h bhai")
                return redirect('/register/')
            return redirect('/login/')
        
            
    
class newvideo(View):
    template1="youtube/new_video.html"
    def get(self,request):
        username=request.user
        if not username.is_authenticated:
            return redirect('/login/',{'username':username})
        form=NewVideo()
        return render(request,self.template1,{'username':username,"form":form})
        
    def post(self,request):
        form=NewVideo(request.POST,request.FILES)

        if form.is_valid():
            # print(dir(request))
            # form.user=request.user
            title=form.cleaned_data["title"]
            desc=form.cleaned_data["desc"]
            file=form.cleaned_data["videofile"]
            random_str="".join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.ascii_uppercase,k=10))
            
            # print(file.name)
            path=random_str+file.name
            new_video=Video(title=title,desc=desc,path=path,user=request.user,videofile=file)
            new_video.save()
            return redirect('/video/{}'.format(new_video.id))
        return render(request,self.template1,{'username':request.user})


class LogoutView(View):
    template1="youtube/index.html"
    def get(self,request):
        if request.user.is_authenticated:
            logout(request)
            return redirect("/")
        var1="index view"
        return render(request,self.template1,{'var1':var1})
    def post(self,request):
        var1="index view"
        return render(request,self.template1,{'var1':var1})


class VideoView(View):
    template_1="youtube/video.html"
    def get(self,request,id):
        username=request.user
        try:
            video=Video.objects.get(id=id)
            comment_form=CommentForm()
        except:
            return HttpResponse("<h2>Video dosent exist</h2>")
        try:
            comments=Comment.objects.filter(video=video).order_by('-datetime')
        except:
            comments=[]
        video_path=video.videofile
        recommendations=Video.objects.filter(user=video.user)
         
        channel=Channel.objects.get(user_id=video.user.id)

        total_subs=channel.total_subs()
        is_liked = False
        is_disliked = False
        is_subscribed = False

        if channel.subs.filter(username=request.user).exists():
            is_subscribed=True
        if video.like.filter(username=request.user).exists():
            is_liked = True
        if video.dislike.filter(username=request.user).exists():
            is_disliked = True
        context={"is_liked":is_liked,"is_disliked":is_disliked,"is_subscribed":is_subscribed,'total_subs':total_subs,'video':video,'form':comment_form,"comments":comments,'username':username,'video_path':video_path,"recommendations":recommendations}
        return render(request,self.template_1,context)

    def post(self,request,id):
        form=CommentForm(request.POST)
        if form.is_valid():
            text=form.cleaned_data['text']
            video=Video.objects.get(id=id)
            new_comment=Comment(user=request.user,text=text,video=video)
            new_comment.save()
            return redirect("/video/{}/".format(id))
        
        return redirect("/video/{}/".format(id))

        

class ChannelView(View):
    template_name ="youtube/channel.html"
    def get(self,request):
        username=request.user
        videos=Video.objects.filter(user=username).order_by("-datetime")
    
        return render(request,self.template_name,{"videos":videos,'username':username})


class LorDView(View):
    template_name ="youtube/video.html"
    def get(self,request,lord,id):
        if request.user.is_authenticated:
            video=Video.objects.get(id=id)
            if lord==11:
                video.like.remove(request.user)
                is_liked=False
            elif lord==10:
                if video.dislike.filter(username=request.user).exists():
                    is_disliked = False
                    video.dislike.remove(request.user)
                video.like.add(request.user)
                is_liked=True
            elif lord==1:
                video.dislike.remove(request.user)
                is_disliked=False
            elif lord==12:
                if video.like.filter(username=request.user).exists():
                    is_liked = False
                    video.like.remove(request.user)
                video.dislike.add(request.user)
                is_disliked=True
            return redirect("/video/{}/".format(id))
        else:
            return redirect("/login")
        

class subview(View):
    template_name ="youtube/video.html"
    def post(self, request,Vid,id):
        if request.user.is_authenticated:
            video_user=Video.objects.get(id=Vid).user
            print(video_user)
            channel=Channel.objects.get(user_id=id)
            my_channel=Channel.objects.get(user_id=request.user.id)
            print(my_channel,channel)
            if channel.subs.filter(username=request.user).exists():
                channel.subs.remove(request.user)
                my_channel.my_sub_channels.remove(video_user)
            else:
                channel.subs.add(request.user)
                my_channel.my_sub_channels.add(video_user)
            return redirect("/video/{}/".format(Vid))
        else:
            return redirect("/login")
    



class subscribtions_View(View):
    template_name="youtube/subscription.html"
    def get(self, request):
        username = request.user
        channel=Channel.objects.get(user=username)
        my_subs=channel.my_sub_channels.all()
        my_sub_videos=[]
        for i in my_subs:
            sub_videos=Video.objects.filter(user=i)
            for j in sub_videos:
                my_sub_videos.append(j)
        print(my_sub_videos)
        return render(request,self.template_name,{'username':username,'my_sub_videos':my_sub_videos})

        



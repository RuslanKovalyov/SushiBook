from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from .forms import UpdateCustomUserForm, UpdateProfileForm, CreatePostForm, LikePostForm
from django.contrib import messages

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateCustomUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to=request.user.profile.get_absolute_url())
    else:
        user_form = UpdateCustomUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})

from PIL import Image
import random
from django.db import models
@login_required
def rotate_avatar_by_90_degrees(request):
    #rotate foto
    avatar = request.user.profile.avatar
    if  avatar != request.user.profile.default_avatar:
        Image.open(avatar.path).rotate(angle = -90, expand=True).save(avatar.path)

        # #chenge name
        # extension = avatar.path.split('.')[-1]
        # filename = str(avatar.path).split('.')
        # filename.pop()
        # name= ''
        # for n in filename:
        #     name+=n
        # for _ in range(4):
        #     name+=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        # new_filename = "%s.%s" % (name, extension)

        # print('avatar .............')
        # print('avatar       --- %s'%(avatar))
        # print('new_filename --- %s'%(new_filename))
        # print('avatar.path  --- %s'%(avatar.path))

        # Image.open(avatar.path).rotate(angle = 90, expand=True).save(new_filename)

        # extension = avatar.path.split('.')[-1]
        # filename = str(avatar).split('.')
        # filename.pop()
        # name= ''
        # for n in filename:
        #     name+=n
        # for _ in range(4):
        #     name+=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        # new_filename = "%s.%s" % (name, extension)
        # request.user.profile.avatar = models.ImageField(default=request.user.profile.default_avatar, upload_to=new_filename)

    return redirect(edit_profile)

@login_required
def rotate_background(request):
    #rotate foto
    background = request.user.profile.profile_background
    if  background != request.user.profile.default_background:
        Image.open(background.path).rotate(angle = -90, expand=True).save(background.path)
    return redirect(edit_profile)

def password_changed(request):
    return render(request, "registration/password_changed.html")

from .models import Profile, Post, PostLike, PostComment

# mail activation
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .models import CustomUser, Profile
def send_activation_email(request, user):
    token_generator = default_token_generator
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = token_generator.make_token(user)
    activation_url = request.build_absolute_uri(
        f'/activate/{uid}/{token}'
    )
    html_message = render_to_string('mail/activation_email.html', {
        'user': user,
        'activation_url': activation_url,
    })
    send_mail(
        subject='Activate your account',
        message=None,
        html_message=html_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )

def sign_up(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)

            send_activation_email(request, user)
            return redirect(to='activation_sent')

            # next is ald version without email activation
            # login(request,user)
            # return redirect(to=request.user.profile.get_absolute_url())

    context = { 'form':form,
                'ENABLE_RECAPTCHA': settings.ENABLE_RECAPTCHA,
                }
    return render(request, 'registration/sign_up.html', context)

def activation_sent(request):
    return render(request, 'registration/activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    token_generator = default_token_generator
    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated')
        return redirect('activation_success')

    else:
        messages.error(request, 'Activation link is invalid or has expired')
        return redirect('activation_error')
        # send new link

def activation_success(request):
    return render(request, 'registration/activation_success.html')

def activation_error(request):
    return render(request, 'registration/activation_error.html')

def logout_view(request):
    logout(request)
    return redirect(to='home')
    
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile

class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    paginate_by = 7

class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post

@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user.profile
            if form.story or form.picture or form.title:
                form.save()
                messages.success(request, 'Post created successfully')
            return redirect(to='/Community')
    else:
        form = CreatePostForm()
    return render(request, 'users/create_post.html', {'form': form,})

from django.shortcuts import get_object_or_404
from .forms import RenewPostForm

@login_required#chech permission to chenges!
def renew_post(request, pk):
    post_inst = get_object_or_404(Post, pk=pk)
    
    #if post.autor!=profile:
    if Post.objects.get(pk=pk).author != request.user.profile:
            return redirect(to=request.user.profile.get_absolute_url())

        
    if request.method == 'POST':
        # Создаём экземпляр формы и заполняем данными из запроса (связывание, binding):
        form = RenewPostForm(request.POST, request.FILES, instance=post_inst)

        if form.is_valid():
            # Обработка данных из form.cleaned_data
            #(здесь мы просто присваиваем их полю due_back)
            post_inst.save()
            #return redirect(to='/Community/')
            return redirect(to=request.user.profile.get_absolute_url())

    # Если это GET (или какой-либо ещё), создать форму по умолчанию.
    else:
        form = RenewPostForm(instance=post_inst)

    return render(request, 'users/post_renew.html', {'form': form, 'postinst':post_inst})

@login_required#chech permission to chenges!
def delete_post(request,pk=None):
    post_to_delete=Post.objects.get(pk=pk)
    post_to_delete.delete()
    return redirect(to=request.user.profile.get_absolute_url())

@login_required
def delete_like(request, pk=None):
    try:
        like_to_delete=PostLike.objects.get(pk=pk)
        like_to_delete.delete()
    except: pass
    return render(request, 'users/delete_like.html')



from django.views.generic.edit import CreateView
from django.urls import reverse
class PostLikeCreate(LoginRequiredMixin, CreateView):

    model = PostLike
    fields = []
    def get_context_data(self, **kwargs):
        """
        Add associated post to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(PostLikeCreate, self).get_context_data(**kwargs)
        # Get the post from id and add it to the context
        context['post'] = get_object_or_404(Post, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """
        Add author and associated post to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of likw
        form.instance.user = self.request.user
        #Associate like with post based on passed id
        form.instance.post=get_object_or_404(Post, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(PostLikeCreate, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting like return to associated post.
        """
        next_url = self.request.POST.get('next')
        return next_url+"?"
        #return reverse('post_detail', kwargs={'pk': self.kwargs['pk'],})

class PostCommentCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a post comment. Requires login. 
    """
    model = PostComment
    fields = ['description',]

    def get_context_data(self, **kwargs):
        """
        Add associated post to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        context = super(PostCommentCreate, self).get_context_data(**kwargs)
        # Get the post from id and add it to the context
        context['post'] = get_object_or_404(Post, pk = self.kwargs['pk'])
        return context
        
    def form_valid(self, form):
        """
        Add profile and associated post to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as profile of comment
        form.instance.profile = self.request.user.profile
        #Associate comment with post based on passed id
        form.instance.post=get_object_or_404(Post, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(PostCommentCreate, self).form_valid(form)

    def get_success_url(self): 
        """
        After posting comment return to associated post.
        """
        next_url = self.request.POST.get('next')
        return next_url+"?"
        #return '/Community/'


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def infinite(request):

    paginator = Paginator(range(1, 10), 3)
    try:
        people = paginator.page(request.GET.get('face'))
    except PageNotAnInteger:
        people = paginator.page(1)
    except EmptyPage:
        people = paginator.page(paginator.num_pages)


    paginator = Paginator(range(1, 300), 50)
    try:
        numbers = paginator.page(request.GET.get('page'))
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)


    context = {'numbers': numbers, 'people': people}
    return render(request, 'infinite.html', context)
    
class InfinitePostsView(LoginRequiredMixin, generic.ListView):
    model = Post
    paginate_by = 5
    context_object_name = 'posts'
    template_name = 'infinite_posts.html'

class Community():
    def all(request):
        paginator = Paginator(Profile.objects.order_by('-id').exclude(avatar="users/profile_images/default.jpg"), 10)
        try:
            people = paginator.page(request.GET.get('page'))
        except PageNotAnInteger:
            people = paginator.page(1)
        except EmptyPage:
            people = paginator.page(paginator.num_pages)
        
        paginator = Paginator(Post.objects.all(), 10)
        try:
            posts = paginator.page(request.GET.get('feed'))
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        

        
        context = {'people': people, 'posts': posts}
        return render(request, 'community.html', context)


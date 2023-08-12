from django.contrib.auth.base_user import BaseUserManager
#from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from PIL import Image
from PIL import ImageOps
from django_countries.fields import CountryField
from django.core.validators import RegexValidator


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ["-is_staff"]#"email"

    def __str__(self):
        return self.email
#from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    # Fields
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE) # Delete profile when user is deleted
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    current_position = models.CharField(max_length=255, null=True, blank=True)
    credo = models.CharField(max_length=255, null=True, blank=True)
    country = CountryField(blank_label='(select country)', null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: +987001234567 Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=16, unique = False, null=True, blank=True)
    #phone = PhoneNumberField(null=True, blank=True, unique=False)


    # save avatar with castum name of profile
    def upload_to(instance, filename):
        extension = filename.split('.')[-1]
        og_filename = filename.split('.')[0]
        new_filename = "%s.%s" % ('%s_avatar_%s' %(instance.user.email, og_filename), extension)
        filename=new_filename

        #add path... return 'users/profile_images/%s/%s' % (instance.user.email, filename)
        return 'users/profile_images/%s' % (filename)
    
    def background_img_upload_to(instance, filename):
        extension = filename.split('.')[-1]
        og_filename = filename.split('.')[0]
        new_filename = "%s.%s" % ('%s_background_img%s' %(instance.user.email, og_filename), extension)
        filename=new_filename

        #add path... return 'users/profile_images/%s/%s' % (instance.user.email, filename)
        return 'users/profile_images/%s' % (filename)

    default_avatar = 'users/profile_images/default.jpg'
    avatar = models.ImageField(default=default_avatar, upload_to=upload_to)

    default_background = 'users/profile_images/default_background.jpeg'
    profile_background = models.ImageField(default=default_background, upload_to=background_img_upload_to)
    
    
    # Metadata
    class Meta:
        ordering = ["first_name"]
        
    # Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Profile.
        """
        return reverse('profile_detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Profile object (in Admin site etc.)
        """
        return f'{self.user}' #show how we want it to be displayed
    
    def save(self, *args, **kwargs):
        
        #delete old avatar
        try:
            this = Profile.objects.get(id=self.id)
            if this.avatar != self.avatar and this.avatar != self.default_avatar:
                this.avatar.delete()
            if this.profile_background != self.profile_background and this.profile_background != self.default_background:
                this.profile_background.delete()
        except: pass
        super(Profile, self).save(*args, **kwargs)
        #super().save()
        
        # resizing images
        img = Image.open(self.avatar.path)
        #fix orientation
        img = ImageOps.exif_transpose(img)
        if img.height > 800 or img.width > 800:
            new_img = (800, 800)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
        
        img = Image.open(self.profile_background.path)
        #fix orientation
        img = ImageOps.exif_transpose(img)
        if img.height > 800 or img.width > 800:
            new_img = (800, 800)
            img.thumbnail(new_img)
            img.save(self.profile_background.path)

    def delete(self, *args, **kwargs):
        #delete avatar
        try:
            if self.avatar:
                if self.avatar != self.default_avatar:
                    self.avatar.delete()
        except: pass

        try:
            if self.profile_background:
                if self.profile_background != self.default_background:
                    self.profile_background.delete()
        except: pass
        # delete the CustomUser to
        self.user.delete()
        
        #super(Profile, self).delete(*args, **kwargs)
        super().delete(*args, **kwargs)

class Post(models.Model):
    """Model representing a Post"""
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, help_text="Post title.", blank=True)
    story = models.TextField(max_length=1000, help_text="Write your story...", blank=True)
    # save avatar with castum name of profile
    def upload_to(instance, filename):
        extension = filename.split('.')[-1]
        og_filename = filename.split('.')[0]
        new_filename = "%s.%s" % ('%s_post_%s' %(instance.author, og_filename), extension)
        filename=new_filename

        #add path... return 'users/profile_images/%s/%s' % (instance.user.email, filename)
        return 'users/post_images/%s' % (filename)
    
    picture = models.ImageField(upload_to=upload_to, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    
    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        """Returns the url to access a particular Post."""
        return reverse('post_detail', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the Model object."""
        return self.story
    
    def delete(self, *args, **kwargs):
        #delete picture
        try:
            if self.picture:
                self.picture.delete()
        except: pass
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        #delete old picture
        try:
            this = Post.objects.get(id=self.id)
            if this.picture != self.picture:
                this.picture.delete()
        except: pass
        super(Post, self).save(*args, **kwargs)

        try:
            # resizing images
            img = Image.open(self.picture.path)
            #fix orientation
            img = ImageOps.exif_transpose(img)
            if img.height > 1000 or img.width > 1000:
                new_img = (1000, 1000)
                img.thumbnail(new_img)
                img.save(self.picture.path)
        except: pass

from django.contrib.auth.models import User #Blog author or commenter
class PostLike(models.Model):
    """Model representing a Like"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']

class PostComment(models.Model):
    """Model representing a Comment"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1000, help_text="Add a comment...")

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        len_title=30
        if len(self.description)>len_title:
            titlestring=self.description[:len_title] + '...'
        else:
            titlestring=self.description
        return titlestring

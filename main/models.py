from django.db import models
from PIL import Image


class News(models.Model):
    title = models.CharField('title', max_length=50)
    picture = models.ImageField(upload_to ='uploads/news')
    picture_credit = models.CharField('picture_credit', max_length=50, default='')
    date = models.DateTimeField(auto_now=True)
    description = models.CharField('description', max_length=250)
    preview = models.CharField('preview', max_length=500)
    content = models.TextField('content')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
    
    def save(self, *args, **kwargs):
        #delete old picture
        try:
            this = News.objects.get(id=self.id)
            if this.picture != self.picture:
                this.picture.delete()
        except: pass
        super(News, self).save(*args, **kwargs)
        #super().save()
        
        # resizing images
        img = Image.open(self.picture.path)

        if img.height > 1000 or img.width > 1000:
            new_img = (1000, 1000)
            img.thumbnail(new_img)
            img.save(self.picture.path)
    
    def delete(self, *args, **kwargs):
        #delete old picture
        try:
            if self.picture:
                self.picture.delete()
        except: pass
        super(News, self).delete(*args, **kwargs)
    
class Job(models.Model):
    country= models.CharField('country', max_length=20)
    city = models.CharField('city', max_length=20)
    position = models.CharField('position', max_length=100)
    company_name = models.CharField('company_name', max_length=50)
    picture = models.ImageField(upload_to ='uploads/job')
    address = models.CharField('address', max_length=100)
    date = models.DateTimeField(auto_now=True)
    salary = models.CharField('salary', max_length=50)
    Responsibilities = models.CharField('Responsibilities', max_length=300)
    Qualifications = models.CharField('Qualifications', max_length=400)
    description = models.CharField('description', max_length=500)

    def __str__(self):
        #return self.country
        myTuple = (self.country, self.city, self.company_name)
        x = " -> ".join(myTuple)
        return x

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
    
    def save(self, *args, **kwargs):
        #delete old picture
        try:
            this = Job.objects.get(id=self.id)
            if this.picture != self.picture:
                this.picture.delete()
        except: pass
        super(Job, self).save(*args, **kwargs)
        #super().save()
        
        # resizing images
        img = Image.open(self.picture.path)

        if img.height > 500 or img.width > 500:
            new_img = (500, 500)
            img.thumbnail(new_img)
            img.save(self.picture.path)
    
    def delete(self, *args, **kwargs):
        #delete old picture
        try:
            if self.picture:
                self.picture.delete()
        except: pass
        super(Job, self).delete(*args, **kwargs)

class SushiRoll(models.Model):
    dish_name = models.CharField('dish_name', max_length=50)
    roll_type = models.CharField('roll_type', max_length=30)
    tags = models.CharField('tags', max_length=30)
    country= models.CharField('country', max_length=50)
    city = models.CharField('city', max_length=50)
    restaurant = models.CharField('restaurant', max_length=25)
    picture = models.ImageField(upload_to ='uploads/insider')
    address = models.CharField('address', max_length=100)
    date = models.DateTimeField(auto_now=True)
    price = models.CharField('price', max_length=20)
    sprinkles = models.CharField('sprinkles', max_length=50)
    top = models.CharField('top', max_length=30)
    wrapped = models.CharField('wrapped', max_length=20)
    filling = models.CharField('filling', max_length=100)
    description = models.CharField('description', max_length=500)

    def __str__(self):
        myTuple = (self.restaurant, self.dish_name)
        x = " -> ".join(myTuple)
        return x

    class Meta:
        verbose_name = 'Roll'
        verbose_name_plural = 'Rolls'
    
    
    def save(self, *args, **kwargs):
        #delete old picture
        try:
            this = SushiRoll.objects.get(id=self.id)
            if this.picture != self.picture:
                this.picture.delete()
        except: pass
        super(SushiRoll, self).save(*args, **kwargs)
        #super().save()
        
        # resizing images
        img = Image.open(self.picture.path)

        if img.height > 500 or img.width > 500:
            new_img = (500, 500)
            img.thumbnail(new_img)
            img.save(self.picture.path)
    
    def delete(self, *args, **kwargs):
        #delete old picture
        try:
            if self.picture:
                self.picture.delete()
        except: pass
        super(SushiRoll, self).delete(*args, **kwargs)

class Freelancer(models.Model):
    country= models.CharField('country', max_length=20)
    city = models.CharField('city', max_length=20)
    first_name = models.CharField('first_name', max_length=20)
    last_name = models.CharField('last_name', max_length=20)
    main_position = models.CharField('main_position', max_length=100)
    skills = models.CharField('skills', max_length=500)
    picture = models.ImageField(upload_to ='uploads/freelancer')
    address = models.CharField('address', max_length=100)
    phone = models.CharField('phone', max_length=20)
    date = models.DateTimeField(auto_now=True)
    price = models.CharField('price', max_length=500)
    Qualifications = models.CharField('Qualifications', max_length=400)
    description = models.CharField('description', max_length=500)

    def __str__(self):
        #return self.country
        myTuple = (self.country, self.city, self.first_name, self.main_position)
        x = " -> ".join(myTuple)
        return x

    class Meta:
        verbose_name = 'Freelancer'
        verbose_name_plural = 'Freelancers'

    
    def save(self, *args, **kwargs):
        #delete old picture
        try:
            this = Freelancer.objects.get(id=self.id)
            if this.picture != self.picture:
                this.picture.delete()
        except: pass
        super(Freelancer, self).save(*args, **kwargs)
        #super().save()
        
        # resizing images
        img = Image.open(self.picture.path)

        if img.height > 1000 or img.width > 1000:
            new_img = (1000, 1000)
            img.thumbnail(new_img)
            img.save(self.picture.path)
    
    def delete(self, *args, **kwargs):
        #delete old picture
        try:
            if self.picture:
                self.picture.delete()
        except: pass
        super(Freelancer, self).delete(*args, **kwargs)

class Chef(models.Model):
    country= models.CharField('country', max_length=20)
    city = models.CharField('city', max_length=20)
    first_name = models.CharField('first_name', max_length=20)
    last_name = models.CharField('last_name', max_length=20)
    main_position = models.CharField('main_position', max_length=100)
    status = models.CharField('status', max_length=100)
    skills = models.CharField('skills', max_length=500)
    picture = models.ImageField(upload_to ='uploads/community')
    address = models.CharField('address', max_length=100)
    phone = models.CharField('phone', max_length=20)
    date = models.DateTimeField(auto_now=True)
    workplace = models.CharField('workplace', max_length=100)
    price = models.CharField('price', max_length=500)
    Qualifications = models.CharField('Qualifications', max_length=400)
    description = models.CharField('description', max_length=500)

    def __str__(self):
        #return self.country
        myTuple = (self.country, self.city, self.first_name, self.main_position)
        x = " -> ".join(myTuple)
        return x

    class Meta:
        verbose_name = 'chef'
        verbose_name_plural = 'chefs'

    
    def save(self, *args, **kwargs):
        #delete old picture
        try:
            this = Chef.objects.get(id=self.id)
            if this.picture != self.picture:
                this.picture.delete()
        except: pass
        super(Chef, self).save(*args, **kwargs)
        #super().save()
        
        # resizing images
        img = Image.open(self.picture.path)

        if img.height > 1000 or img.width > 1000:
            new_img = (1000, 1000)
            img.thumbnail(new_img)
            img.save(self.picture.path)
    
    def delete(self, *args, **kwargs):
        #delete old picture
        try:
            if self.picture:
                self.picture.delete()
        except: pass
        super(Chef, self).delete(*args, **kwargs)

class Partner(models.Model):
    name = models.CharField('name', max_length=50)
    title = models.CharField('title', max_length=50)
    picture = models.ImageField(upload_to ='uploads/partner')
    date = models.DateTimeField(auto_now=True)
    description = models.CharField('description', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'
    
    
    def save(self, *args, **kwargs):
        #delete old picture
        try:
            this = Partner.objects.get(id=self.id)
            if this.picture != self.picture:
                this.picture.delete()
        except: pass
        super(Partner, self).save(*args, **kwargs)
        #super().save()
        
        # resizing images
        img = Image.open(self.picture.path)

        if img.height > 500 or img.width > 500:
            new_img = (500, 500)
            img.thumbnail(new_img)
            img.save(self.picture.path)
    
    def delete(self, *args, **kwargs):
        #delete old picture
        try:
            if self.picture:
                self.picture.delete()
        except: pass
        super(Partner, self).delete(*args, **kwargs)
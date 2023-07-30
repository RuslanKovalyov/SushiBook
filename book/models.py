from os import access
from django.db import models
from PIL import Image
from PIL import ImageOps
from django.urls import reverse

class Section(models.Model):#Chapters of book : basics, Sauces, etc.
    name  = models.CharField('Section name',primary_key = True, max_length=20)
    # access = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

class Page(models.Model):
    name  = models.CharField('Page name (url)',primary_key=True, max_length=20)
    #section = models.CharField(max_length=50, blank=True)# external model
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    type = models.CharField(max_length=50, blank=True)# external model
    description = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now=True, blank=True)
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to ='uploads/book/pages/img')
    picture_credit = models.CharField(max_length=50, blank=True, default='')
    #video frame from youtube
    author = models.CharField(max_length=50, blank=True)# models.ForeignKey(Profile, on_delete=models.CASCADE)
    language = models.CharField(max_length=50, blank=True)# external
    warning = models.CharField(max_length=250, blank=True)
    note = models.CharField(max_length=250, blank=True)
    remark = models.CharField(max_length=250, blank=True)
    ingredient_note =models.CharField(max_length=250, blank=True)
    allergens = models.CharField(max_length=250, blank=True)
    introduction = models.CharField(max_length=250, blank=True)
    cooking_time_and_amount = models.CharField(max_length=250, blank=True)
    text_top = models.TextField(blank=True)
    text_bottom = models.TextField(blank=True)
    title_directions_1 = models.CharField(max_length=50, blank=True)
    title_directions_2 = models.CharField(max_length=50, blank=True)
    title_directions_3 = models.CharField(max_length=50, blank=True)
    title_directions_4 = models.CharField(max_length=50, blank=True)
    title_directions_5 = models.CharField(max_length=50, blank=True)
    directions_1 = models.TextField(blank=True)
    directions_2 = models.TextField(blank=True)
    directions_3 = models.TextField(blank=True)
    directions_4 = models.TextField(blank=True)
    directions_5 = models.TextField(blank=True)


    def get_absolute_url(self):
        """Returns the url to access a particular Page."""
        return reverse('page', args=[self.name])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['section', 'type']
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
    
    def save(self, *args, **kwargs):
        #delete old picture
        try:
            this = Page.objects.get(name=self.name)
            if this.picture.path != self.picture.path:
                this.picture.delete()
        except: pass
        super(Page, self).save(*args, **kwargs)
        #super().save()
        
        img = Image.open(self.picture.path)
        #fix orientation
        img = ImageOps.exif_transpose(img)
        # resizing images
        if img.height > 1000 or img.width > 1000:
            new_img = (1000, 1000)
            img.thumbnail(new_img)
            img.save(self.picture.path)
    
    def delete(self, *args, **kwargs):
        #delete picture
        try:
            if self.picture:
                self.picture.delete()
        except: pass
        super(Page, self).delete(*args, **kwargs)

class Product(models.Model):
    name  = models.CharField('Product name',primary_key = True, max_length=250)
    second_name = models.CharField(max_length=50, blank=True)
    note = models.CharField(max_length=50, blank=True)
    type = models.CharField(max_length=50, blank=True)# external model
    picture = models.ImageField(upload_to ='uploads/book/products/img')
    Description = models.CharField(max_length=1000, blank=True)
    link_on_article_page = models.ForeignKey(Page, on_delete=models.PROTECT)
    Nutritional_value = models.CharField(max_length=250, blank=True)
    warning = models.CharField(max_length=500, blank=True)
    Storage_method = models.CharField(max_length=250, blank=True)
    Brand = models.CharField(max_length=50, blank=True)#model
    Supplier = models.CharField(max_length=50, blank=True)#model

    # access = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def save(self, *args, **kwargs):
        #delete old picture
        try:
            this = Product.objects.get(id=self.id)
            if this.picture.path != self.picture.path:
                this.picture.delete()
        except: pass
        super(Product, self).save(*args, **kwargs)
        
        img = Image.open(self.picture.path)
        #fix orientation
        img = ImageOps.exif_transpose(img)
        # resizing images
        if img.height > 1000 or img.width > 1000:
            new_img = (1000, 1000)
            img.thumbnail(new_img)
            img.save(self.picture.path)
    
    def delete(self, *args, **kwargs):
        #delete picture
        try:
            if self.picture:
                self.picture.delete()
        except: pass
        super(Product, self).delete(*args, **kwargs)

class RecipeDetails(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.CharField(max_length=50, blank=True)
    recipe_part = models.CharField(max_length=50, blank=True)# separated ingredients by parts of recipe


    def __str__(self):
        return str(self.product)+' ----> '+str(self.page)

    class Meta:
        ordering = ['page','id']
        verbose_name = 'Ingredients'
        verbose_name_plural = 'Ingredients'

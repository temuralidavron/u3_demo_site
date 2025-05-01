from django.db import models

class DeleteModel(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    is_deleted = models.BooleanField(default=False)

    objects=DeleteModel()
    new=models.Manager()

    class Meta:
        abstract = True

    def delete(self,*args, **kwargs):
        self.is_deleted = True
        self.save(*args,**kwargs)









class Author(BaseModel):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    country = models.CharField(max_length=100)


class Book(BaseModel):
    title = models.CharField(max_length=100)
    authors = models.ForeignKey(Author,on_delete=models.PROTECT,related_name='books',blank=True,null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_year = models.DateField()
    file = models.FileField(upload_to='books/%Y/%m/%d',blank=True,null=True)
    image = models.ImageField(upload_to='image/%Y/%m/%d',blank=True,null=True)


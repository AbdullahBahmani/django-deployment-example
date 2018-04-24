from django.db import models


# Create your models here.




class Authors(models.Model):
    name=models.CharField(max_length=264, unique=True, null=False)
    def __str__(self):
        print (self.name)


class Books(models.Model):
    bookId=models.IntegerField(unique=True, null=False)
    bookName=models.CharField(max_length=264,null=False)
    pageNumbers=models.IntegerField()
    price=models.IntegerField()
    booksAuthor=models.ForeignKey(Authors,on_delete=None)
    def __str__(self):
         print (self.name + "ID :" + self.bookId)

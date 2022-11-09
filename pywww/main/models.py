from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Post(models.Model):
    title = models.CharField(max_length=255)
    # text field with constrains in length
    content = models.TextField()
    # text field without constrains in length
    published = models.BooleanField(default=False)
    # true/false flag
    created = models.DateTimeField(auto_now_add=True)
    # data utworzenia - tylko przy utworzeniu
    modified = models.DateTimeField(auto_now=True)




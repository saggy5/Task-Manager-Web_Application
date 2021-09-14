from django.db import models
from django.contrib.auth.models import User

class TaskModel(models.Model):
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	task_no = models.IntegerField(primary_key=True)
	task = models.TextField()
	time_date = models.DateTimeField(auto_now_add=True)

class user_Todo(models.Model):
	User_Name = models.ForeignKey(TaskModel,on_delete=models.CASCADE)



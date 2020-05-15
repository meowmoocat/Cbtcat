from django.contrib.auth.models import User
from django.db import models


class CbtcatUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    username = models.CharField(max_length=50, unique=True)
    num_times_login = models.IntegerField(
        default=1,
        help_text="Number of times the user has logged in"
    )
    current_level = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.username}"


class L1A(models.Model):
    username = models.CharField(max_length=50, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    finished_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    current_question = models.IntegerField(default=1, editable=True)

    class Meta:
        ordering = ['username', 'created_on']

    def __str__(self):
        return f"finished: {self.finished}, current question: {self.current_question}"


class L2Ans(models.Model):
    username = models.CharField(max_length=50, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    finished_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    current_question = models.IntegerField(default=1, editable=True)

    class Meta:
        ordering = ['username', 'created_on']

    def __str__(self):
        return f"finished: {self.finished}, current question: {self.current_question}"


class L3Ans(models.Model):
    username = models.CharField(max_length=50, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    finished_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    current_question = models.IntegerField(default=1, editable=True)

    class Meta:
        ordering = ['username', 'created_on']

    def __str__(self):
        return f"finished: {self.finished}, current question: {self.current_question}"


class L4Ans(models.Model):
    username = models.CharField(max_length=50, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    finished_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    current_question = models.IntegerField(default=1, editable=True)

    class Meta:
        ordering = ['username', 'created_on']

    def __str__(self):
        return f"finished: {self.finished}, current question: {self.current_question}"


class L5Ans(models.Model):
    username = models.CharField(max_length=50, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    finished_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    current_question = models.IntegerField(default=1, editable=True)

    class Meta:
        ordering = ['username', 'created_on']

    def __str__(self):
        return f"finished: {self.finished}, current question: {self.current_question}"


class L6Ans(models.Model):
    username = models.CharField(max_length=50, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    finished_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    current_question = models.IntegerField(default=1, editable=True)

    class Meta:
        ordering = ['username', 'created_on']

    def __str__(self):
        return f"finished: {self.finished}, current question: {self.current_question}"


class Lvl1UserData(models.Model):
    table_created = models.BooleanField(default=True)
    num_unique_users_started = models.IntegerField(default=0)
    num_unique_users_completed = models.IntegerField(default=0)
    total_times_started = models.IntegerField(default=0)
    total_times_finished = models.IntegerField(default=0)


class Lvl2UserData(models.Model):
    table_created = models.BooleanField(default=True)
    num_unique_users_started = models.IntegerField(default=0)
    num_unique_users_completed = models.IntegerField(default=0)
    total_times_started = models.IntegerField(default=0)
    total_times_finished = models.IntegerField(default=0)


class Lvl3UserData(models.Model):
    table_created = models.BooleanField(default=True)
    num_unique_users_started = models.IntegerField(default=0)
    num_unique_users_completed = models.IntegerField(default=0)
    total_times_started = models.IntegerField(default=0)
    total_times_finished = models.IntegerField(default=0)


class Lvl4UserData(models.Model):
    table_created = models.BooleanField(default=True)
    num_unique_users_started = models.IntegerField(default=0)
    num_unique_users_completed = models.IntegerField(default=0)
    total_times_started = models.IntegerField(default=0)
    total_times_finished = models.IntegerField(default=0)


class Lvl5UserData(models.Model):
    table_created = models.BooleanField(default=True)
    num_unique_users_started = models.IntegerField(default=0)
    num_unique_users_completed = models.IntegerField(default=0)
    total_times_started = models.IntegerField(default=0)
    total_times_finished = models.IntegerField(default=0)


class Lvl6UserData(models.Model):
    table_created = models.BooleanField(default=True)
    num_unique_users_started = models.IntegerField(default=0)
    num_unique_users_completed = models.IntegerField(default=0)
    total_times_started = models.IntegerField(default=0)
    total_times_finished = models.IntegerField(default=0)


class Login(models.Model):
    date_time = models.DateTimeField(auto_now_add=True, null=True)
    username = models.CharField(max_length=50, default="")

    class Meta:
        ordering = ['username']

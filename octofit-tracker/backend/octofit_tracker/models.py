

from djongo import models

# User collection
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100, blank=True, null=True)  # Team name
    leaderboard_score = models.IntegerField(default=0)

    def __str__(self):
        return self.username

# Team collection
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Activity collection
class Activity(models.Model):
    user = models.CharField(max_length=150)  # Username
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    calories = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user} - {self.type}"

# Workout collection
class Workout(models.Model):
    user = models.CharField(max_length=150)  # Username
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user} - {self.date}"

# Leaderboard collection
class Leaderboard(models.Model):
    user = models.CharField(max_length=150)  # Username
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user}: {self.score}"

from django.db import models

# Create your models here.

class team(models.Model):
    team_name = models.CharField(max_length=100,null=True)
    logo = models.ImageField(upload_to='logo/')
    purse_remaining = models.IntegerField(default=1000)
    manager = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    
    def __str__(self):
        return self.team_name

class player(models.Model):
    team = models.ForeignKey(team, on_delete=models.CASCADE, null=True, blank=True, related_name='players')
    name = models.CharField(max_length=100)
    card_image = models.ImageField(upload_to='player_cards/')
    base_price = models.DecimalField(max_digits=10, decimal_places=2, default=20)
    year = models.IntegerField()
    shown = models.BooleanField(default=False)  # Add this line to track if the player has been shown
    def __str__(self):
        return self.name

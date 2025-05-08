from django.db import models

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    #первое значение сохраняется в бд, второе для отображения
    ACCOUNT_STATUS_CHOICES = [
        ('premium', 'Premium'),
        ('standard', 'Standard'),
    ]

    id = models.AutoField(primary_key=True)
    telegram_id = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=100)
    account_status = models.CharField(max_length=10, choices=ACCOUNT_STATUS_CHOICES, default='standard')
    description = models.CharField(max_length=500)
    current_partner_requests = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class PartnerRequest(models.Model):
    PLATFORM_CHOICES = [
        ('PC', 'PC'),
        ('Console', 'Console'),
        ('Mobile', 'Mobile'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    required_players = models.IntegerField()
    description = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    lifetime = models.IntegerField()
    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)

    def __str__(self):
        return f"Request by {self.user.username} for {self.game.name}"

class UserGame(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s game: {self.game.name}"

class UserLog(models.Model):
    LOG_TYPE_CHOICES = [
        ('info', 'Info'),
        ('warning', 'Warning'),
        ('error', 'Error'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    log_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    log_type = models.CharField(max_length=10, choices=LOG_TYPE_CHOICES, default='info')

    def __str__(self):
        return f"Log for {self.user.username} - {self.log_type}"

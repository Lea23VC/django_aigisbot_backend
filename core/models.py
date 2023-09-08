from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)

    class Meta:
        db_table = "regions"

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    password = models.CharField(max_length=255)
    release_date = models.DateField()
    console = models.ForeignKey("Console", on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="games")
    developer = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    players = models.IntegerField()
    availability = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "games"

    def __str__(self):
        return self.name


class Console(models.Model):
    name = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    nasos = models.CharField(max_length=255)
    order_column = models.IntegerField()

    class Meta:
        db_table = "consoles"

    def __str__(self):
        return self.name


class Boxart(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="boxarts")
    image = models.ImageField(upload_to="boxart/")
    image_hash = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()

    class Meta:
        db_table = "boxarts"

    def __str__(self):
        return f"Boxart for {self.game.name}"

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name_actor = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='actor_img/', null=True, blank=True)

    def __str__(self):
        return self.name_actor


class Director(models.Model):
    name_director = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='director_img/', null=True, blank=True)

    def __str__(self):
        return self.name_director


class Genre(models.Model):
    name_genre = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name_genre


class Movie(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    poster = models.ImageField(upload_to='movies_img/', blank=True, null=True)
    year = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    directors = models.ManyToManyField(Director)
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    world_premiere = models.DateField(blank=True, null=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    fees_in_usa = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    fees_in_world = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MovieShot(models.Model):
    title_short = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='shot_img/', blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_short


class Rating(models.Model):
    ip = models.CharField('IP адрес', max_length=15)
    star = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)],
                                default=1, verbose_name="Оценка")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.movie}"


class Review(models.Model):
    email = models.EmailField()
    name_rev = models.CharField(max_length=100)
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name_rev} - {self.movie}"


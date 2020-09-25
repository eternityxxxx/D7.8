from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Author(BaseModel):
    full_name = models.CharField(max_length=128, verbose_name='ФИО')
    birth_year = models.PositiveSmallIntegerField(verbose_name='Год рождения')
    country = models.CharField(max_length=2, verbose_name='Страна')

    def __str__(self):
        return self.full_name


class Publisher(BaseModel):
    name = models.CharField(max_length=128, verbose_name='Название')
    address = models.TextField(verbose_name='Физический адрес')

    def __str__(self):
        return self.name


class Friend(BaseModel):
    full_name = models.CharField(max_length=128, verbose_name='ФИО')
    address = models.TextField(verbose_name='Физический адрес')
    email = models.EmailField(verbose_name='Электронный адрес')

    def __str__(self):
        return self.full_name


class Book(BaseModel):
    ISBN = models.CharField(max_length=13, verbose_name='Международный стандартный книжный номер')
    title = models.CharField(max_length=128, verbose_name='Название книги')
    description = models.TextField(verbose_name='Аннотация')
    year_release = models.PositiveSmallIntegerField(verbose_name='Год издания')
    copy_count = models.PositiveSmallIntegerField(default=1, verbose_name='Число копий в библиотеке')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Цена')
    photo = models.ImageField(upload_to='media/books_photo', blank=True, verbose_name='Фото')

    authors = models.ManyToManyField(
        Author,
        blank=True,
        related_name='book_author',
        verbose_name='Автор'
    )
    publisher = models.ForeignKey(
        Publisher,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='book_publisher',
        verbose_name='Издательство'
    )
    friend = models.ManyToManyField(
        Friend,
        blank=True,
        related_name='book_friend',
        verbose_name='Кто из друзей читает'
    )

    def __str__(self):
        return self.title

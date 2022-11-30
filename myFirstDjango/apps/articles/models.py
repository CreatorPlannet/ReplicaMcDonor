from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField("Название Бургера", max_length=255)
    content = models.TextField("Доп. ингридиенты")
    postDate = models.DateTimeField("Дата добавления нового бургера", default=datetime.now)
    source = models.CharField("Цена", max_length=50)
    image = models.CharField("Ссылка на изображение", max_length=500,blank=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Бургер"
        verbose_name_plural = "Бургеры"

class Juice(models.Model):
    titleT = models.CharField("Название Сока", max_length=255)
    contentT = models.TextField("Доп. ингридиенты")
    postDateT = models.DateTimeField("Дата добавления нового сока", default=datetime.now)
    sourceT = models.CharField("Цена", max_length=50)
    imageJ = models.CharField("Ссылка на изображение", max_length=500,blank=True)


    def __str__(self):
        return self.titleT


    class Meta:
        verbose_name = "Сок"
        verbose_name_plural = "Соки"

class drinkHot(models.Model):
    nameDrink = models.CharField("Название напитка", max_length=255)
    newIngredients = models.TextField("Доп. ингридиенты")
    addDateHot = models.DateTimeField("Дата добавления нового напитка", default=datetime.now)
    priceHot = models.CharField("Цена", max_length=50)
    imageH = models.CharField("Ссылка на изображение", max_length=500,blank=True)

    def __str__(self):
        return self.nameDrink

    class Meta:
        verbose_name = "ГорячийНапиток"
        verbose_name_plural = "ГорячиеНапитки"

class Snack(models.Model):
    nameSnack = models.CharField("Название закуска", max_length=255)
    newSnackIngredients = models.TextField("Доп. ингридиенты")
    addDateSnack = models.DateTimeField("Дата добавления нового закуска", default=datetime.now)
    priceSnack = models.CharField("Цена", max_length=50)
    imageS = models.CharField("Ссылка на изображение", max_length=500,blank=True)

    def __str__(self):
        return self.nameSnack

    class Meta:
        verbose_name = "Закуска"
        verbose_name_plural = "Закуски"
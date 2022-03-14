from django.db import models


class Сomitet(models.Model):
    name = models.CharField("ФИО",  max_length=100)
    position = models.TextField("Должности")
    type = models.CharField("Комитет",  max_length=200)
    country = models.CharField("Страна",  max_length=50)

    # theme = ""
    # format = ""
    # company = ""
    # status = ""
    # email = ""
    # tel = ""
    # city = ""


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Комитет"
        verbose_name_plural = "Комитет"

class Program(models.Model):
    round = models.CharField("Этап", max_length=200)
    data = models.CharField("Дата",  max_length=50)
    position = models.TextField("Описание")

    def __str__(self):
        return self.round

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программа"


class Client(models.Model):
    name = models.CharField("ФИО",  max_length=100)
    position = models.CharField("Ученое звание", max_length=200)
    theme = models.CharField("Тема научного доклада", max_length=200)
    type = models.CharField(verbose_name='Вид образования', max_length=5, choices=(
     ('sec', 'Юридическое лицо'),
     ('high', 'Физическое лицо'),
))
    format = models.CharField(verbose_name='Вид образования', max_length=5, choices=(
     ('f1', 'Очно'),
     ('f2', 'Заочно'),
     ('f3', 'Дистанционно'),
     ('f4', 'Слушатель'),
     ('f5', 'Докладчик'),
))
    company = models.CharField("Организация",  max_length=50)
    status = models.CharField("Должность",  max_length=50)
    email = models.CharField("e-mail",  max_length=50)
    tel = models.CharField("Телефон",  max_length=50)
    city = models.CharField("Город",  max_length=50)
    country = models.CharField("Страна",  max_length=50)
    discription = models.TextField("Описание")
    # files = models.FileField("Файлы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

from django.db import models


class Customer(models.Model):
    tg_id = models.TextField(verbose_name='id телеграмм', blank=False, unique=True)
    tg_first_name = models.TextField(verbose_name='Имя', blank=True)
    tg_last_name = models.TextField(verbose_name='Фамилия', blank=True)
    tg_username = models.TextField(verbose_name='Логин', blank=True)
    comment = models.TextField(verbose_name='Комментарии', blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=11, blank=True)
    product = models.ManyToManyField('Product', blank=True, related_name='products')
    procedure = models.ManyToManyField('Procedure', blank=True, related_name='proceduries')

    def __str__(self):
        return self.tg_id

    def display_product(self):
        return ', '.join([product.title for product in self.product.all()[:]])

    display_product.short_description = 'Продукт'

    def display_procedure(self):
        return ', '.join([procedure.title for procedure in self.procedure.all()[:]])

    display_procedure.short_description = 'Процедура'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class TypeProcedure(models.Model):
    title = models.TextField(verbose_name='Название', blank=False)
    comment = models.TextField(verbose_name='Комментарии', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вид процедуры'
        verbose_name_plural = 'Виды процедур'


class Procedure(models.Model):
    title = models.TextField(verbose_name='Название', blank=False)
    comment = models.TextField(verbose_name='Комментарии', blank=False)
    price = models.CharField(verbose_name='Цена', max_length=15, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    typeprocedure = models.ForeignKey(TypeProcedure, related_name='procedure', blank=False, on_delete=models.CASCADE)

    def display_typeprocedure(self):
        return self.typeprocedure

    display_typeprocedure.short_description = 'Вид процедуры'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Процедура'
        verbose_name_plural = 'Процедуры'


class TypeProduct(models.Model):
    title = models.TextField(verbose_name='Название', blank=False)
    comment = models.TextField(verbose_name='Комментарии', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вид товара'
        verbose_name_plural = 'Виды товаров'


class Product(models.Model):
    title = models.TextField(verbose_name='Название', blank=False)
    comment = models.TextField(verbose_name='Комментарии', blank=False)
    price = models.CharField(verbose_name='Цена', max_length=15, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    typeproduct = models.ForeignKey(TypeProduct, related_name='typeproduct', blank=False, on_delete=models.CASCADE)

    def display_typeproduct(self):
        return self.typeproduct

    display_typeproduct.short_description = 'Вид продукта'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

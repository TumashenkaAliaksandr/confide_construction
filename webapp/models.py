from decimal import Decimal
from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils import timezone


class Services(models.Model):
    """Services model"""
    name = models.CharField(max_length=100, verbose_name='name')
    description = models.TextField(verbose_name='description')
    image = models.ImageField(upload_to='services', verbose_name='photo')
    is_main = models.BooleanField(default=False)
    link = models.URLField()  # Поле для хранения ссылки
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Services"


class ServicesSlider(models.Model):
    """Services slides model"""
    name = models.CharField(max_length=100, verbose_name='name', null=False)
    image = models.ImageField(upload_to='services_slider', verbose_name='photo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Services-Slider"
        verbose_name_plural = "Services-Slider"


class Assessment(models.Model):
    """Assessment Confide for About us"""
    name = models.CharField(max_length=100, verbose_name='name', null=False)
    image = models.ImageField(upload_to='assessment', verbose_name='photo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Individual Assessment"
        verbose_name_plural = "Individual Assessment"


class Recommended(models.Model):
    """Recommended model"""
    name = models.CharField(max_length=100, verbose_name='name')
    image = models.ImageField(upload_to='recommended', verbose_name='photo')
    is_main = models.BooleanField(default=False)
    link = models.URLField()  # Поле для хранения ссылки

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Recommended"
        verbose_name_plural = "Recommended"


class Project(models.Model):
    """Model for projects"""
    title = models.CharField(max_length=100, verbose_name='name')
    description = models.TextField(verbose_name='descriptions')
    image = models.ImageField(upload_to='projects', verbose_name='photo')
    is_main = models.BooleanField(default=False)
    link_project = models.URLField(default='True')  # Поле для хранения ссылки

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Project"


class Callback(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """Категории продуктов"""
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class Subcategory(models.Model):
    """Подкатегории продуктов"""
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subcategories/', blank=True, null=True)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subcategory_detail', kwargs={'slug': self.slug})


class Product(models.Model):
    """Продукты в каталоге"""
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)  # Основное описание продукта
    additional_description = models.TextField(blank=True)  # Дополнительное описание продукта
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)  # Поле для скидки
    invoice_description = models.TextField(blank=True, default='small job description')
    data_created_at = models.DateField(blank=True, null=True)

    # Новые поля
    brand = models.CharField(max_length=100, blank=True)  # Бренд продукта
    capacity = models.CharField(max_length=100, blank=True)  # Вместимость
    color = models.CharField(max_length=50, blank=True)  # Цвет
    material_up = models.CharField(max_length=100, blank=True)  # Верхний материал
    power_source = models.CharField(max_length=100, blank=True)  # Источник питания
    material = models.CharField(max_length=100, blank=True)  # Материал

    # Связь с категориями (несколько категорий для одного продукта)
    categories = models.ManyToManyField(Category, related_name='products', blank=True)

    # Новые поля для флагов
    invoices = models.BooleanField(default=False)
    flag_2 = models.BooleanField(default=False)
    flag_3 = models.BooleanField(default=False)

    show_quantity = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])


class CheckoutDetails(models.Model):
    last_name_check = models.CharField(max_length=100, default='')
    street_address = models.CharField(max_length=255, default='')
    town_city = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=20, default='')
    email = models.EmailField()
    order_notes = models.TextField()
    date = models.DateField()  # Добавляем поле с датой
    price_check = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Используйте DecimalField для цены
    discount_check = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Поле для скидки
    name_check = models.CharField(max_length=255, default='')  # Поле для имени продукта

    # Поля для GenericForeignKey
    product_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    product_object_id = models.PositiveIntegerField(null=True)
    product = GenericForeignKey('product_content_type', 'product_object_id')

    def __str__(self):
        return f"{self.last_name_check}"

    class Meta:
        verbose_name = "Checkout Details"
        verbose_name_plural = "Checkout Details"


# class CheckoutDetails(models.Model):
#     first_name_check = models.CharField(max_length=100)
#     last_name_check = models.CharField(max_length=100)
#     street_address = models.CharField(max_length=255)
#     town_city = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=20)
#     email = models.EmailField()
#     order_notes = models.TextField()
#     date = models.DateField()  # Добавляем поле с датой и временем
#     price_check = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Используйте DecimalField для цены
#
#     # Поля для GenericForeignKey
#     product_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     product_object_id = models.PositiveIntegerField()
#     product = GenericForeignKey('product_content_type', 'product_object_id')
#
#     def __str__(self):
#         return f"{self.first_name_check} {self.last_name_check}"
#
#     class Meta:
#         verbose_name = "Checkout Details"
#         verbose_name_plural = "Checkout Details"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to="media/profile/")
    facebook = models.CharField(max_length=50, null=True, blank=True)
    twitter = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=128, default="Your Password")  # Храните пароли в зашифрованном виде

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


class User_Photo(models.Model):
    user_profile = models.ForeignKey(Profile, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users_photos/', verbose_name='Photo', blank=True, null=True)
    # Другие поля и методы модели Photo

    def __str__(self):
        return f"Photo of {self.user_profile.user.username}"


class Review(models.Model):
    author = models.CharField(max_length=100)  # Имя автора отзыва
    text = models.TextField()  # Текст отзыва
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания отзыва
    rating = models.PositiveIntegerField(default=5)  # Рейтинг отзыва (например, от 1 до 5)
    approved = models.BooleanField(default=False)  # Поле для отметки одобрения отзыва администратором
    photo = models.ImageField(upload_to='review_photos/', null=True, blank=True)  # Фотография, прикрепленная к отзыву

    def __str__(self):
        return self.author  # Возвращает имя автора в административной панели Django

    class Meta:
        ordering = ['-created_at']  # Отсортировать отзывы по дате создания (сначала новые)

        verbose_name = "Review"
        verbose_name_plural = "Review"


class Quality(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fa fa-trophy')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Quality"
        verbose_name_plural = "Quality"


class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ad_images/')
    link = models.URLField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisement"


# class CheckoutSession(models.Model):
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)  # Связь с продуктом
#     session_id = models.CharField(max_length=255)  # ID сессии Stripe
#     created_at = models.DateTimeField(auto_now_add=True)  # Время создания сессии
#
#     def __str__(self):
#         return f"CheckoutSession for {self.product.name} - {self.session_id}"


class CheckoutSession(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)  # Связь с продуктом
    session_id = models.CharField(max_length=255, unique=True)  # Уникальный ID сессии Stripe
    user_email = models.EmailField(max_length=255, null=True)  # Электронная почта пользователя
    last_name_check = models.CharField(max_length=100, null=True)  # Фамилия пользователя
    street_address = models.CharField(max_length=255, null=True)  # Улица и номер дома
    town_city = models.CharField(max_length=100, null=True)  # Город
    phone_number = models.CharField(max_length=15, null=True)  # Номер телефона
    order_notes = models.TextField(blank=True)  # Примечания к заказу
    date = models.DateField(default=timezone.now)  # Дата заказа (с значением по умолчанию)
    price_check = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Цена продукта
    discount_check = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Скидка на продукт
    created_at = models.DateTimeField(auto_now_add=True)  # Время создания сессии

    def __str__(self):
        return f"CheckoutSession for {self.product.name} - {self.session_id}"


class Invoice(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    invoice_link = models.URLField(max_length=200, blank=True, null=True)  # Новое поле для ссылки
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice for {self.client_name} - ${self.amount}"


class Basket(models.Model):  # Переименовали Cart в Basket
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Basket for {self.user.username}"

    def total_price(self):
        return sum(item.total_price() for item in self.basket_items.all())

class BasketItem(models.Model):  # Переименовали CartItem в BasketItem
    basket = models.ForeignKey(Basket, related_name='basket_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


class OrderConsultations(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"File: {self.file.name}"


class Order(models.Model):
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=30)
    zip_code = models.CharField("Почтовый индекс", max_length=10)
    job_description = models.TextField("Описание работы")
    hours_needed = models.IntegerField("Количество часов")
    appointment_date = models.DateField("Дата визита")
    appointment_time = models.TimeField("Время визита")
    email = models.EmailField("Электронная почта")
    phone_number = models.CharField("Телефон", max_length=15)
    photo = models.ImageField("Фото", upload_to='photos/')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.zip_code}"

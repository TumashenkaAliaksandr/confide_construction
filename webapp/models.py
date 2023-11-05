from decimal import Decimal
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


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


class News(models.Model):
    """News Model"""
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    location = models.CharField(max_length=200, verbose_name='Место', default='')
    photo = models.ImageField(upload_to='news_photos/', null=True, blank=True, verbose_name='Фото')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"

    def get_absolute_url(self):
        return reverse('news-datail', kwargs={'pk': self.id})


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


from django.db import models

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Ссылка на пользователя, если есть
    order_number = models.CharField(max_length=20, unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    order_month = models.IntegerField(default=1)  # Поле для хранения месяца

    def save(self, *args, **kwargs):
        # Извлекаем месяц из created_at и сохраняем его в order_month
        self.order_month = self.created_at.month
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.order_number}"


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=20, default='pending')
    payment_date = models.DateTimeField(auto_now=True)

    MONTH_CHOICES = [
        ('01', 'January'),
        ('02', 'February'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    ]

    expiration_date_month = models.CharField(max_length=2, choices=MONTH_CHOICES)
    expiration_date_year = models.PositiveIntegerField()

    cvv = models.CharField(max_length=4)
    card_number = models.CharField(max_length=16)
    owner = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Добавьте другие поля для платежей, если необходимо

    def __str__(self):
        return f"Payment #{self.pk} for Order #{self.order.order_number}"


class Transaction(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    transaction_status = models.CharField(max_length=20)
    transaction_date = models.DateTimeField(auto_now=True)
    # Добавьте другие поля для транзакций, если необходимо

    def __str__(self):
        return f"Transaction #{self.pk} for Payment #{self.payment.pk}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=128)  # Храните пароли в зашифрованном виде

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


class DisposalService(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    advantages = models.TextField(verbose_name='Benefits')
    material = models.CharField(max_length=100, verbose_name='Material')
    photo = models.ImageField(upload_to='disposal_photos/', verbose_name='Photo', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Discount', default=0.00)

    def __str__(self):
        return self.name

    def save_model(self, request, obj, form, change):
        # Если цена была изменена, пересчитываем скидку
        if 'price' in form.changed_data:
            price = form.cleaned_data['price']
            discount = price - Decimal('90.00')  # Вычитаем Decimal объект

            obj.discount = discount

        super().save_model(request, obj, form, change)

    class Meta:
        verbose_name = "Disposal"
        verbose_name_plural = "Disposal"


class Drywall(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    advantages = models.TextField(verbose_name='Benefits')
    material = models.CharField(max_length=100, verbose_name='Material')
    photo = models.ImageField(upload_to='drywall_photos/', verbose_name='Photo', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Discount', default=0.00)

    def __str__(self):
        return self.name

    def save_model(self, request, obj, form, change):
        # Если цена была изменена, пересчитываем скидку
        if 'price' in form.changed_data:
            price = form.cleaned_data['price']
            discount = price - Decimal('90.00')  # Вычитаем Decimal объект

            obj.discount = discount

        super().save_model(request, obj, form, change)

    class Meta:
        verbose_name = "Drywall"
        verbose_name_plural = "Drywall"


from django.db import models

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


class Quality(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
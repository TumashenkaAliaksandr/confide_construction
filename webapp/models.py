from decimal import Decimal
from django.contrib.auth.models import User
from django.db import models


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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
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
    user_profile = models.ForeignKey(UserProfile, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users_photos/', verbose_name='Photo', blank=True, null=True)
    # Другие поля и методы модели Photo

    def __str__(self):
        return f"Photo of {self.user_profile.user.username}"

class Disposal(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    advantages = models.TextField(verbose_name='Benefits')
    material = models.CharField(max_length=350, verbose_name='Material')
    photo = models.ImageField(upload_to='disposal_photos/', verbose_name='Photo', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Discount', default=0.00)

    # Создание поля photos для связи с моделью DisposalPhoto.
    # Множество фотографий может быть связано с одним элементом Disposal.
    photos = models.ManyToManyField('DisposalPhoto', related_name='disposal', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Disposal"
        verbose_name_plural = "Disposal"


# Определение модели DisposalPhoto, которая представляет фотографии для электрооборудования.
class DisposalPhoto(models.Model):
    # Поле для загрузки фотографий, указан путь для сохранения в папке Disposal_photos.
    photo = models.ImageField(upload_to='disposal_photos/', verbose_name='Photo', default=0)

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name = "Photo for Disposal"
        verbose_name_plural = "Photos for Disposal"


class DisposalService(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    photo = models.ImageField(upload_to='disposalservice_photos/', verbose_name='Photo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "DisposalService"
        verbose_name_plural = "DisposalService"


class Drywall(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    advantages = models.TextField(verbose_name='Benefits')
    material = models.CharField(max_length=350, verbose_name='Material')
    photo = models.ImageField(upload_to='drywall_photos/', verbose_name='Photo', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Discount', default=0.00)

    # Создание поля photos для связи с моделью DrywallPhoto.
    # Множество фотографий может быть связано с одним элементом Drywall.
    photos = models.ManyToManyField('DrywallPhoto', related_name='drywall', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Drywall"
        verbose_name_plural = "Drywall"


# Определение модели DrywallPhoto, которая представляет фотографии для электрооборудования.
class DrywallPhoto(models.Model):
    # Поле для загрузки фотографий, указан путь для сохранения в папке Drywall_photos.
    photo = models.ImageField(upload_to='drywall_photos/', verbose_name='Photo', default=0)

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name = "Photo for Drywall"
        verbose_name_plural = "Photos for Drywall"


class DrywallService(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    photo = models.ImageField(upload_to='drywallservice_photos/', verbose_name='Photo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "DrywallService"
        verbose_name_plural = "DrywallService"



class Soundproofing(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    advantages = models.TextField(verbose_name='Benefits')
    material = models.CharField(max_length=350, verbose_name='Material')
    photo = models.ImageField(upload_to='soundproofing_photos/', verbose_name='Photo', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Discount', default=0.00)

    # Создание поля photos для связи с моделью SoundproofingPhoto.
    # Множество фотографий может быть связано с одним элементом Soundproofing.
    photos = models.ManyToManyField('SoundproofingPhoto', related_name='soundproofing', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Soundproofing"
        verbose_name_plural = "Soundproofing"


# Определение модели SoundproofingPhoto, которая представляет фотографии для электрооборудования.
class SoundproofingPhoto(models.Model):
    # Поле для загрузки фотографий, указан путь для сохранения в папке soundproofing_photos.
    photo = models.ImageField(upload_to='soundproofing_photos/', verbose_name='Photo', default=0)

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name = "Photo for Soundproofing"
        verbose_name_plural = "Photos for Soundproofing"


class SoundproofingService(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    photo = models.ImageField(upload_to='soundproofingservice_photos/', verbose_name='Photo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "SoundproofingService"
        verbose_name_plural = "SoundproofingService"



class Wallpaper(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    advantages = models.TextField(verbose_name='Benefits')
    material = models.CharField(max_length=350, verbose_name='Material')
    photo = models.ImageField(upload_to='wallpaper_photos/', verbose_name='Photo', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Discount', default=0.00)

    # Создание поля photos для связи с моделью SoundproofingPhoto.
    # Множество фотографий может быть связано с одним элементом Soundproofing.
    photos = models.ManyToManyField('WallpaperPhoto', related_name='wallpaper', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Wallpaper"
        verbose_name_plural = "Wallpaper"


# Определение модели SoundproofingPhoto, которая представляет фотографии для электрооборудования.
class WallpaperPhoto(models.Model):
    # Поле для загрузки фотографий, указан путь для сохранения в папке soundproofing_photos.
    photo = models.ImageField(upload_to='wallpaper_photos/', verbose_name='Photo', default=0)

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name = "Photo for Wallpaper"
        verbose_name_plural = "Photos for Wallpaper"


class WallpaperService(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    photo = models.ImageField(upload_to='wallpaperservice_photos/', verbose_name='Photo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "WallpaperService"
        verbose_name_plural = "WallpaperService"



class Backsplash(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    advantages = models.TextField(verbose_name='Benefits')
    material = models.CharField(max_length=150, verbose_name='Material')
    photo = models.ImageField(upload_to='soundproofing_photos/', verbose_name='Photo', default=0)
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
        verbose_name = "Backsplash"
        verbose_name_plural = "Backsplash"


class Electrical(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    advantages = models.TextField(verbose_name='Benefits')
    material = models.CharField(max_length=350, verbose_name='Material')
    photo = models.ImageField(upload_to='electrical_photos/', verbose_name='Photo', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Discount', default=0.00)

    # Создание поля photos для связи с моделью ElectricalPhoto.
    # Множество фотографий может быть связано с одним элементом Electrical.
    photos = models.ManyToManyField('ElectricalPhoto', related_name='electricals', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Electrical"
        verbose_name_plural = "Electrical"


# Определение модели ElectricalPhoto, которая представляет фотографии для электрооборудования.
class ElectricalPhoto(models.Model):
    # Поле для загрузки фотографий, указан путь для сохранения в папке soundproofing_photos.
    photo = models.ImageField(upload_to='electrical_photos/', verbose_name='Photo', default=0)

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name = "Photo for Electrical"
        verbose_name_plural = "Photos for Electrical"


class ElectricalService(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    photo = models.ImageField(upload_to='electricalservice_photos/', verbose_name='Photo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ElectricalService"
        verbose_name_plural = "ElectricalService"


class Handyman(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    advantages = models.TextField(verbose_name='Benefits')
    material = models.CharField(max_length=350, verbose_name='Material')
    photo = models.ImageField(upload_to='handyman_photos/', verbose_name='Photo', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Discount', default=0.00)

    # Создание поля photos для связи с моделью HandymanPhoto.
    # Множество фотографий может быть связано с одним элементом Handyman.
    photos = models.ManyToManyField('HandymanPhoto', related_name='handyman', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Handyman"
        verbose_name_plural = "Handyman"


# Определение модели HandymanPhoto, которая представляет фотографии для электрооборудования.
class HandymanPhoto(models.Model):
    # Поле для загрузки фотографий, указан путь для сохранения в папке soundproofing_photos.
    photo = models.ImageField(upload_to='handyman_photos/', verbose_name='Photo', default=0)

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name = "Photo for Handyman"
        verbose_name_plural = "Photos for Handyman"


class HandymanService(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    photo = models.ImageField(upload_to='handymanservice_photos/', verbose_name='Photo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "HandymanService"
        verbose_name_plural = "HandymanService"


class Painting(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    advantages = models.TextField(verbose_name='Benefits')
    material = models.CharField(max_length=350, verbose_name='Material')
    photo = models.ImageField(upload_to='painting_photos/', verbose_name='Photo', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Discount', default=0.00)

    # Создание поля photos для связи с моделью ElectricalPhoto.
    # Множество фотографий может быть связано с одним элементом Electrical.
    photos = models.ManyToManyField('PaintingPhoto', related_name='painting', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Painting"
        verbose_name_plural = "Painting"


# Определение модели ElectricalPhoto, которая представляет фотографии для электрооборудования.
class PaintingPhoto(models.Model):
    # Поле для загрузки фотографий, указан путь для сохранения в папке soundproofing_photos.
    photo = models.ImageField(upload_to='painting_photos/', verbose_name='Photo', default=0)

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name = "Photo for Painting"
        verbose_name_plural = "Photos for Painting"


class PaintingService(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    photo = models.ImageField(upload_to='paintingservice_photos/', verbose_name='Photo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "PaintingService"
        verbose_name_plural = "PaintingService"


class Furniture(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    advantages = models.TextField(verbose_name='Benefits')
    material = models.CharField(max_length=350, verbose_name='Material')
    photo = models.ImageField(upload_to='furniture_photos/', verbose_name='Photo', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Discount', default=0.00)

    # Создание поля photos для связи с моделью ElectricalPhoto.
    # Множество фотографий может быть связано с одним элементом Electrical.
    photos = models.ManyToManyField('FurniturePhoto', related_name='furniture', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Furniture"
        verbose_name_plural = "Furniture"


# Определение модели ElectricalPhoto, которая представляет фотографии для электрооборудования.
class FurniturePhoto(models.Model):
    # Поле для загрузки фотографий, указан путь для сохранения в папке soundproofing_photos.
    photo = models.ImageField(upload_to='furniture_photos/', verbose_name='Photo', default=0)

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name = "Photo for Furniture"
        verbose_name_plural = "Photos for Furniture"


class FurnitureService(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    photo = models.ImageField(upload_to='furnitureservice_photos/', verbose_name='Photo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "FurnitureService"
        verbose_name_plural = "FurnitureService"


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

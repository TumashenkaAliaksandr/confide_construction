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


class Product(models.Model):
    """Продукты в каталоге"""
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)  # Основное описание продукта
    additional_description = models.TextField(blank=True)  # Дополнительное описание продукта
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)  # Поле для скидки

    # Новые поля
    brand = models.CharField(max_length=100, blank=True)  # Бренд продукта
    capacity = models.CharField(max_length=100, blank=True)  # Вместимость
    color = models.CharField(max_length=50, blank=True)  # Цвет
    material_up = models.CharField(max_length=100, blank=True)  # Верхний материал
    power_source = models.CharField(max_length=100, blank=True)  # Источник питания
    material = models.CharField(max_length=100, blank=True)  # Материал

    # Новые поля для флагов
    flag_1 = models.BooleanField(default=False)
    flag_2 = models.BooleanField(default=False)
    flag_3 = models.BooleanField(default=False)

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


class Disposal(models.Model):

    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(default='Description', verbose_name='Description')
    description_installations = models.TextField(default='description_installations', verbose_name='Description installations')
    description_all = models.TextField(default='description all', verbose_name='Description all')
    additional_information = models.TextField(default='Additional Information', verbose_name='Additional Information')
    solution = models.TextField(default='Solution', verbose_name='Solution')
    advantages = models.TextField(verbose_name='Benefits')
    brand = models.CharField(max_length=350, default='Brand', verbose_name='Brand')
    capacity = models.CharField(max_length=350, default='Capacity', verbose_name='Capacity')
    color = models.CharField(max_length=350, default='Color', verbose_name='Color')
    material_up = models.CharField(max_length=350, default='Material Up', verbose_name='Material Up')
    power_source = models.CharField(max_length=350, default='Power Source', verbose_name='Power Source')
    material = models.CharField(max_length=350, verbose_name='Material')
    photo = models.ImageField(upload_to='disposal_photos/', verbose_name='Photo', default=0)
    # photo_two = models.ImageField(upload_to='disposal_photos/', verbose_name='Photo', default=0)
    # photo_three = models.ImageField(upload_to='disposal_photos/', verbose_name='Photo', default=0)
    # photo_four = models.ImageField(upload_to='disposal_photos/', verbose_name='Photo', default=0)
    # photo_five = models.ImageField(upload_to='disposal_photos/', verbose_name='Photo', default=0)
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


class TVMount(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(default='Description', verbose_name='Description')
    description_installations = models.TextField(default='Installation Instructions', verbose_name='Description of Installations')
    description_all = models.TextField(default='Detailed Description', verbose_name='Description All')
    additional_information = models.TextField(default='Additional Information', verbose_name='Additional Information')
    solution = models.TextField(default='Solution', verbose_name='Solution')
    advantages = models.TextField(verbose_name='Benefits')
    brand = models.CharField(max_length=350, default='Brand', verbose_name='Brand')
    color = models.CharField(max_length=350, default='Color', verbose_name='Color')
    material_up = models.CharField(max_length=350, default='Material Up', verbose_name='Material Up')
    power_source = models.CharField(max_length=350, default='Power Source', verbose_name='Power Source')
    material = models.CharField(max_length=350, verbose_name='Material')
    photo = models.ImageField(upload_to='tv_mount_photos/', verbose_name='Photo', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Discount', default=0.00)

    # Создание поля photos для связи с моделью CeilingFanPhoto.
    photos = models.ManyToManyField('TvMountPhoto', related_name='TvMount', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tv Mount"
        verbose_name_plural = "Tv Mount"


# Определение модели TvMountPhoto, которая представляет фотографии для потолочного вентилятора.
class TvMountPhoto(models.Model):
    # Поле для загрузки фотографий, указан путь для сохранения в папке tv mount photos.
    photo = models.ImageField(upload_to='tv_mount_photos/', verbose_name='Photo', default=0)

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name = "Photo for Tv Mount"
        verbose_name_plural = "Photos for Tv Mounts"


class CeilingFan(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(default='Description', verbose_name='Description')
    description_installations = models.TextField(default='Installation Instructions', verbose_name='Description of Installations')
    description_all = models.TextField(default='Detailed Description', verbose_name='Description All')
    additional_information = models.TextField(default='Additional Information', verbose_name='Additional Information')
    solution = models.TextField(default='Solution', verbose_name='Solution')
    advantages = models.TextField(verbose_name='Benefits')
    brand = models.CharField(max_length=350, default='Brand', verbose_name='Brand')
    color = models.CharField(max_length=350, default='Color', verbose_name='Color')
    material_up = models.CharField(max_length=350, default='Material Up', verbose_name='Material Up')
    power_source = models.CharField(max_length=350, default='Power Source', verbose_name='Power Source')
    material = models.CharField(max_length=350, verbose_name='Material')
    photo = models.ImageField(upload_to='ceiling_fan_photos/', verbose_name='Photo', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Discount', default=0.00)

    # Создание поля photos для связи с моделью CeilingFanPhoto.
    photos = models.ManyToManyField('CeilingFanPhoto', related_name='ceiling_fan', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ceiling Fan"
        verbose_name_plural = "Ceiling Fans"


# Определение модели CeilingFanPhoto, которая представляет фотографии для потолочного вентилятора.
class CeilingFanPhoto(models.Model):
    # Поле для загрузки фотографий, указан путь для сохранения в папке ceiling_fan_photos.
    photo = models.ImageField(upload_to='ceiling_fan_photos/', verbose_name='Photo', default=0)

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name = "Photo for Ceiling Fan"
        verbose_name_plural = "Photos for Ceiling Fans"


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
    material = models.CharField(max_length=350, verbose_name='Material')
    photo = models.ImageField(upload_to='backsplash_photos/', verbose_name='Photo', default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Discount', default=0.00)

    # Создание поля photos для связи с моделью DisposalPhoto.
    # Множество фотографий может быть связано с одним элементом Disposal.
    photos = models.ManyToManyField('BacksplashPhoto', related_name='backsplash', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Backsplash"
        verbose_name_plural = "Backsplash"


# Определение модели DisposalPhoto, которая представляет фотографии для электрооборудования.
class BacksplashPhoto(models.Model):
    # Поле для загрузки фотографий, указан путь для сохранения в папке Disposal_photos.
    photo = models.ImageField(upload_to='backsplash_photos/', verbose_name='Photo', default=0)

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name = "Photo for Backsplash"
        verbose_name_plural = "Photos for Backsplash"


class BacksplashService(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    photo = models.ImageField(upload_to='backsplashservice_photos/', verbose_name='Photo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "BacksplashService"
        verbose_name_plural = "BacksplashService"

# class Backsplash(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Name')
#     description = models.TextField(verbose_name='Description')
#     advantages = models.TextField(verbose_name='Benefits')
#     material = models.CharField(max_length=150, verbose_name='Material')
#     photo = models.ImageField(upload_to='soundproofing_photos/', verbose_name='Photo', default=0)
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)
#     discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Discount', default=0.00)
#
#     def __str__(self):
#         return self.name
#
#     def save_model(self, request, obj, form, change):
#         # Если цена была изменена, пересчитываем скидку
#         if 'price' in form.changed_data:
#             price = form.cleaned_data['price']
#             discount = price - Decimal('90.00')  # Вычитаем Decimal объект
#
#             obj.discount = discount
#
#         super().save_model(request, obj, form, change)
#
#     class Meta:
#         verbose_name = "Backsplash"
#         verbose_name_plural = "Backsplash"


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
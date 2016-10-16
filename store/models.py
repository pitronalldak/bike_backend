# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from model_utils import Choices
from my_auth.models import User

TYPE_AVIAILABILIRY = Choices(
    'in_store', 'online', 'private',
    'rent'
)

TYPE_CONDITION = Choices(
    'new', 'used'
)

TYPE_GENDER = Choices(
    'unisex', 'men', 'women'
)

BMX_BIKES_TYPE_WHEEL_SIZE = Choices(
    '12', '14', '16', '18', '20',
    '24', '26', '29'
)

BMX_BIKES_TYPE_TOP_TUBE = Choices(
    '12.5', '14', '15', '16', '16.25', '16.5',
    '16.75', '17', '17.25', '17.5', '17.75',
    '17.9', '18', '18.25', '18.5', '18.75', '19',
    '19.25', '19.5', '19.75', '19.8', '20', '20.25',
    '20.4', '20.5', '20.6', '20.75', '21', '21.25',
    '21.3', '21.5', '21.75', '22', '22.5', '22.75',
    '23.5'
)
BMX_BIKES_TYPE_FRAME_SIZE = Choices(
    'micro_mini', 'mini', 'junior', 'expert', 'pro',
    'pro_xl', 'pro_xxl', 'pro_xxxl'
)

BMX_BIKES_TYPE_MATERIAL = Choices(
    'alloy', 'chromoly', 'steel'
)

BIKES_TYPE_FRAME_SIZE = Choices(
    'xxs', 'xs', 'xs-s', 'small', 's-m', 'medium',
    'm-l', 'large', 'l-xl', 'xl', 'xxl'
)

KIDES_BIKES_TYPE_WHEEL_SIZE = Choices(
    '12', '14', '16', '18', '20', '24', '26',
    '28', 'balance'
)


class ItemManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(is_active=True, approved=True)


class ItemModel(models.Manager):

    objects = ItemManager()

    seller = models.ForeignKey(User)
    availability = models.CharField(
        max_length=100, choices=TYPE_AVIAILABILIRY
    )
    condition = models.CharField(
        max_length=100, choices=TYPE_CONDITION
    )
    gender = models.CharField(
        max_length=100, choices=TYPE_GENDER, null=True
    )
    year = models.IntegerField(default=2016)
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    old_price = models.IntegerField(default=0)
    new_price = models.IntegerField(default=0)
    specification = models.TextField()
    description = models.TextField(null=True)
    views = models.IntegerField(default=0)
    premium = models.BooleanField(default=False)
    main_photo_path = models.ImageField()
    photo_path_2 = models.ImageField()
    photo_path_3 = models.ImageField()
    photo_path_4 = models.ImageField()
    approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
            abstract = True


# freestyle_bmx _bikes
class FreestyleBmxBikes(ItemModel):
    category = models.CharField(default='freestyle_bmx_bike', max_length=100)
    bmx_bikes_type_wheel_size = models.CharField(
        max_length=100, choices=BMX_BIKES_TYPE_WHEEL_SIZE
    )
    bmx_bikes_type_top_tube = models.CharField(
        max_length=100, choices=BMX_BIKES_TYPE_TOP_TUBE
    )
    bmx_bikes_type_frame_size = models.CharField(
        max_length=100, choices=BMX_BIKES_TYPE_FRAME_SIZE
    )
    bmx_bikes_type_material = models.CharField(
        max_length=100, choices=BMX_BIKES_TYPE_MATERIAL
    )


# race_bmx_bikes
class RaceBmxBikes(ItemModel):
    category = models.CharField(default='race_bmx_bikes', max_length=100)
    bmx_bikes_type_wheel_size = models.CharField(
        max_length=100, choices=BMX_BIKES_TYPE_WHEEL_SIZE
    )
    bmx_bikes_type_top_tube = models.CharField(
        max_length=100, choices=BMX_BIKES_TYPE_TOP_TUBE
    )
    bmx_bikes_type_frame_size = models.CharField(
        max_length=100, choices=BMX_BIKES_TYPE_FRAME_SIZE
    )
    bmx_bikes_type_material = models.CharField(
        max_length=100, choices=BMX_BIKES_TYPE_MATERIAL
    )


# classic_and_vintage_bikes
class ClassicAndVintageBikes(ItemModel):
    category = models.CharField(
        default='classic_and_vintage_bikes', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )


# cruiser_bikes
class CruiserBikes(ItemModel):
    category = models.CharField(
        default='cruiser_bikes', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )


# cyclocross_bikes
class CyclocrossBikes(ItemModel):
    category = models.CharField(
        default='cyclocross_bikes', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )


# electric_bikes
class ElectricBikes(ItemModel):
    category = models.CharField(
        default='electric_bikes', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )


# fixie_bikes
class FixieBikes(ItemModel):
    category = models.CharField(
        default='fixie_bikes', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )


# folding_portable_bikes
class FoldingPortableBikes(ItemModel):
    category = models.CharField(
        default='folding_portable_bikes', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )


# hybrid_bikes
class HybridBikes(ItemModel):
    category = models.CharField(
        default='hybrid_bikes', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )


# kids_bikes
class KidsBikes(ItemModel):
    category = models.CharField(
        default='kids_bikes', max_length=100
    )
    kids_bikes_types_wheel_size = models.CharField(
        max_length=100, choices=KIDES_BIKES_TYPE_WHEEL_SIZE
    )


# fat_bikes
class FatBikes(ItemModel):
    category = models.CharField(
        default='fat_bikes', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )


# other_bikes
class OtherBikes(ItemModel):
    category = models.CharField(
        default='other_bikes', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )


# scooter_bikes
class ScootersBikes(ItemModel):
    category = models.CharField(
        default='scooter_bikes', max_length=100
    )


# triathlon_time_trial_bikes
class TriathlonAndTimeTrialBikes(ItemModel):
    category = models.CharField(
        default='triathlon_time_trial_bikes', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )


# urban_bikes
class UrbanBikes(ItemModel):
    category = models.CharField(
        default='urban_bikes', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )


# mtb_27_5_bikes
class MTB275Bikes(ItemModel):
    category = models.CharField(
        default='mtb_27_5_bikes', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )


# mrb_27_5_dual_suspension_bikes
class MTB275DualSuspensionBikes(ItemModel):
    category = models.CharField(
        default='mrb_27_5_dual_suspension_bikes', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )


# mtb_26_bikes
class MTB26Bikes(ItemModel):
    category = models.CharField(
        default='mtb_26_bikes', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )


# mtb_26_dual_suspension_bikes
class MTB26DualSuspensionBikes(ItemModel):
    category = models.CharField(
        default='mtb_26_dual_suspension_bikes', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )


# mtb_29er_bike
class MTB29Bikes(ItemModel):
    category = models.CharField(
        default='mtb_29er_bike', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )


# mtb_29er_dual_suspension_bikes
class MTB29DualSuspensionBikes(ItemModel):
    category = models.CharField(
        default='mtb_29er_dual_suspension_bikes', max_length=100
    )
    bikes_types_frame_size = models.CharField(
        max_length=100, choices=BIKES_TYPE_FRAME_SIZE
    )

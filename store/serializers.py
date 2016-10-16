from rest_framework import serializers

from models import (
    FreestyleBmxBikes, RaceBmxBikes, ClassicAndVintageBikes,
    CruiserBikes, CyclocrossBikes, ElectricBikes,
    FixieBikes, FoldingPortableBikes, HybridBikes, KidsBikes,
    FatBikes, OtherBikes, ScootersBikes, TriathlonAndTimeTrialBikes,
    UrbanBikes, MTB275Bikes, MTB275DualSuspensionBikes, MTB26Bikes,
    MTB26DualSuspensionBikes, MTB29Bikes, MTB29DualSuspensionBikes)
from my_auth.serializers import UserSerializer
from backend.serializers import ActiveModelSerializer
from my_auth.models import User


class SellerSerializer(ActiveModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'city'
        )


class ItemsListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    new_price = serializers.IntegerField()
    old_price = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    seller = SellerSerializer(read_only=True)
    category = serializers.CharField(max_length=100)
    availability = serializers.CharField(max_length=100)


class ItemSerializer(serializers.Serializer):
    seller = UserSerializer(read_only=True)
    date_created = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", read_only=True
    )

    class Meta:

        model = FreestyleBmxBikes
        fields = (
            'id', 'availability', 'brand', 'condition', 'year',
            'title', 'location', 'old_price', 'new_price', 'gender',
            'specification', 'description', 'seller', 'premium',
            'date_created'
        )


class FreestyleBmxBikeSerializer(ItemSerializer):
    class Meta:

        model = FreestyleBmxBikes
        fields = (
            'bmx_bikes_type_wheel_size',
            'bmx_bikes_type_top_tube',
            'bmx_bikes_type_frame_size', 'bmx_bikes_type_material',
        )


class RaceBmxBikeSerializer(ItemSerializer):
    class Meta:

        model = RaceBmxBikes
        fields = (
            'bmx_bikes_type_wheel_size',
            'bmx_bikes_type_top_tube',
            'bmx_bikes_type_frame_size', 'bmx_bikes_type_material',
        )


class ClassicAndVintageBikeSerializer(ItemSerializer):
    class Meta:

        model = ClassicAndVintageBikes
        fields = (
            'bikes_types_frame_size'
        )


class CruiserBikeSerializer(ItemSerializer):
    class Meta:

        model = CruiserBikes
        fields = (
            'bikes_types_frame_size'
        )


class CyclocrossBikeSerializer(ItemSerializer):
    class Meta:

        model = CyclocrossBikes
        fields = (
            'bikes_types_frame_size'
        )


class ElectricBikeSerializer(ItemSerializer):
    class Meta:

        model = ElectricBikes
        fields = (
            'bikes_types_frame_size'
        )


class FixieBikeSerializer(ItemSerializer):
    class Meta:

        model = FixieBikes
        fields = (
            'bikes_types_frame_size'
        )


class FoldingPortableBikeSerializer(ItemSerializer):
    class Meta:

        model = FoldingPortableBikes
        fields = (
            'bikes_types_frame_size'
        )


class HybridBikeSerializer(ItemSerializer):
    class Meta:

        model = HybridBikes
        fields = (
            'bikes_types_frame_size'
        )


class KidsBikeSerializer(ItemSerializer):
    class Meta:

        model = KidsBikes
        fields = (
            'kids_bikes_types_wheel_size'
        )


class FatBikeSerializer(ItemSerializer):
    class Meta:

        model = FatBikes
        fields = (
            'bikes_types_frame_size'
        )


class OtherBikeSerializer(ItemSerializer):
    class Meta:

        model = OtherBikes
        fields = (
            'bikes_types_frame_size'
        )


class ScootersBikeSerializer(ItemSerializer):
    class Meta:

        model = ScootersBikes


class TriathlonAndTimeTrialBikeSerializer(ItemSerializer):
    class Meta:

        model = TriathlonAndTimeTrialBikes
        fields = (
            'bikes_types_frame_size'
        )


class UrbanBikeSerializer(ItemSerializer):
    class Meta:

        model = UrbanBikes
        fields = (
            'bikes_types_frame_size'
        )


class MTB275BikeSerializer(ItemSerializer):
    class Meta:

        model = MTB275Bikes
        fields = (
            'bikes_types_frame_size'
        )


class MTB275DualSuspensionBikeSerializer(ItemSerializer):
    class Meta:

        model = MTB275DualSuspensionBikes
        fields = (
            'bikes_types_frame_size'
        )


class MTB26BikeSerializer(ItemSerializer):
    class Meta:

        model = MTB26Bikes
        fields = (
            'bikes_types_frame_size'
        )


class MTB26DualSuspensionBikeSerializer(ItemSerializer):
    class Meta:

        model = MTB26DualSuspensionBikes
        fields = (
            'bikes_types_frame_size'
        )


class MTB29BikeSerializer(ItemSerializer):
    class Meta:

        model = MTB29Bikes
        fields = (
            'bikes_types_frame_size'
        )


class MTB29DualSuspensionBikeSerializer(ItemSerializer):
    class Meta:

        model = MTB29DualSuspensionBikes
        fields = (
            'bikes_types_frame_size'
        )

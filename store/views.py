from django.http import Http404
from django.db.models import Q
from itertools import chain

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter, SearchFilter

from store.models import (
    FreestyleBmxBikes, RaceBmxBikes, ClassicAndVintageBikes,
    CruiserBikes, CyclocrossBikes, ElectricBikes,
    FixieBikes, FoldingPortableBikes, HybridBikes, KidsBikes,
    FatBikes, OtherBikes, ScootersBikes, TriathlonAndTimeTrialBikes,
    UrbanBikes, MTB275Bikes, MTB275DualSuspensionBikes, MTB26Bikes,
    MTB26DualSuspensionBikes, MTB29Bikes, MTB29DualSuspensionBikes)
from store.serializers import (
    FreestyleBmxBikeSerializer, ItemsListSerializer,
    RaceBmxBikeSerializer, ClassicAndVintageBikeSerializer)


# Create your views here.
class AllItemsView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ItemsListSerializer
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = list(chain(
            FreestyleBmxBikes.objects.active()
        ))
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset


class BikesView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ItemsListSerializer
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    # search_fields = ('brand',)

    def get_queryset(self):
        queryset = list(chain(
            FreestyleBmxBikes.objects.active()
        ))
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset


# FreestyleBmxBike
class FreestyleBmxBikeView(ListAPIView):
    serializer_class = FreestyleBmxBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = FreestyleBmxBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = FreestyleBmxBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            FreestyleBmxBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            freestyle_bmx_bike = FreestyleBmxBikes.objects.get(pk=id)
        except FreestyleBmxBikes.DoesNotExist:
            raise Http404("freestyle_bmx_bike doens't exist")
        freestyle_bmx_bike.is_deleted = True
        freestyle_bmx_bike.save()
        return Response(status=204)


# RaceBmxBike
class RaceBmxBikeView(ListAPIView):
    serializer_class = RaceBmxBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = RaceBmxBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = RaceBmxBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            RaceBmxBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            race_bmx_bike = RaceBmxBikes.objects.get(pk=id)
        except RaceBmxBikes.DoesNotExist:
            raise Http404("freestyle_bmx_bike doens't exist")
        race_bmx_bike.is_deleted = True
        race_bmx_bike.save()
        return Response(status=204)


# ClassicAndVintageBikeView
class ClassicAndVintageBikeView(ListAPIView):
    serializer_class = ClassicAndVintageBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = ClassicAndVintageBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = ClassicAndVintageBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            ClassicAndVintageBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            classic_and_vintage_bike = ClassicAndVintageBikes.objects.get(pk=id)
        except ClassicAndVintageBikes.DoesNotExist:
            raise Http404("classic_and_vintage_bike doens't exist")
        classic_and_vintage_bike.is_deleted = True
        classic_and_vintage_bike.save()
        return Response(status=204)


# CruiserBikeView
class CruiserBikeView(ListAPIView):
    serializer_class = CruiserBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = CruiserBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = CruiserBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            CruiserBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            cruiser_bikes = CruiserBikes.objects.get(pk=id)
        except CruiserBikes.DoesNotExist:
            raise Http404("classic_and_vintage_bike doens't exist")
        cruiser_bikes.is_deleted = True
        cruiser_bikes.save()
        return Response(status=204)


# CyclocrossBikeView
class CyclocrossBikeView(ListAPIView):
    serializer_class = CyclocrossBikeerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = CyclocrossBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = CyclocrossBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            CyclocrossBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            cyclocross_bikes = CyclocrossBikes.objects.get(pk=id)
        except CyclocrossBikes.DoesNotExist:
            raise Http404("classic_and_vintage_bike doens't exist")
        cyclocross_bikes.is_deleted = True
        cyclocross_bikes.save()
        return Response(status=204)


# ElectricBikeView
class ElectricBikeView(ListAPIView):
    serializer_class = ElectricBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = ElectricBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = ElectricBikesSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            ElectricBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            electric_bikes = ElectricBikes.objects.get(pk=id)
        except ElectricBikes.DoesNotExist:
            raise Http404("classic_and_vintage_bike doens't exist")
        electric_bikes.is_deleted = True
        electric_bikes.save()
        return Response(status=204)


# FixieBikeView
class FixieBikeView(ListAPIView):
    serializer_class = FixieBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = FixieBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = FixieBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            FixieBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            fixie_bikes = FixieBikes.objects.get(pk=id)
        except FixieBikes.DoesNotExist:
            raise Http404("classic_and_vintage_bike doens't exist")
        fixie_bikes.is_deleted = True
        fixie_bikes.save()
        return Response(status=204)


# FoldingPortableBikeView
class FoldingPortableBikeView(ListAPIView):
    serializer_class = FoldingPortableBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = FoldingPortableBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = FoldingPortableBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            FoldingPortableBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            folding_portable_bikes = FoldingPortableBikes.objects.get(pk=id)
        except FoldingPortableBikes.DoesNotExist:
            raise Http404("folding_portable_bikes doens't exist")
        folding_portable_bikes.is_deleted = True
        folding_portable_bikes.save()
        return Response(status=204)


# HybridBikeView
class HybridBikeView(ListAPIView):
    serializer_class = HybridBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = HybridBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = HybridBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            HybridBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            hybrid_bikes = HybridBikes.objects.get(pk=id)
        except HybridBikes.DoesNotExist:
            raise Http404("hybrid_bikes doens't exist")
        hybrid_bikes.is_deleted = True
        hybrid_bikes.save()
        return Response(status=204)


# KidsBikeView
class KidsBikeView(ListAPIView):
    serializer_class = KidsBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = KidsBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = KidsBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            HybridBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            kids_bikes = KidsBikes.objects.get(pk=id)
        except KidsBikes.DoesNotExist:
            raise Http404("kids_bikes doens't exist")
        kids_bikes.is_deleted = True
        kids_bikes.save()
        return Response(status=204)


# FatBikeView
class FatBikeView(ListAPIView):
    serializer_class = FatBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = FatBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = FatBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            FatBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            fat_bikes = FatBikes.objects.get(pk=id)
        except FatBikes.DoesNotExist:
            raise Http404("fat_bikes doens't exist")
        fat_bikes.is_deleted = True
        fat_bikes.save()
        return Response(status=204)


# OtherBikeView
class OtherBikeView(ListAPIView):
    serializer_class = OtherBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = OtherBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = OtherBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            OtherBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            other_bikes = OtherBikes.objects.get(pk=id)
        except OtherBikes.DoesNotExist:
            raise Http404("other_bikes doens't exist")
        other_bikes.is_deleted = True
        other_bikes.save()
        return Response(status=204)


# ScootersBikeView
class ScootersBikeView(ListAPIView):
    serializer_class = ScootersBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = ScootersBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = ScootersBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            ScootersBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            scooter_bikes = ScootersBikes.objects.get(pk=id)
        except ScootersBikes.DoesNotExist:
            raise Http404("scooter_bikes doens't exist")
        scooter_bikes.is_deleted = True
        scooter_bikes.save()
        return Response(status=204)


# TriathlonAndTimeTrialBikeView
class TriathlonAndTimeTrialBikeView(ListAPIView):
    serializer_class = TriathlonAndTimeTrialBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = TriathlonAndTimeTrialBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = TriathlonAndTimeTrialBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            TriathlonAndTimeTrialBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            triathlon_time_trial_bikes = TriathlonAndTimeTrialBikes.objects.get(pk=id)
        except TriathlonAndTimeTrialBikes.DoesNotExist:
            raise Http404("triathlon_time_trial_bikes doens't exist")
        triathlon_time_trial_bikes.is_deleted = True
        triathlon_time_trial_bikes.save()
        return Response(status=204)


# UrbanBikeView
class UrbanBikeView(ListAPIView):
    serializer_class = UrbanBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = UrbanBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = UrbanBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            UrbanBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            urban_bikes = UrbanBikes.objects.get(pk=id)
        except UrbanBikes.DoesNotExist:
            raise Http404("urban_bikes doens't exist")
        urban_bikes.is_deleted = True
        urban_bikes.save()
        return Response(status=204)


# MTB275BikeView
class MTB275BikeView(ListAPIView):
    serializer_class = MTB275BikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = MTB275Bikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = MTB275BikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            MTB275Bikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            mtb_27_5_bikes = MTB275Bikes.objects.get(pk=id)
        except MTB275Bikes.DoesNotExist:
            raise Http404("mtb_27_5_bikes doens't exist")
        mtb_27_5_bikes.is_deleted = True
        mtb_27_5_bikes.save()
        return Response(status=204)


# MTB275DualSuspensionBikeView
class MTB275DualSuspensionBikeView(ListAPIView):
    serializer_class = MTB275DualSuspensionBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = MTB275DualSuspensionBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = MTB275DualSuspensionBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            MTB275DualSuspensionBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            mrb_27_5_dual_suspension_bikes = MTB275DualSuspensionBikes.objects.get(pk=id)
        except MTB275DualSuspensionBikes.DoesNotExist:
            raise Http404("mrb_27_5_dual_suspension_bikes doens't exist")
        mrb_27_5_dual_suspension_bikes.is_deleted = True
        mrb_27_5_dual_suspension_bikes.save()
        return Response(status=204)


# MTB26BikeBikeView
class MTB26BikeBikeView(ListAPIView):
    serializer_class = MTB26BikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = MTB26Bikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = MTB26BikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            MTB26Bikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            mtb_26_bikes = MTB26Bikes.objects.get(pk=id)
        except MTB26Bikes.DoesNotExist:
            raise Http404("mtb_26_bikes doens't exist")
        mtb_26_bikes.is_deleted = True
        mtb_26_bikes.save()
        return Response(status=204)


# MTB26DualSuspensionBikeView
class MTB26DualSuspensionBikeView(ListAPIView):
    serializer_class = MTB26DualSuspensionBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = MTB26DualSuspensionBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = MTB26DualSuspensionBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            MTB26DualSuspensionBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            mtb_26_dual_suspension_bikes = MTB26DualSuspensionBikes.objects.get(pk=id)
        except MTB26DualSuspensionBikes.DoesNotExist:
            raise Http404("mtb_26_dual_suspension_bikes doens't exist")
        mtb_26_dual_suspension_bikes.is_deleted = True
        mtb_26_dual_suspension_bikes.save()
        return Response(status=204)


# MTB29BikeView
class MTB29BikeView(ListAPIView):
    serializer_class = MTB29BikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = MTB29Bikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = MTB29BikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            MTB29Bikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            mtb_29er_bike = MTB29Bikes.objects.get(pk=id)
        except MTB29Bikes.DoesNotExist:
            raise Http404("mtb_29er_bike doens't exist")
        mtb_29er_bike.is_deleted = True
        mtb_29er_bike.save()
        return Response(status=204)


# MTB29DualSuspensionBikeView
class MTB29DualSuspensionBikeView(ListAPIView):
    serializer_class = MTB29DualSuspensionBikeSerializer
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    filter_backends = (OrderingFilter, SearchFilter)
    filter_fields = (
        'id', 'availability', 'condition', 'gender'
    )
    search_fields = ('brand',)

    def get_queryset(self):
        queryset = MTB29DualSuspensionBikes.objects.active()
        for filter_field in self.filter_fields:
            value = self.request.query_params.get(filter_field, False)
            if value:
                value_list = value.split(',')
                queryset = queryset.filter(Q(**{'{0}__in'.format(filter_field): value_list}))

        return queryset.distinct()

    def post(self, request, id, format=None):
        json_data = request.data
        serializer = MTB29DualSuspensionBikeSerializer(data=json_data)
        if serializer.is_valid(raise_exception=True):
            MTB29DualSuspensionBikes.objects.update_or_create(seller=request.user, **json_data)
            return Response(status=204)

    def delete(self, request, id, format=None):
        try:
            mtb_29er_dual_suspension_bikes = MTB29DualSuspensionBikes.objects.get(pk=id)
        except MTB29DualSuspensionBikes.DoesNotExist:
            raise Http404("mtb_29er_dual_suspension_bikes doens't exist")
        mtb_29er_dual_suspension_bikes.is_deleted = True
        mtb_29er_dual_suspension_bikes.save()
        return Response(status=204)

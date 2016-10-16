from django.contrib.auth import get_user_model

from backend.serializers import ActiveModelSerializer


class UserSerializer(ActiveModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'email', 'first_name', 'last_name', 'city', 'phone_number',
            'is_admin', 'is_active'
        )

    def create_or_update(self, validated_data):
        def after_func(obj):
            if (validated_data.get('password')):
                obj.set_password(validated_data['password'])
        return super(UserSerializer, self).create_or_update(validated_data, after_func)


class CompanySerializer(ActiveModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id', 'email', 'name', 'url', 'first_name', 'is_company',
            'last_name', 'address', 'phone_number',
            'is_admin', 'is_active'
        )

    def create_or_update(self, validated_data):
        def after_func(obj):
            if (validated_data.get('password')):
                obj.set_password(validated_data['password'])
        return super(CompanySerializer, self).create_or_update(validated_data, after_func)

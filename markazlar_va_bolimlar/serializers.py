from rest_framework import serializers
from markazlar_va_bolimlar.models import Markazlar_bolimlar, Bolimlar_tarix, Rasm, Azolar, Azolarsub


class Markazlar_bolimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Markazlar_bolimlar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'order', 'created_at',
                  'updated_at',)


class Bolimlar_tarixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolimlar_tarix
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'file', 'status', 'center_id', 'order',
                  'created_at', 'updated_at',)


# class TadqiqotSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tadqiqot
#         fields = ('id', 'title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'file',
#         'status', 'center_id', 'order', 'created_at','updated_at',)
#


class AzolarsubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Azolarsub
        fields = ('id', 'title_uz', 'title_en', 'link',)


class AzolarSerializer(serializers.ModelSerializer):
    azolarsub = AzolarsubSerializer(many=True, read_only=True)

    class Meta:
        model = Azolar
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'birth', 'sphere',
                  'center_id', 'position_uz', 'position_en', 'academic_degree_uz', 'academic_degree_en', 'email',
                  'file', 'status', 'order', 'created_at', 'updated_at', 'azolarsub',)


class RasmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rasm
        fields = ('id', 'title_uz', 'title_en', 'content_uz', 'content_en', 'image', 'center_id', 'file', 'status',
                  'order', 'created_at', 'updated_at',)

# class VideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Video
#         fields = ('id', 'title_uz', 'title_ru', 'title_en', 'content_uz', 'content_ru', 'content_en', 'link', 'file',
#         'center_id', 'status', 'order', 'created_at',
#                   'updated_at',)

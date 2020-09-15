from rest_framework import serializers
from works.models import Works, Description, Tags, ProgLang


# class ProgLangSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProgLang
#         fields = ('name', )

class ProgLangName(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class WorksSerializer(serializers.ModelSerializer):
    # prog_lang = serializers.SlugRelatedField(
    #     read_only=True, slug_field='name'
    # )
    prog_lang = serializers.StringRelatedField(many=True, read_only=True)
    # prog_lang = ProgLangName(many=True, read_only=True)
    tags = serializers.StringRelatedField(many=True, read_only=True)
    description = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Works
        # fields = '__all__'
        fields = ('name', 'image', 'prog_lang',
                  'work_type', 'description', 'tags', 'added_on',)


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ('description, menu')

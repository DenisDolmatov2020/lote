from rest_framework import serializers
from rules.models import TypeRule, Rule


class TypeRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeRule
        fields = ['title']


class RuleSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Rule
        fields = ['id', 'type', 'title', 'text']

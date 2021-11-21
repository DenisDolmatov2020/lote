from rest_framework.generics import ListAPIView
from rules.models import Rule
from rules.serializers import RuleSerializer


class RulesListView(ListAPIView):
    serializer_class = RuleSerializer
    queryset = Rule.objects.all()

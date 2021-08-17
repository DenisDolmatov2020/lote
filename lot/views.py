from rest_framework import status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.viewsets import ViewSet
# from lottee_new.permissions import ReadOnly
from lot.models import Lot, Condition
from lot.serializers import LotSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from number.models import Number


class LotViewSet(ViewSet):
    parser_classes = (MultiPartParser, FormParser, JSONParser, FileUploadParser)
    file_content_parser_classes = (JSONParser, FileUploadParser)
    permission_classes = [AllowAny]
    queryset = Lot.objects.all()
    serializer = LotSerializer

    def list(self, request, *args):
        lots = Lot.objects.filter(active=True)
        serializer = self.serializer(lots, many=True)
        print('LIST')
        print(lots)
        print(serializer.data)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args):
        lot = get_object_or_404(self.queryset, pk=pk)
        if lot.active:
            lot.conditions = Condition.objects.filter(lot_id=lot.id)
            lot.free_numbers = Number.objects.filter(lot_id=lot.id, user=None).count()
        else:
            lot.wins = Number.objects.filter(lot_id=lot.id, won=True)
        serializer = self.serializer(lot)
        return Response(serializer.data)

    @staticmethod
    def create(request, *args):
        conditions = request.data.get('conditions')
        data_ = request.data.dict()
        data_['conditions'] = json.loads(conditions)
        data_['user_id'] = request.user.id
        serializer = LotSerializer(data=data_)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

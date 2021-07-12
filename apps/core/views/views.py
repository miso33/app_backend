from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions

from .tracking import TrackingView
from ..paginations import BasePagination
from rest_framework.generics import ListAPIView, RetrieveAPIView


class BaseView(TrackingView):
    pagination_class = BasePagination
    permission_classes = (DjangoModelPermissions,)


class BaseViewSet(BaseView, ModelViewSet):
    pass


class BaseListView(BaseView, ListAPIView):
    pass


class BaseRetrieveView(BaseView, RetrieveAPIView):
    pass

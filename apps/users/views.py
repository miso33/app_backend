from django.contrib.auth import get_user_model

from apps.core.permissions import ViewDjangoModelPermission
from apps.core.views import BaseViewSet
from .filters import UserFilter
from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(BaseViewSet):
    filter_class = UserFilter
    queryset = User.objects.filter()
    permission_classes = (ViewDjangoModelPermission,)
    serializer_class = UserSerializer

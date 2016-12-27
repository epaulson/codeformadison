from graphene import relay, ObjectType, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Profile, BusStop

class ProfileNode(DjangoObjectType):
  class Meta:
    model = Profile
    filter_fields = ['user', 'address']
    interfaces = (relay.Node,)


class BusStopNode(DjangoObjectType):
  class Meta:
    model = BusStop
    filter_fields = ['name', 'id']
    interfaces = (relay.Node,)


class Query(AbstractType):
    profile = relay.Node.Field(ProfileNode)
    all_profiles = DjangoFilterConnectionField(ProfileNode)

    busstop = relay.Node.Field(BusStopNode)
    all_busstops = DjangoFilterConnectionField(BusStopNode)

    def resolve_all_busstops(self, args, context, info):
      print(context.user)
      if not context.user.is_authenticated():
        return BusStop.objects.none()
      else:
        return BusStop.objects.filter(owner=context.user.profile)



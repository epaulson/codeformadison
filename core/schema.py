from graphene import relay, ObjectType, AbstractType, String
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import datetime

from .models import Profile, BusStop

class ProfileNode(DjangoObjectType):
  nextpickupdate = String()
  class Meta:
    model = Profile
    filter_fields = ['user', 'address']
    interfaces = (relay.Node,)

  def resolve_nextpickupdate(self, args, context, info):
    matched = next(x for x in schedules[context.user.profile.trashpickup]  if x[0]>=datetime.date.today())
    return("The next pickup is %s and it is a trash and %s pickup day" % (matched[0].strftime("%A %B %-d"), matched[1])) 

class BusStopNode(DjangoObjectType):
  class Meta:
    model = BusStop
    filter_fields = ['name', 'id']
    interfaces = (relay.Node,)


class Query(AbstractType):
    #profile = relay.Node.Field(ProfileNode)
    all_profiles = DjangoFilterConnectionField(ProfileNode)

    #busstop = relay.Node.Field(BusStopNode)
    all_busstops = DjangoFilterConnectionField(BusStopNode)

    def resolve_all_busstops(self, args, context, info):
      print(context.user)
      if not context.user.is_authenticated():
        return BusStop.objects.none()
      else:
        return BusStop.objects.filter(owner=context.user.profile)

    def resolve_all_profiles(self, args, context, info):
      print(context.user)
      if not context.user.is_authenticated():
        return Profile.objects.none()
      else:
        return Profile.objects.filter(user=context.user)


schedules = { 'http://www.cityofmadison.com/streets/documents/wedA.pdf': [(datetime.date(2017, 1, 4), 'Recycle'),
 (datetime.date(2017, 1, 11), 'Large Item'),
 (datetime.date(2017, 1, 18), 'Recycle'),
 (datetime.date(2017, 1, 25), 'Large Item'),
 (datetime.date(2017, 2, 1), 'Recycle'),
 (datetime.date(2017, 2, 8), 'Large Item'),
 (datetime.date(2017, 2, 15), 'Recycle'),
 (datetime.date(2017, 2, 22), 'Large Item'),
 (datetime.date(2017, 3, 1), 'Recycle'),
 (datetime.date(2017, 3, 8), 'Large Item'),
 (datetime.date(2017, 3, 15), 'Recycle'),
 (datetime.date(2017, 3, 22), 'Large Item'),
 (datetime.date(2017, 3, 29), 'Recycle'),
 (datetime.date(2017, 4, 5), 'Large Item'),
 (datetime.date(2017, 4, 12), 'Recycle'),
 (datetime.date(2017, 4, 19), 'Large Item'),
 (datetime.date(2017, 4, 26), 'Recycle'),
 (datetime.date(2017, 5, 3), 'Large Item'),
 (datetime.date(2017, 5, 10), 'Recycle'),
 (datetime.date(2017, 5, 17), 'Large Item'),
 (datetime.date(2017, 5, 24), 'Recycle'),
 (datetime.date(2017, 5, 31), 'Large Item'),
 (datetime.date(2017, 6, 7), 'Recycle'),
 (datetime.date(2017, 6, 14), 'Large Item'),
 (datetime.date(2017, 6, 21), 'Recycle'),
 (datetime.date(2017, 6, 28), 'Large Item'),
 (datetime.date(2017, 7, 5), 'Recycle'),
 (datetime.date(2017, 7, 12), 'Large Item'),
 (datetime.date(2017, 7, 19), 'Recycle'),
 (datetime.date(2017, 7, 26), 'Large Item'),
 (datetime.date(2017, 8, 2), 'Recycle'),
 (datetime.date(2017, 8, 9), 'Large Item'),
 (datetime.date(2017, 8, 16), 'Recycle'),
 (datetime.date(2017, 8, 23), 'Large Item'),
 (datetime.date(2017, 8, 30), 'Recycle'),
 (datetime.date(2017, 9, 6), 'Large Item'),
 (datetime.date(2017, 9, 13), 'Recycle'),
 (datetime.date(2017, 9, 20), 'Large Item'),
 (datetime.date(2017, 9, 27), 'Recycle'),
 (datetime.date(2017, 10, 4), 'Large Item'),
 (datetime.date(2017, 10, 11), 'Recycle'),
 (datetime.date(2017, 10, 18), 'Large Item'),
 (datetime.date(2017, 10, 25), 'Recycle'),
 (datetime.date(2017, 11, 1), 'Large Item'),
 (datetime.date(2017, 11, 8), 'Recycle'),
 (datetime.date(2017, 11, 15), 'Large Item'),
 (datetime.date(2017, 11, 22), 'Recycle'),
 (datetime.date(2017, 11, 29), 'Large Item'),
 (datetime.date(2017, 12, 6), 'Recycle'),
 (datetime.date(2017, 12, 13), 'Large Item'),
 (datetime.date(2017, 12, 20), 'Recycle'),
 (datetime.date(2017, 12, 27), 'Large Item')]}

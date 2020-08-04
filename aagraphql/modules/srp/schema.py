import graphene

from graphene_django.types import DjangoObjectType

from allianceauth.srp.models import SrpFleetMain, SrpUserRequest


class SRPFleetType(DjangoObjectType):
    class Meta:
        model = SrpFleetMain


class SRPUserRequestType(DjangoObjectType):
    class Meta:
        model = SrpUserRequest


class Query(object):
    fleets = graphene.List(SRPFleetType)
    fleet_requests = graphene.List(SRPUserRequestType, fleet_id=graphene.Int())

    def resolve_fleets(self, info, **kwargs):
        return SrpFleetMain.objects.all()

    def resolve_fleet_requests(self, info, **kwargs):
        fleet_id = kwargs.get('fleet_id')
        if fleet_id is not None:
            fleet_main = SrpFleetMain.objects.get(id=fleet_id)
            return fleet_main.srpuserrequest_set.select_related(
                'character').order_by('srp_ship_name')
        return None

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
    requests = graphene.List(SRPUserRequestType)

    def resolve_fleets(self, info, **kwargs):
        return SrpFleetMain.objects.all()

    def resolve_user_requests(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return SrpUserRequest.objects.all()

import logging

from bravado.exception import HTTPError
from celery import shared_task

from allianceauth.eveonline import providers

from allianceauth.eveonline.models import EveAllianceInfo
from allianceauth.eveonline.models import EveCharacter
from allianceauth.eveonline.models import EveCorporationInfo

from allianceauth.eveonline.tasks import update_alliance, update_character, update_corp

logger = logging.getLogger(__name__)


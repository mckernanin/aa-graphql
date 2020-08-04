from django.conf import settings


def fleets_active():
    return 'allianceauth.optimer' in settings.INSTALLED_APPS


def timers_active():
    return 'allianceauth.timerboard' in settings.INSTALLED_APPS


def hr_active():
    return 'allianceauth.hrapplications' in settings.INSTALLED_APPS


def srp_active():
    return 'allianceauth.srp' in settings.INSTALLED_APPS

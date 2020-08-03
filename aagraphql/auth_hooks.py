from . import urls
from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook
from allianceauth.authentication.models import UserProfile, State

 
class GqlMenu(MenuItemHook):
    def __init__(self):
        MenuItemHook.__init__(self, 'GraphQL',
                              'fa fa-empire fa-fw',
                              'graphql:graphql',
                              navactive=['graphql:graphql'])

    def render(self, request):
        return MenuItemHook.render(self, request)


@hooks.register('menu_item_hook')
def register_menu():
    return GqlMenu()


@hooks.register('url_hook')
def register_url():
    return UrlHook(urls, 'graphql', r'^graphql/')


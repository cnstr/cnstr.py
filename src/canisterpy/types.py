'''Defines all canister.py types (package, repo, etc).'''
# types.py

# imports
from typing import Optional


# package object
class Package(object):
    '''
    Canister package object.
    '''
    def __init__(self, data: dict[str, str]):
        # identifier of package
        self.identifier: str = data.get('identifier')
        # depiction header
        self.header: Optional[str] = data.get('header')
        # depiction tint color
        self.tint_color: Optional[str] = data.get('tintColor')
        # name of package
        self.name: Optional[str] = data.get('name')
        # price of package
        self.price: str = data.get('price')
        # description of package
        self.description: str = data.get('description')
        # section of package
        self.section: str = data.get('section')
        # maintainer of package
        self.maintainer: str = data.get('maintainer')
        # author of package
        self.author: Optional[str] = data.get('author')
        # depiction of package
        self.depiction: Optional[str] = data.get('depiction')
        # version of package
        self.version: str = data.get('latestVersion')
        # native depiction of package
        self.native_depiction: Optional[str] = data.get('nativeDepiction')
        # icon of package
        self.icon_url: Optional[str] = data.get('packageIcon')
        # repository
        self.repository: dict = {'uri': data.get('repository').get('uri'), 'name': data.get('repository').get('name')}


# repo object
class Repo(object):
    '''
    Canister repo object.
    '''
    def __init__(self, data: dict[str, str]):
        # repo slug
        self.slug: str = data.get('slug')
        # repo aliases
        self.aliases: list = data.get('aliases')
        # repo uri
        self.uri: str = data.get('uri')
        # repo dist
        self.dist: Optional[str] = data.get('dist')
        # repo version
        self.version: float = data.get('version')
        # repo suite
        self.suite: Optional[str] = data.get('suite')
        # repo name
        self.name: str = data.get('name')
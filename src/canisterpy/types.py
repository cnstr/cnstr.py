from __future__ import annotations
'''Defines all canister.py types (package, repo, etc).'''
# types.py

# imports
from .errors import InvalidFieldError
from datetime import datetime
from typing import Optional

# fields
class Fields(object):
    def __init__(self, map):
        self.__map = map
    
    def all_true(self) -> PackageSearchFields:
        '''Sets all fields to true.'''
        for m in self.__map.keys():
            self.__map[m] = True
        return self

    def set(self, key: str, value: bool) -> PackageSearchFields:
        '''Set a field value.
        Args:
            key (str): Key to set.
            value (bool): Value to set key to.
        Returns:
            SearchFields: Updated class object.
        '''
        if key.lower() not in self.__map.keys():
            InvalidFieldError('Invalid field {} provided.'.format(key))
        self.__map[key.lower()] = value
        return self
    
    @property
    def __string__(self):
        final = ''
        for key in self.__map.keys():
            if self.__map[key] is True:
                final += (key + ',')
        return (final[::-1].replace(','[::1], ''[::-1], 1))[::-1]

# package search fields
class PackageSearchFields(Fields):
    '''
    Fields to search for packages with.
    '''
    def __init__(self):
        super().__init__(map={
            'name': False,
            'author': False,
            'maintainer': False,
            'description': False,
            'identifier': False
        })

# repository search fields
class RepositorySearchFields(Fields):
    '''
    Fields to search for repositories with.
    '''
    def __init__(self):
        super().__init__(map={
            'slug': False,
            'uri': False,
            'aliases': False,
            'name': False,
            'description': False
        })

# package object
class Package(object):
    '''
    Canister package object.
    '''
    def __init__(self, data: dict[str, str]):
        # start time
        start = datetime.now().timestamp()
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
        self.repository: dict = {
            'uri': data.get('repository').get('uri'),
            'name': data.get('repository').get('name')
        }
        # end time
        self.__time__ = datetime.now().timestamp() - start

# repo object
class Repo(object):
    '''
    Canister repo object.
    '''
    def __init__(self, data: dict[str, str]):
        # start time
        start = datetime.now().timestamp()
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
        # end time
        self.__time__ = datetime.now().timestamp() - start
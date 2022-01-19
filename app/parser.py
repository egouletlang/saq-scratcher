# [Native]
from enum import Enum
import re

from bs4 import BeautifulSoup

class Property(Enum):
    SPAN = 1
    TEXT = 2

class Sanitize:

    @classmethod
    def utf8(cls, target):
        return target.replace('\\u00e9', 'é') if target else None

    @classmethod
    def get_integer(cls, target):
        match = re.search(r'(\d+)', target) if target else None
        return match.group(1) if match else None

class BaseParser:

    def _safe_find(
        self,
        soup, 
        instructions, 
        property=Property.SPAN, 
        default=None,
        debug=False
    ):
        for (elem_type, characteristics) in instructions:
            if debug:
                print(f'[soup == {soup != None}]looking for {elem_type} with {characteristics}')
            if characteristics:
                soup = soup.find(elem_type, characteristics) if soup else None
            else:
                soup = soup.find(elem_type) if soup else None

        if property == Property.TEXT:
            return soup.text if soup else default
        return soup

class SaqParser(BaseParser):

    def __get_online_availability(self, soup):
        count = self._safe_find(
            soup=soup,
            instructions=[
                ('span', {'class' : 'product-online-availability'}),
                ('span', None)
            ],
            property=Property.TEXT
        )
        count = Sanitize.get_integer(count)

        return {
            'count': count
        }

    def __get_store_availability(self, soup):
        store_type = self._safe_find(
            soup=soup,
            instructions=[
                ('div', {'class': 'store-list-item-header'}),
                ('div', {'class': 'store-banner'})
            ],
            property=Property.TEXT
        )
        store_type = Sanitize.utf8(store_type)

        store_id = self._safe_find(
            soup=soup,
            instructions=[
                ('div', {'class': 'store-list-item-header'}),
                ('span', {'class': 'id-store'})
            ],
            property=Property.TEXT
        )
        store_id = Sanitize.utf8(store_id)

        distance = self._safe_find(
            soup=soup,
            instructions=[
                ('div', {'class': 'store-list-item-header'}),
                ('span', {'class': 'distance'})
            ],
            property=Property.TEXT
        )
        distance = Sanitize.utf8(distance)

        name = self._safe_find(
            soup=soup,
            instructions=[
                ('div', {'class': 'store-list-item-header'}),
                ('div', {'class': 'name'}),
                ('h4', None)
            ],
            property=Property.TEXT
        )
        name = Sanitize.utf8(name)

        quantity = self._safe_find(
            soup=soup,
            instructions=[
                ('div', {'class': 'more-details'}),
                ('div', {'class': 'disponibility'})
            ],
            property=Property.TEXT
        )
        quantity = Sanitize.get_integer(quantity)

        return {
            'store_type': store_type,
            'store_id': store_id,
            'distance': distance,
            'store_name': name,
            'quantity': quantity
        }

    def __get_stores_availability(self, soup):
        store_listings = soup.find_all('li', {'class' : 'store-list-item'})
        return [self.__get_store_availability(store) for store in store_listings]

    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return {
            'online': self.__get_online_availability(soup),
            'in-store': self.__get_stores_availability(soup)
        }

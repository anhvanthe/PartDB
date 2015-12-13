import Distributors.__Distributor
import re
import copy


class Farnell(Distributors.__Distributor.Distributor):

    def __init__(self, partDB):
        super().__init__(partDB)

    def matchPartNumber(self, data):
        matches = re.search(
            '^(?P<distributorPartNumber>\d{7})$', data)
        if matches:
            result = copy.copy(matches.groupdict())
            return result
        else:
            return None

    def matchBarcode(self, data):
        return None

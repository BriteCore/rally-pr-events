import os

from pyral import Rally
from pyral.restapi import RallyRESTAPIError

class RallyBase:
    def __init__(self, API_KEY):
        self.rally = Rally(apikey=API_KEY)

    def get_rally_item(self, item_id, item_type):
        try:
            return self.rally.get(item_type, fetch=True, instance=True, projectScopeDown=True, query=f'FormattedID = {item_id}')
        except RallyRESTAPIError:
            raise RallyLookupFailure('Failed to find the Story/Defect in Rally')

    def update_item(self, item, item_data):
        try:
            return self.rally.update(item._type,
                                fetch=True,
                                instance=True,
                                itemData=item_data)
        except RallyRESTAPIError:
            raise RallyLookupFailure('Failed to find the Story/Defect in Rally')


def parse_key_value(values):
    pairs = values.split('::')
    result = dict()
    if len(pairs):
        for pair in pairs:
            item = pair.split(":")
            if len(item) == 2:
                result[item[0]] = item[1]
    return result


def main():
	# Get Env variables
    item_id = os.getenv('INPUT_ITEM_ID')
    item_type = os.getenv('INPUT_ITEM_TYPE')
    values = os.getenv('INPUT_VALUES')
    API_KEY = os.getenv('INPUT_RALLY_API_KEY')

    # Instantiate Rally Instance
    rally = RallyBase(API_KEY)
    response = rally.get_rally_item(item_id, item_type)
    parsed_values = parse_key_value(values)

    item_data = {
        'ObjectID': response.ObjectID,
        'FormattedID': response.FormattedID,
        **parsed_values
    }

    # Update Rally Item
    rally.update_item(response, item_data)	


if __name__ == '__main__':
    main()

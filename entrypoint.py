#!/usr/local/bin/python

import os

from pyral import Rally

class RallyBase:
    def __init__(self, API_KEY):
        self.rally = Rally(apikey=API_KEY)

    def get_rally_item(self, item_id, item_type):
        return self.rally.get(item_type, fetch=True, instance=True, projectScopeDown=True, query=f'FormattedID = {item_id}')

    def update_item(self, item, item_data):
        return self.rally.update(item._type,
                            fetch=True,
                            instance=True,
                            itemData=item_data)


    def get_flow_states(self, project_name):
        return self.rally.get('FlowState',
                        project=project_name)

    def get_flow_state(self, project_name, state_name):
        flow_states = self.get_flow_states(project_name)
        found = None
        for flow_state in flow_states:
            if flow_state.Name == state_name:
                return flow_state
        raise LookupError(f'Could not find desired Flow State: {state_name}')

    def normalize_data(self, item, item_data):
        if item_data.get('FlowStateName'):
            project_name = item.Project.Name
            state_name = item_data.pop('FlowStateName')
            flow_state = self.get_flow_state(project_name, state_name)
            item_data['FlowState'] = flow_state.oid
        return item_data


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
    values = os.getenv('INPUT_KEY_VALUES')
    API_KEY = os.getenv('INPUT_RALLY_API_KEY')

    # Instantiate Rally Instance
    rally = RallyBase(API_KEY)
    response = rally.get_rally_item(item_id, item_type)
    parsed_values = parse_key_value(values)

    item_data = rally.normalize_data(response, {
        'ObjectID': response.ObjectID,
        'FormattedID': response.FormattedID,
        **parsed_values
    })

    # Update Rally Item
    rally.update_item(response, item_data)	


if __name__ == '__main__':
    main()

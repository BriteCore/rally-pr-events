# GitHub Action for Updating Rally items
An action that helps with updating [Rally](https://rally1.rallydev.com/) items on PR Events built by IntuitiveWebSolution's team!

## Usage

One usage of updating Rally fields when a PR is merged

```.yaml
name: 'Update Rally Field'

on:
  pull_request:
    types: [ closed ]

jobs:
  rally-update-field:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v2
    - name: Update Rally
      if: github.event.pull_request.merged == true
      uses: IntuitiveWebSolutions/rally-pr-events@master
      with:
        rally_api_key: "APIKey"
        item_type: "ItemType"
        item_id: "ItemID"
        key_values: 'RallyKey:RallyValue::AnotherKey:AnotherValue'
```

## Inputs

* `key_values`: String to parse KeyValue pairs **Required**
* `item_id`: Rally's Formatted ID. **Required**
* `item_type`: Rally's record type **Required**
* `rally_api_key`: API Key **Required**

## Contributions

All contributions are welcome !

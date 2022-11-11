import requests
import json
import numpy as np
import pandas as pd


class LiveData:
    def __init__(self):
        self.results_df = None

        self.get_data_using_api()
        self.remove_duplicate_data()
        print(self.results_df)

    def remove_duplicate_data(self):
        # Check and drop the duplicate based on having the same pollutant, country, and city name
        self.results_df = self.results_df.drop_duplicates(subset=['measurements_parameter', 'country_name_en', 'city'], keep="first")

        # Get API Data
    def get_data_using_api(self):
        record_fields = []

        # Connect to the API
        response_API = requests.get(
            'https://public.opendatasoft.com/api/records/1.0/search/?dataset=openaq&q=&rows=10000&sort=measurements_lastupdated&facet=country&facet=city&facet=location&facet=measurements_parameter&facet=measurements_sourcename&facet=measurements_lastupdated&facet=country_name_en')
        data = response_API.text
        parse_json = json.loads(data)

        # Split the API data to see records section
        records = parse_json['records']

        # Put the data record fields into a list
        for i in range(len(records)):
            record_fields.append(records[i]['fields'])

        # Put the data that is going to be used into a data frame
        self.results_df = pd.DataFrame(record_fields,
                                       columns=['measurements_unit', 'measurements_value', 'coordinates',
                                                'measurements_sourcename', 'measurements_lastupdated',
                                                'measurements_parameter', 'country_name_en', 'city'])


if __name__ == '__main__':
    live_Data = LiveData()

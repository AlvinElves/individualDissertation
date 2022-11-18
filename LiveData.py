import requests
import json
import numpy as np
import pandas as pd


class LiveData:
    def __init__(self):
        self.live_dataset = None

        self.get_data_using_api()
        self.remove_duplicate_data()
        self.remove_null_data()
        self.write_dataset_to_excel()

        #print(self.live_dataset)

    def write_dataset_to_excel(self):
        self.live_dataset.to_excel('CleanedDataset/CleanedLiveData.xlsx', index=False)

    def split_data_based_on_pollutant(self, name):
        return self.live_dataset.loc[self.live_dataset['measurements_parameter'] == name].reset_index(drop=True)

    def remove_duplicate_data(self):
        # Check and drop the duplicate based on having the same type pollutant, country name, and city name
        self.live_dataset = self.live_dataset.drop_duplicates(subset=['measurements_parameter', 'country_name_en', 'city'],
                                                              keep="first").reset_index(drop=True)

    def remove_null_data(self):
        self.live_dataset[self.live_dataset == 'N/A'] = np.NaN
        #print(self.live_dataset.isnull().sum())

        self.live_dataset = self.live_dataset.dropna(axis=0, how='any').reset_index(drop=True)
        #print(self.live_dataset.isnull().sum())

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
        self.live_dataset = pd.DataFrame(record_fields,
                                         columns=['measurements_unit', 'measurements_value', 'coordinates',
                                            'measurements_sourcename', 'measurements_lastupdated',
                                            'measurements_parameter', 'country_name_en', 'city'])

        # Change the coordinates to latitude and longitude, first coordinate is latitude and second is longitude
        self.live_dataset['latitude'] = self.live_dataset['coordinates'].str.get(0)
        self.live_dataset['longitude'] = self.live_dataset['coordinates'].str.get(1)
        self.live_dataset = self.live_dataset.drop(['coordinates'], axis=1)


if __name__ == '__main__':
    live_Data = LiveData()

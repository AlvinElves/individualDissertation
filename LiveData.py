import requests
import json
import numpy as np
import pandas as pd


class LiveData:
    def __init__(self):
        self.live_dataset = None
        self.all_live_dataset = None

        self.get_data_using_api()
        self.split_date()
        self.remove_duplicate_data()
        self.remove_null_data()
        self.write_dataset_to_excel()

    def split_date(self):
        # Split the last_updated date and time into day, month, year, time and timezone column
        self.live_dataset[["Date", "Timezone"]] = self.live_dataset["measurements_lastupdated"].str.split("+", expand=True)
        self.live_dataset[["Date", "Time"]] = self.live_dataset["Date"].str.split("T", expand=True)
        self.live_dataset['Date'] = pd.to_datetime(self.live_dataset.Date, format='%Y-%m-%d')
        self.live_dataset['Day'] = self.live_dataset['Date'].dt.day
        self.live_dataset['Month'] = self.live_dataset['Date'].dt.month
        self.live_dataset['Year'] = self.live_dataset['Date'].dt.year

        # Drop the unused column
        self.live_dataset = self.live_dataset.drop(columns=['measurements_lastupdated', 'Date'])

        # Rearrange the column to have the date in front
        date = ['Timezone', 'Time', 'Year', 'Month', 'Day']
        for i in date:
            column = self.live_dataset.pop(i)
            self.live_dataset.insert(0, i, column)

        self.all_live_dataset = self.live_dataset
        self.all_live_dataset = self.all_live_dataset.loc[self.all_live_dataset['measurements_unit'] == 'µg/m³'].reset_index(drop=True)

    def write_dataset_to_excel(self):
        self.live_dataset.to_excel('CleanedDataset/CleanedLiveData.xlsx', index=False)
        self.all_live_dataset.to_excel('CleanedDataset/CleanedAllLiveData.xlsx', index=False)

    def split_data_based_on_pollutant(self, name):
        return self.live_dataset.loc[self.live_dataset['measurements_parameter'] == name].reset_index(drop=True)

    def remove_duplicate_data(self):
        # Check and drop the duplicate based on having the same type pollutant, country name, and city name
        self.live_dataset = self.live_dataset.drop_duplicates(subset=['measurements_parameter', 'country_name_en', 'city'],
                                                              keep="first").reset_index(drop=True)

    def remove_null_data(self):
        self.live_dataset[self.live_dataset == 'N/A'] = np.NaN

        self.live_dataset = self.live_dataset.dropna(axis=0, how='any').reset_index(drop=True)
        self.all_live_dataset = self.all_live_dataset.dropna(axis=0, how='any').reset_index(drop=True)

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

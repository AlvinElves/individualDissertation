import requests
import json
import numpy as np
import pandas as pd


class LiveData:
    """
    LiveData Class to be imported into GUI files. This class contains the API Air Quality (Live Data) that can be called for
    LiveDataVis class. This class gets the dataset from API and clean the dataset.
    """
    def __init__(self):
        """
        LiveData Class Constructor that calls the dataset from API and clean the dataset.
        """
        self.live_dataset = pd.DataFrame()
        self.all_live_dataset = pd.DataFrame()

        self.get_data_using_api()
        self.split_date()
        self.remove_unwanted_data()
        self.remove_null_data()

    def split_date(self):
        """
        A function that split the measurements_lastupdated column into several column, Date, Month, Year, Time, and Timezone column.
        :return: A dataset that has Date, Month, Year, Time, and Timezone as column
        """
        # Split the last_updated date and time into day, month, year, time and timezone column
        self.live_dataset[["Date", "Timezone"]] = self.live_dataset["measurements_lastupdated"].str.split("+",
                                                                                                          expand=True)
        self.live_dataset[["Date", "Time"]] = self.live_dataset["Date"].str.split("T", expand=True)

        data = self.live_dataset[["Date", "Time", 'Timezone']].iloc[0]
        self.last_updated = data[0] + ', ' + data[1] + '\nGMT+' + data[2]

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

        self.all_live_dataset = self.live_dataset.copy()

    @staticmethod
    def split_data_based_on_pollutant(dataset, name):
        """
        A function that splits the data based on the air pollutant
        :param dataset: The dataset that is used to visualise
        :param name: The type of air pollutant the user want to visualise
        :return: A dataset that only contains the air pollutant chosen
        """
        # Get the rows of data based on the value of the measurements_parameter
        return dataset.loc[dataset['measurements_parameter'] == name].reset_index(drop=True)

    def on_map_data(self, pollutant_type, visual_type):
        """
        A function that gets the data based on the pollutant type and visual type chosen
        :param pollutant_type: The type of air pollutant the user want to visualise
        :param visual_type: The type of measurement time the user want to visualise
        :return: A dataset that has only the pollutant type and in the type of measurement chosen
        """
        data = self.split_data_based_on_pollutant(self.all_live_dataset, pollutant_type)

        # If user chose most frequent data, then top 80 city that has the most information
        if visual_type == 'most_frequent':
            frequent_city = data['city'].value_counts().index.values
            visual_city = frequent_city[:80]
        # If user chose last updated data, then top 80 city that has been newly updated
        elif visual_type == 'last_updated':
            unique_city = data['city'].unique()
            visual_city = unique_city[:80]

        # Get the row of the data based on the city
        visual_data = data.loc[data['city'].isin(visual_city)].reset_index(drop=True)

        return visual_data

    def remove_unwanted_data(self):
        """
        A function that clean the data by preprocessing it, removing redundant values.
        :return: A dataset that does not have redundant values
        """
        # Change the ppm parameter to µg/m³, since 1ppm = 1000µg/m³
        self.live_dataset.loc[
            self.live_dataset['measurements_unit'] == 'ppm', ['measurements_value']] = self.live_dataset.loc[
            self.live_dataset['measurements_unit'] == 'ppm']['measurements_value'] * 1000

        self.live_dataset.loc[
            self.live_dataset['measurements_unit'] == 'ppm', ['measurements_unit']] = 'µg/m³'

        self.all_live_dataset.loc[
            self.all_live_dataset['measurements_unit'] == 'ppm', ['measurements_value']] = self.all_live_dataset.loc[
            self.all_live_dataset['measurements_unit'] == 'ppm']['measurements_value'] * 1000

        self.all_live_dataset.loc[
            self.all_live_dataset['measurements_unit'] == 'ppm', ['measurements_unit']] = 'µg/m³'

        self.live_dataset = self.live_dataset.loc[self.live_dataset["measurements_value"] > -1]
        self.all_live_dataset = self.all_live_dataset.loc[self.all_live_dataset["measurements_value"] > -1]

        # Check and drop the duplicate based on having the same type pollutant, country name, city name, and time
        self.live_dataset = self.live_dataset.drop_duplicates(
            subset=['measurements_parameter', 'country_name_en', 'city', 'Time'],
            keep="first").reset_index(drop=True)

        self.all_live_dataset = self.all_live_dataset.drop_duplicates(
            subset=['measurements_parameter', 'country_name_en', 'city', 'Time'],
            keep="first").reset_index(drop=True)

    def remove_null_data(self):
        """
        A function that clean the data by preprocessing it, removing null values.
        :return: A dataset that does not have null values
        """
        # Change the dataset with N/A value to nan value
        self.live_dataset[self.live_dataset == 'N/A'] = np.NaN
        self.all_live_dataset[self.all_live_dataset == 'N/A'] = np.NaN

        # Drop the nan value
        self.live_dataset = self.live_dataset.dropna(axis=0, how='any').reset_index(drop=True)
        self.all_live_dataset = self.all_live_dataset.dropna(axis=0, how='any').reset_index(drop=True)

        # Get API Data
    def get_data_using_api(self):
        """
        A function that gets the dataset from API and save it into a pandas dataframe.
        :return: A dataset that contains the Live Air Quality Data from API
        """
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

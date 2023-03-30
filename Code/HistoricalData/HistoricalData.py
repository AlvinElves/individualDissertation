import pandas as pd
import numpy as np
import os


class HistoricalData:
    """
    HistoricalData Class to be imported into GUI files. This class contains the Air Quality (Historical Data) that can be called for
    AIModel class and HistoricalDataVis class. This class read the dataset from the Excel file and clean the dataset.
    """

    def __init__(self):
        """
        HistoricalData Class Constructor that calls the dataset from excel and clean the dataset.
        """
        self.historical_dataset = pd.DataFrame()
        self.merged_date_dataset = pd.DataFrame()
        self.original_dataset = pd.DataFrame()

        self.get_data_from_excel()
        self.data_cleaning()

    def create_folder(self, name):
        """
        A function that is used to create a folder in the user's computer.
        :param name: The name of the created folder
        :return: Creates the folder and return the path of the folder
        """
        new_directory = name  # New folder name
        path = os.path.dirname(os.getcwd())  # Get current file path

        data_path = os.path.join(path, new_directory)

        # Create new folder
        if not os.path.exists(data_path):
            os.mkdir(data_path)

        return data_path

    def grouping(self, group_by_column):
        """
        A function that group the dataset based on the column chosen and get the average value of the group.
        :param group_by_column: The column from the dataset the user want to visualise
        :return: A dataset that is grouped by the column chosen and the average value of the group
        """
        # Group the dataset by the column chosen and get the average value from the groups
        return self.historical_dataset.groupby(group_by_column, as_index=False).mean(numeric_only=True).reset_index(
            drop=True)

    def split_date(self):
        """
        A function that split the Date column into several column, Day, Month, and Year column.
        :return: A dataset that has Day, Month, Year as column
        """
        # Split the date into day month and year column and drop the Date column
        self.historical_dataset['Day'] = self.historical_dataset['Date'].dt.day
        self.historical_dataset['Month'] = self.historical_dataset['Date'].dt.month
        self.historical_dataset['Year'] = self.historical_dataset['Date'].dt.year

        # Rearrange the column to have the date in front
        date = ['Year', 'Month', 'Day']
        for i in date:
            column = self.historical_dataset.pop(i)
            self.historical_dataset.insert(0, i, column)
        self.historical_dataset = self.historical_dataset.drop(columns=['Date'])

    def merge_date(self):
        """
        A function that merge the Day, Month, and Year column into one column, Date.
        :return: A dataset that has Date as column only
        """
        # Change the column Date to datetime format
        self.merged_date_dataset['Date'] = pd.to_datetime(self.merged_date_dataset['Date']).dt.date

    def data_cleaning(self):
        """
        A function that clean the data by preprocessing it, removing null values, unwanted column, and redundant values.
        :return: A dataset that is cleaned and not redundant from the Air Quality Data
        """
        # Change the -200 value to null, -200 is null based on the sheet
        self.historical_dataset[self.historical_dataset == -200] = np.NaN

        # Drop the column NMHC(GT) since almost 90% of the data is null
        self.historical_dataset = self.historical_dataset.drop(columns=['NMHC(GT)'])

        # Delete the other rows that contains null
        self.historical_dataset = self.historical_dataset.dropna(axis=0, how='any').reset_index(drop=True)

        # Copy to another dataset
        self.merged_date_dataset = self.historical_dataset.copy()

        self.merge_date()

        self.split_date()

    def get_data_from_excel(self):
        """
        A function that read the Air Quality Excel File and save it into a pandas dataframe.
        :return: A dataset that contains the Air Quality Data from Excel File
        """
        # Read the dataset from Excel file
        self.historical_dataset = pd.read_excel("../Dataset/AirQualityUCI.xlsx")
        self.original_dataset = self.historical_dataset.copy()


if __name__ == '__main__':
    historical_Data = HistoricalData()

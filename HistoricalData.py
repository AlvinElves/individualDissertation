import pandas as pd
import numpy as np
import os


class HistoricalData:

    def __init__(self):
        self.historical_dataset = pd.DataFrame()
        self.merged_date_dataset = pd.DataFrame()
        self.original_dataset = pd.DataFrame()

        self.get_data_from_excel()
        self.data_cleaning()

    def grouping(self, group_by_column):
        return self.historical_dataset.groupby(group_by_column, as_index=False).mean(numeric_only=True).reset_index(drop=True)

    def split_date(self):
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
        self.merged_date_dataset['Date'] = pd.to_datetime(self.merged_date_dataset['Date']).dt.date

    def data_cleaning(self):

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

        new_directory = "CleanedDataset"  # New folder name
        path = os.getcwd()  # Get current file path
        data_path = os.path.join(path, new_directory)

        # Create new folder
        if not os.path.exists(data_path):
            os.mkdir(data_path)

            # Put it into an Excel file to visualise using tableau or excel
        self.historical_dataset.to_excel('CleanedDataset/CleanedHistoricalData.xlsx', index=False)
        self.merged_date_dataset.to_excel('CleanedDataset/MergedHistoricalData.xlsx', index=False)

    def get_data_from_excel(self):
        self.historical_dataset = pd.read_excel("Dataset/AirQualityUCI.xlsx")
        self.original_dataset = self.historical_dataset.copy()


if __name__ == '__main__':
    historical_Data = HistoricalData()

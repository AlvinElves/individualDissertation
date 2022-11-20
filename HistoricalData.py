import pandas as pd
import numpy as np


class HistoricalData:
    def __init__(self):
        self.historical_dataset = None

        self.get_data_from_excel()
        self.data_cleaning()
        print(self.historical_dataset)

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

    def data_cleaning(self):

        # Change the -200 value to null, -200 is null based on the sheet
        self.historical_dataset[self.historical_dataset == -200] = np.NaN

        # Drop the column NMHC(GT) since almost 90% of the data is null
        self.historical_dataset = self.historical_dataset.drop(columns=['NMHC(GT)'])

        # Delete the other rows that contains null
        self.historical_dataset = self.historical_dataset.dropna(axis=0, how='any').reset_index(drop=True)

        self.split_date()

        # Put it into an Excel file to visualise using tableau or excel
        self.historical_dataset.to_excel('CleanedDataset/CleanedHistoricalData.xlsx', index=False)

    def get_data_from_excel(self):
        self.historical_dataset = pd.read_excel("Dataset/AirQualityUCI.xlsx")


if __name__ == '__main__':
    historical_Data = HistoricalData()

import pandas as pd
import numpy as np


class HistoricalData:
    def __init__(self):
        self.historical_dataset = None

        self.get_data_from_excel()
        self.data_cleaning()
        print(self.historical_dataset)

    def data_cleaning(self):

        # Change the -200 value to null, -200 is null based on the sheet
        self.historical_dataset[self.historical_dataset == -200] = np.NaN
        print(self.historical_dataset.isnull().sum())

        # Drop the column NMHC(GT) since almost 90% of the data is null
        self.historical_dataset = self.historical_dataset.drop(columns=['NMHC(GT)'])
        print(self.historical_dataset.isnull().sum())

        # Delete the other rows that contains null
        column_header = list(self.historical_dataset.columns.values)
        for header in column_header:
            self.historical_dataset = self.historical_dataset[~self.historical_dataset[[header]].isnull().all(axis=1)]
        print(self.historical_dataset.isnull().sum())

        # Put it into an Excel file to visualise using tableau or excel
        self.historical_dataset.to_excel('CleanedDataset/CleanedHistoricalData.xlsx', index=False)

    def get_data_from_excel(self):
        self.historical_dataset = pd.read_excel("Dataset/AirQualityUCI.xlsx")
        print(self.historical_dataset)


if __name__ == '__main__':
    historical_Data = HistoricalData()

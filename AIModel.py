from HistoricalData import *
import pandas as pd


class AIModel:
    def __init__(self):
        self.dataset = None
        self.get_data_from_excel()

    def get_data_from_excel(self):
        self.dataset = pd.read_excel("Dataset/AirQualityUCI.xlsx")


if __name__ == '__main__':
    model = AIModel()

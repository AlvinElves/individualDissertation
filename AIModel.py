from HistoricalData import *


class AIModel:
    def __init__(self):
        self.historical_data = HistoricalData()
        dataset = self.historical_data.historical_dataset.copy()


if __name__ == '__main__':
    model = AIModel()

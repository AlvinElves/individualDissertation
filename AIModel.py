from AIModelVis import *


class AIModel:
    def __init__(self):
        ai_Model_Vis = AIModelVis()

        T_dataset = ai_Model_Vis.feature_scaling('lasso', ai_Model_Vis.null_value('delete', ai_Model_Vis.outliers('delete', ai_Model_Vis.data_preprocessing('T'))), 'T')
        AH_dataset = ai_Model_Vis.feature_scaling('none', ai_Model_Vis.null_value('delete', ai_Model_Vis.outliers('delete', ai_Model_Vis.data_preprocessing('AH'))), 'AH')
        RH_dataset = ai_Model_Vis.feature_scaling('lasso', ai_Model_Vis.null_value('delete', ai_Model_Vis.outliers('none', ai_Model_Vis.data_preprocessing('RH'))), 'RH')

        print(T_dataset.shape)
        print(AH_dataset.shape)
        print(RH_dataset.shape)
        """
        self.T_model = RandomForestRegressor(n_estimators=242, max_features='log2', criterion='friedman_mse',
                                             random_state=5, n_jobs=5)
        self.T_model.fit(T_dataset.drop(['T'], axis=1), T_dataset['T'])

        self.AH_model = RandomForestRegressor(n_estimators=255, max_features=1.0, criterion='squared_error',
                                              random_state=5, n_jobs=5)
        self.AH_model.fit(AH_dataset.drop(['AH'], axis=1), AH_dataset['AH'])

        self.RH_model = RandomForestRegressor(n_estimators=487, max_features=1.0, criterion='friedman_mse',
                                              random_state=5, n_jobs=5)
        self.RH_model.fit(RH_dataset.drop(['RH'], axis=1), RH_dataset['RH'])
        """


if __name__ == '__main__':
    model = AIModel()

from AIModelVis import *
import plotly.express as px


class HistoricalDataVisualisation:
    def __init__(self):
        self.model_vis = AIModelVis()
        self.historical_data = self.model_vis.ai_model.historical_data

        self.path = self.model_vis.create_Folder()

        # self.plot_Bar_by_Month(self.historical_data)
        # self.plot_Bar_by_Day(self.historical_data)
        self.plot_line_all(self.historical_data, ['T', 'AH', 'RH'])

    def plot_line_all(self, historical_data, y_Value):
        df = historical_data.merged_date_dataset.copy()
        df['Date'] = pd.to_datetime(df.Date.astype(str) + ' ' + df.Time.astype(str))
        fig = px.line(df, x='Date', y=y_Value, title='Date VS Multiple Attributes', render_mode='webg1')
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1 Month", step="month", stepmode="backward"),
                    dict(count=6, label="6 Month", step="month", stepmode="backward"),
                    dict(count=1, label="1 Year", step="year", stepmode="backward"),
                    dict(label='All', step="all")
                ])
            ),
            tickformatstops=[
                dict(dtickrange=[None, 1000], value="%H:%M:%S.%L ms"),
                dict(dtickrange=[1000, 60000], value="%H:%M:%S"),
                dict(dtickrange=[60000, 3600000], value="%H:%M hr"),
                dict(dtickrange=[3600000, 86400000], value="%H:%M hr"),
                dict(dtickrange=[86400000, 604800000], value="%e %b"),
                dict(dtickrange=[604800000, "M1"], value="%e %b"),
                dict(dtickrange=["M1", "M12"], value="%b '%y"),
                dict(dtickrange=["M12", None], value="%Y")
            ]
        )

        button_list = [dict(label='All', method='update',
                            args=[{'visible': [True, True, True]}, {'title': 'Date VS Multiple Attributes'}])]
        for i in range(0, len(y_Value)):
            visible = [j == i for j in list(range(0, len(y_Value)))]

            button_list.append(dict(label=y_Value[i], method='update',
                                    args=[{'visible': visible}, {'title': 'Date VS ' + str(y_Value[i])}]))

        fig.update_layout(
            updatemenus=[
                dict(
                    active=0,
                    buttons=button_list
                )
            ],
            legend=dict(
                title="Attributes"
            )
        )
        fig.write_html(self.path + "/" + "Graph.html")
        fig.show()

    @staticmethod
    def plot_Bar_by_Month(historical_data):
        month_year_data = historical_data.grouping(['Month', 'Year'])
        month_year_data['Year'] = month_year_data['Year'].astype(str)

        fig = px.bar(month_year_data, x="Month", y='CO(GT)',
                     color='Year')
        fig.update_layout(barmode='group')
        fig.show()

    @staticmethod
    def plot_Bar_by_Day(historical_data):
        month_year_data = historical_data.grouping(['Day', 'Month', 'Year'])
        month_year_data['Year'] = month_year_data['Year'].astype(str)

        fig = px.bar(month_year_data, x='Day', y='T', facet_col="Month", facet_col_wrap=4,
                     color='Year')
        fig.update_layout(barmode='group')
        # fig = px.bar(month_year_data, x='Month', y='T')
        fig.show()


if __name__ == '__main__':
    live_Data = HistoricalDataVisualisation()

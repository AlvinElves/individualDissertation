from Code.AIModel.AIModelVis import *
import plotly.express as px
import matplotlib.animation as animate


class HistoricalDataVisualisation:
    def __init__(self):
        self.model_vis = AIModelVis()
        self.historical_data = self.model_vis.ai_model.historical_data

        self.path = self.model_vis.create_Folder()

        #self.plot_Bar_by_Month(self.historical_data, 'CO(GT)')
        #self.plot_Bar_by_Day(self.historical_data, 'CO(GT)')
        # self.plot_line_all(self.historical_data, ['T', 'AH', 'RH'])
        # self.animated_line_graph(self.historical_data, ['T', 'AH', 'RH'])
        self.animated_bar_graph(self.historical_data, 'T')

    def animated_line_graph(self, historical_data, column):
        colours = []
        time = []
        colour_number = 0

        df = historical_data.merged_date_dataset.copy()
        df['Date'] = pd.to_datetime(df.Date.astype(str) + ' ' + df.Time.astype(str))
        column_name = ['Date'] + column
        df = df[column_name]
        df = df.set_index('Date')

        for i in range(len(df.columns)):
            colour_number += 1
            time.append(df.columns[i])
            colours.append("C" + str(colour_number))

        colours_legend = dict(zip(time, colours))
        labels = list(colours_legend.keys())
        handles = [plt.Rectangle((0, 0), width=1, height=1, color=colours_legend[label]) for label in labels]

        fig = plt.figure()

        def build(i=int):
            plt.clf()
            p = plt.plot(df[:i].index, df[:i].values)
            plt.legend(handles, labels)
            plt.xticks(rotation=45, ha="right", rotation_mode="anchor")
            plt.subplots_adjust(bottom=0.2, top=0.9)
            plt.xlabel('Dates')
            plt.ylabel('Values')

            for j in range(len(df.columns)):
                p[j].set_color(colours[j])

        animator = animate.FuncAnimation(fig, build, interval=50)
        plt.show()

    def animated_bar_graph(self, historical_data, column):
        colours = []
        time = []
        colour_number = 0
        df = historical_data.grouping(['Day', 'Month', 'Year'])
        df['Date'] = pd.to_datetime(df[['Day', 'Month', 'Year']]).dt.strftime('%m-%d')
        """column_name = ['Date'] + [column]
        df = df[column_name]
        df = df.set_index('Date')"""

        print(df)

        """df = historical_data.merged_date_dataset.copy()
        df['Date'] = pd.to_datetime(df.Date.astype(str) + ' ' + df.Time.astype(str))
        column_name = ['Date'] + column
        df = df[column_name]
        df = df.set_index('Date')

        for i in range(len(df.columns)):
            colour_number += 1
            time.append(df.columns[i])
            colours.append("C" + str(colour_number))

        colours_legend = dict(zip(time, colours))
        labels = list(colours_legend.keys())
        handles = [plt.Rectangle((0, 0), width=1, height=1, color=colours_legend[label]) for label in labels]

        fig = plt.figure()

        def test(i=int):
            iv = min(i, len(df.index) - 1)
            objects = df.max().index
            y_pos = np.arange(len(objects))
            performance = df.iloc[[iv]].values.tolist()[0]

            plt.bar(y_pos, performance, align='center')
            plt.xticks(y_pos, objects)
            plt.ylabel('Values')
            plt.xlabel('Dates')
            plt.title(str(df.index[iv].strftime('%y/%m/%d')))

        animator = animate.FuncAnimation(fig, test, interval=50)
        plt.show()"""

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

    def plot_Bar_by_Month(self, historical_data, y_Value):
        month_year_data = historical_data.grouping(['Month', 'Year'])
        month_year_data['Year'] = month_year_data['Year'].astype(str)

        fig = px.bar(month_year_data, x="Month", y=y_Value,
                     color='Year', title="Monthly Bar Graph on " + y_Value + " value")
        fig.update_layout(barmode='group')
        #fig.write_html(self.path + "/" + "Graph.html")
        fig.show(config={'displayModeBar': False})

    def plot_Bar_by_Day(self, historical_data, y_Value):
        month_year_data = historical_data.grouping(['Day', 'Month', 'Year'])
        month_year_data['Year'] = month_year_data['Year'].astype(str)

        fig = px.bar(month_year_data, x='Day', y=y_Value, facet_col="Month", facet_col_wrap=4,
                     color='Year', title="Daily Bar Graph on " + y_Value + " value")
        fig.update_layout(barmode='group')
        #fig.write_html(self.path + "/" + "Graph.html")

        fig.show(config={'displayModeBar': False})


if __name__ == '__main__':
    live_Data = HistoricalDataVisualisation()

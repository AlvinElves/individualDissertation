from Code.HistoricalData.HistoricalData import *
import plotly.express as px
import matplotlib.animation as animate
import matplotlib.pyplot as plt


class HistoricalDataVisualisation:
    def __init__(self):
        self.historical_data = HistoricalData()

        # self.path = self.model_vis.create_Folder()

    @staticmethod
    def date_index_dataset(historical_data, column):
        df = historical_data.grouping(['Day', 'Month', 'Year'])

        df['Date'] = pd.to_datetime(df[['Day', 'Month', 'Year']]).dt.strftime('%m-%d')
        column_name = ['Date', 'Year'] + [column]
        df = df[column_name]

        unique_year = df['Year'].unique()
        df1 = df.loc[df['Year'] == unique_year[1]]
        df2 = df.loc[df['Year'] == unique_year[0]]
        merged_df = pd.merge(df1, df2, on='Date', how='left')
        merged_df2 = pd.merge(df1, df2, on='Date', how='right')

        column_str = column + '_x'
        merged_df2 = merged_df2[merged_df2[column_str].isnull()].reset_index(drop=True)

        final_df = pd.concat([merged_df, merged_df2], ignore_index=True)

        column_use = ['Date'] + [column + '_x'] + [column + '_y']
        final_df = final_df[column_use]
        final_df.columns = ['Date', '2004', '2005']

        final_df = final_df.sort_values(by='Date')

        final_df[['Month', 'Day']] = final_df.Date.str.split("-", expand=True)
        final_df['Year'] = 2002
        final_df['Date'] = pd.to_datetime(final_df[['Day', 'Month', 'Year']]).dt.strftime('%b-%d')
        final_df = final_df[['Date', '2004', '2005']]

        saved_df = final_df.copy()

        final_df = final_df.set_index('Date')

        max_value = max(final_df[['2004', '2005']].max(axis=1))

        return final_df, max_value, saved_df

    def animated_line_graph(self, historical_data, column, method):
        df = historical_data.merged_date_dataset.copy()
        df['Date'] = pd.to_datetime(df.Date.astype(str) + ' ' + df.Time.astype(str))
        column_name = ['Date'] + column
        df = df[column_name]
        saved_df = df.copy()
        df = df.set_index('Date')
        if len(df.columns) < 2:
            column_label = df.columns[0]
        else:
            column_label = df.columns

        if method != 'dataset':
            fig = plt.figure()
            fig.canvas.manager.set_window_title('Animated Line Graph Visualisation')

            def build(i=int):
                plt.clf()
                plt.plot(df[:i].index, df[:i].values, label=column_label)
                plt.legend()
                plt.xticks(rotation=45, ha="right", rotation_mode="anchor")
                plt.subplots_adjust(bottom=0.2, top=0.9)
                plt.xlabel('Dates')
                plt.ylabel('Values')

            animator = animate.FuncAnimation(fig, build, interval=50)
            plt.show()
        else:
            return saved_df

    def animated_pie_chart(self, historical_data, column, method):
        final_df, max_value, saved_df = self.date_index_dataset(historical_data, column)

        if method != 'dataset':
            fig, ax = plt.subplots()
            explode = [0.01, 0.01]
            fig.canvas.manager.set_window_title('Animated Pie Chart Visualisation')

            def buildpie(i):
                def absolute_value(val):  # turn % back to the value
                    a = np.round(val / 100. * final_df.iloc[[i]].squeeze().sum(), 3)
                    if a > 0:
                        return a

                ax.clear()
                plot = final_df.iloc[[i]].squeeze().plot.pie(y=final_df.columns, label='',
                                                             autopct=absolute_value, explode=explode, shadow=True)
                plot.set_title('Date of the year: ' + str(final_df.index[i]), fontsize=12)

            animator = animate.FuncAnimation(fig, buildpie, interval=200)
            plt.show()
        else:
            return saved_df

    def animated_bar_graph(self, historical_data, column, method):
        final_df, max_value, saved_df = self.date_index_dataset(historical_data, column)

        if method != 'dataset':
            fig = plt.figure()
            fig.canvas.manager.set_window_title('Animated Bar Graph Visualisation')

            def buildbar(i=int):
                plt.clf()

                number = min(i, len(final_df.index) - 1)
                objects = final_df.max().index
                y_pos = np.arange(len(objects))
                performance = final_df.iloc[[number]].values.tolist()[0]

                plt.bar(y_pos, performance, align='center', label=final_df.columns.values, color=['blue', 'orange'])
                plt.legend()

                plt.xticks(y_pos, objects)
                plt.ylabel(column + ' Values')
                plt.xlabel('Year')

                plt.xlim(-0.5, 1.5)
                plt.ylim(0, max_value + 0.5)

                plt.title('Date of the year: ' + str(final_df.index[number]))

            animator = animate.FuncAnimation(fig, buildbar, interval=100)
            plt.show()
        else:
            return saved_df

    def plot_line_all(self, historical_data, y_Value, method, file_name):
        df = historical_data.merged_date_dataset.copy()
        df['Date'] = pd.to_datetime(df.Date.astype(str) + ' ' + df.Time.astype(str))

        if method != 'dataset':
            if len(y_Value) == 1:
                if y_Value[0] == 'T':
                    variable = 'T (Temperature)'
                elif y_Value[0] == 'AH':
                    variable = 'AH (Absolute Humidity)'
                elif y_Value[0] == 'RH':
                    variable = 'RH (Relative Humidity)'
                else:
                    variable = str(y_Value[0])

                title = 'Date VS Feature ' + variable
            else:
                title = 'Date VS Multiple Features'

            fig = px.line(df, x='Date', y=y_Value, title=title, render_mode='webg1')
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

                if y_Value[i] == 'T':
                    variable = 'T (Temperature)'
                elif y_Value[i] == 'AH':
                    variable = 'AH (Absolute Humidity)'
                elif y_Value[i] == 'RH':
                    variable = 'RH (Relative Humidity)'
                else:
                    variable = str(y_Value[i])

                button_list.append(dict(label=variable, method='update',
                                        args=[{'visible': visible}, {'title': 'Date VS Feature ' + variable}]))

            fig.update_layout(
                updatemenus=[
                    dict(
                        active=0,
                        buttons=button_list
                    )
                ],
                legend=dict(
                    title="Attributes"
                ),
                yaxis_title="Feature Values"
            )
            if method == 'save':
                fig.write_html(file_name)

            fig.show()
        else:
            column_used = ['Date'] + y_Value
            df = df[column_used]
            return df

    def plot_Bar_by_Month(self, historical_data, y_Value, method, file_name):
        month_year_data = historical_data.grouping(['Month', 'Year'])
        month_year_data['Year'] = month_year_data['Year'].astype(str)

        if method != 'dataset':
            fig = px.bar(month_year_data, x="Month", y=y_Value,
                         color='Year', title="Monthly Bar Graph on " + y_Value + " value")
            fig.update_layout(barmode='group', yaxis_title=y_Value + " Values")

            if method == 'save':
                fig.write_html(file_name)

            fig.show()
        else:
            column_used = ['Month', 'Year'] + [y_Value]
            month_year_data = month_year_data[column_used]
            return month_year_data

    def plot_Bar_by_Day(self, historical_data, y_Value, method, file_name):
        month_year_data = historical_data.grouping(['Day', 'Month', 'Year'])
        month_year_data['Year'] = month_year_data['Year'].astype(str)

        if method != 'dataset':
            fig = px.bar(month_year_data, x='Day', y=y_Value, facet_col="Month", facet_col_wrap=4,
                         color='Year', title="Daily Bar Graph on " + y_Value + " value")
            fig.update_layout(barmode='group', yaxis_title=y_Value + " Values")
            if method == 'save':
                fig.write_html(file_name)

            fig.show()
        else:
            column_used = ['Month', 'Year'] + [y_Value]
            month_year_data = month_year_data[column_used]
            return month_year_data


if __name__ == '__main__':
    live_Data = HistoricalDataVisualisation()

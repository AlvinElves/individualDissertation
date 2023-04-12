from Code.HistoricalData.HistoricalData import *
import plotly.express as px
import matplotlib.animation as animate
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter


class HistoricalDataVisualisation:
    """
    HistoricalDataVisualisation Class to be imported into GUI files. This class contains all Historical Data Visualisation functions
    that can be called in the GUI file easily.
    """
    def __init__(self):
        """
        HistoricalDataVisualisation Class Constructor that calls the HistoricalData Class and remove the matplotlib toolbar.
        """
        self.historical_data = HistoricalData()

        # Remove the matplotlib toolbar
        plt.rcParams['toolbar'] = 'None'

    def date_index_dataset(self, column):
        """
        A function that gets the value of the year and put the Date to the index.
        :param column: The column the user want to visualise
        :return: Two dataset that has the value of the year based on the column chosen, and the maximum value of it
        """
        df = self.historical_data.grouping(['Day', 'Month', 'Year'])

        # Create a new column for Date using datetime format
        df['Date'] = pd.to_datetime(df[['Day', 'Month', 'Year']]).dt.strftime('%m-%d')
        column_name = ['Date', 'Year'] + [column]
        df = df[column_name]

        # Get the year from the dataset
        unique_year = df['Year'].unique()

        # Get the dataset based on the value of unique year
        df1 = df.loc[df['Year'] == unique_year[1]]
        df2 = df.loc[df['Year'] == unique_year[0]]

        # Merge the two dataset using left and right join
        merged_df = pd.merge(df1, df2, on='Date', how='left')
        merged_df2 = pd.merge(df1, df2, on='Date', how='right')

        # Drop the row that has null value on the first column
        column_str = column + '_x'
        merged_df2 = merged_df2[merged_df2[column_str].isnull()].reset_index(drop=True)

        # Concatenate the two dataset
        final_df = pd.concat([merged_df, merged_df2], ignore_index=True)

        # Get the useful column from the dataset
        column_use = ['Date'] + [column + '_x'] + [column + '_y']
        final_df = final_df[column_use]
        final_df.columns = ['Date', '2004', '2005']

        # Sort the dataset based on the Date column
        final_df = final_df.sort_values(by='Date')

        # Change the date column to the format (April 01)
        final_df[['Month', 'Day']] = final_df.Date.str.split("-", expand=True)
        final_df['Year'] = 2002
        final_df['Date'] = pd.to_datetime(final_df[['Day', 'Month', 'Year']]).dt.strftime('%b-%d')

        # Get the column needed for visualisation
        final_df = final_df[['Date', '2004', '2005']]

        saved_df = final_df.copy()

        # Set the index of the dataset based on the Date column
        final_df = final_df.set_index('Date')

        # Get the maximum value from the dataset
        max_value = max(final_df[['2004', '2005']].max(axis=1))

        return final_df, max_value, saved_df

    def animated_line_graph(self, column, method):
        """
        A function that is used to visualise the column values in an animated line graph form.
        :param column: The column the user want to visualise
        :param method: The method that the user chose to do with in GUI, can choose between visualise, save visualise and save dataset
        :return: A matplotlib figure that shows the values on the column chosen using line graph and animation
        """
        df = self.historical_data.merged_date_dataset.copy()

        # Create a new column for Date using datetime format
        df['Date'] = pd.to_datetime(df.Date.astype(str) + ' ' + df.Time.astype(str))
        column_name = ['Date'] + column
        df = df[column_name]

        saved_df = df.copy()

        # Set the index of the dataset based on the Date column
        df = df.set_index('Date')

        # If the user chose 1 variable to visualise
        if len(df.columns) < 2:
            # Dataframe column for visualisation
            column_label = df.columns[0]
        else:  # If the user chose more than 1 variable to visualise
            # Dataframe column for visualisation
            column_label = df.columns

        if method != 'dataset':
            # Create a figure and set the window title
            fig = plt.figure()
            fig.canvas.manager.set_window_title('Animated Line Graph Visualisation')

            def build(i=int):
                # Clear the plot
                plt.clf()

                # Plot the dataset using a line chart
                plt.plot(df[:i].index, df[:i].values, label=column_label)

                # Set the plot legend
                plt.legend()

                # Set the axis label
                plt.xticks(rotation=45, ha="right", rotation_mode="anchor")
                plt.subplots_adjust(bottom=0.2, top=0.9)
                plt.gca().xaxis.set_major_formatter(DateFormatter("%Y-%m-%d"))
                plt.xlabel('Dates')
                plt.ylabel('Values')

            # Create the animated chart
            animator = animate.FuncAnimation(fig, build, interval=50)
            plt.show()
        else:
            return saved_df

    def animated_bar_graph(self, column, method):
        """
        A function that is used to visualise the column values in an animated bar graph form.
        :param column: The column the user want to visualise
        :param method: The method that the user chose to do with in GUI, can choose between visualise, save visualise and save dataset
        :return: A matplotlib figure that shows the values on the column chosen using bar graph and animation
        """
        final_df, max_value, saved_df = self.date_index_dataset(column)

        if method != 'dataset':
            # Create a figure and set the window title
            fig = plt.figure(figsize=(10, 7))
            fig.canvas.manager.set_window_title('Animated Bar Graph Visualisation')

            def buildbar(i=int):
                # Clear the plot
                plt.clf()

                # If the history of the animated bar chart is more than or equal to 10
                if i > 10:
                    # Get the X axis value based on the rows of dataset
                    x = np.arange(len(saved_df[i-10:i]))

                    # Plot the dataset based on i variable using two bar chart
                    plt.bar(x - 0.2, saved_df[i-10:i][saved_df.columns[1]], 0.4, label=saved_df.columns[1], color='green')
                    plt.bar(x + 0.2, saved_df[i-10:i][saved_df.columns[2]], 0.4, label=saved_df.columns[2], color='orange')

                    # Set the plot legend
                    plt.legend()

                    # Set the X axis limit
                    plt.xlim(-0.5, len(saved_df[i-10:i]) - 0.5)
                    plt.xticks(x, saved_df[i - 10:i][saved_df.columns[0]])

                    # Loop through the number of bar, set the value of each bar onto the middle of each plotted bar
                    for j in range(len(x)):
                        if not np.isnan(round(saved_df.iloc[i - 10 + j][saved_df.columns[1]], 2)):
                            plt.text(j - 0.2, saved_df.iloc[i - 10 + j][saved_df.columns[1]] / 2,
                                     round(saved_df.iloc[i - 10 + j][saved_df.columns[1]], 2), ha='center', fontsize=8)

                        if not np.isnan(round(saved_df.iloc[i - 10 + j][saved_df.columns[2]], 2)):
                            plt.text(j + 0.2, saved_df.iloc[i - 10 + j][saved_df.columns[2]] / 2,
                                     round(saved_df.iloc[i - 10 + j][saved_df.columns[2]], 2), ha='center', fontsize=8)

                # If the history of the animated bar chart is less than 10
                else:
                    # If the row of dataset is more than 0, then start plot
                    if len(saved_df[:i]) > 0:
                        # Get the X axis value based on the rows of dataset
                        x = np.arange(len(saved_df[:i]))

                        # Plot the dataset based on i variable using two bar chart
                        plt.bar(x - 0.2, saved_df[:i][saved_df.columns[1]], 0.4, label=saved_df.columns[1], color='green')
                        plt.bar(x + 0.2, saved_df[:i][saved_df.columns[2]], 0.4, label=saved_df.columns[2], color='orange')

                        # Set the plot legend
                        plt.legend()

                        # Set the X axis limit
                        plt.xlim(-0.5, len(saved_df[:i]) - 0.5)
                        plt.xticks(x, saved_df[:i][saved_df.columns[0]])

                        # Loop through the number of bar, set the value of each bar onto the middle of each plotted bar
                        for j in range(len(x)):
                            if not np.isnan(round(saved_df.iloc[j][saved_df.columns[1]], 2)):
                                plt.text(j - 0.2, saved_df.iloc[j][saved_df.columns[1]] / 2,
                                         round(saved_df.iloc[j][saved_df.columns[1]], 2), ha='center', fontsize=8)

                            if not np.isnan(round(saved_df.iloc[j][saved_df.columns[2]], 2)):
                                plt.text(j + 0.2, saved_df.iloc[j][saved_df.columns[2]] / 2,
                                         round(saved_df.iloc[j][saved_df.columns[2]], 2), ha='center', fontsize=8)

                # Set the axis label and Y axis limit
                plt.ylim(0, max_value + 0.5)
                plt.ylabel(column + ' Values')
                plt.xlabel('Date')
                plt.xticks(rotation=45, ha="right", rotation_mode="anchor")

                # Set the plot title
                plt.title('2004 VS 2005, Daily Value for feature ' + column)

            # Create the animated chart
            animator = animate.FuncAnimation(fig, buildbar, interval=300)
            plt.show()
        else:
            return saved_df

    def plot_line_all(self, y_Value, method, file_name):
        """
        A function that is used to visualise the column values using line graph.
        :param y_Value: The column(s) the user want to visualise
        :param method: The method that the user chose to do with in GUI, can choose between visualise, save visualise and save dataset
        :param file_name: The name of the file that the user want to use to save the visualisation or dataset
        :return: A plotly HTML figure that shows the value of the column(s) chosen using line graph
        """
        df = self.historical_data.merged_date_dataset.copy()
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

            # Plot the dataset using a line chart
            fig = px.line(df, x='Date', y=y_Value, title=title, render_mode='webg1')

            # Set the X axis label and create a slider and buttons for the user to use
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

            # List of button that shows all the features
            button_list = [dict(label='All', method='update',
                                args=[{'visible': [True, True, True]}, {'title': 'Date VS Multiple Features'}])]
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

                # List of button that used to change the type of the visualisation features
                button_list.append(dict(label=variable, method='update',
                                        args=[{'visible': visible}, {'title': 'Date VS Feature ' + variable}]))

            # Set the Y axis label, legend title and button menus
            fig.update_layout(
                updatemenus=[
                    dict(
                        active=0,
                        buttons=button_list
                    )
                ],
                legend=dict(
                    title="Features"
                ),
                yaxis_title="Feature Values"
            )
            if method == 'save':
                # Save the figure
                fig.write_html(file_name)

            fig.show()
        else:
            # Get the dataset based on the column used in the visualisation
            column_used = ['Date'] + y_Value
            df = df[column_used]
            return df

    def plot_Bar_by_Month(self, y_Value, method, file_name):
        """
        A function that is used to visualise the monthly column values using bar graph.
        :param y_Value: The column the user want to visualise
        :param method: The method that the user chose to do with in GUI, can choose between visualise, save visualise and save dataset
        :param file_name: The name of the file that the user want to use to save the visualisation or dataset
        :return: A plotly HTML figure that shows the value of the column chosen using bar graph
        """
        month_year_data = self.historical_data.grouping(['Month', 'Year'])
        month_year_data['Year'] = month_year_data['Year'].astype(str)

        if method != 'dataset':
            # Plot the dataset showing visualisation average value from each month using a bar chart
            fig = px.bar(month_year_data, x="Month", y=y_Value,
                         color='Year', title="Monthly Bar Graph on " + y_Value + " value")

            # Set the Y axis label
            fig.update_layout(barmode='group', yaxis_title=y_Value + " Values")

            if method == 'save':
                # Save the figure
                fig.write_html(file_name)

            fig.show()
        else:
            # Get the dataset based on the column used in the visualisation
            column_used = ['Month', 'Year'] + [y_Value]
            month_year_data = month_year_data[column_used]
            return month_year_data

    def plot_Bar_by_Day(self, y_Value, method, file_name):
        """
        A function that is used to visualise the daily column values using bar graph.
        :param y_Value: The column the user want to visualise
        :param method: The method that the user chose to do with in GUI, can choose between visualise, save visualise and save dataset
        :param file_name: The name of the file that the user want to use to save the visualisation or dataset
        :return: A plotly HTML figure that shows the value of the column chosen using bar graph
        """
        month_year_data = self.historical_data.grouping(['Day', 'Month', 'Year'])
        month_year_data['Year'] = month_year_data['Year'].astype(str)

        if method != 'dataset':
            # Plot the dataset showing visualisation value from the year using a bar chart
            fig = px.bar(month_year_data, x='Day', y=y_Value, facet_col="Month", facet_col_wrap=4,
                         color='Year', title="Daily Bar Graph on " + y_Value + " value")

            # Set the Y axis label
            fig.update_layout(barmode='group', yaxis_title=y_Value + " Values")
            if method == 'save':
                # Save the figure
                fig.write_html(file_name)

            fig.show()
        else:
            # Get the dataset based on the column used in the visualisation
            column_used = ['Day', 'Month', 'Year'] + [y_Value]
            month_year_data = month_year_data[column_used]
            return month_year_data


if __name__ == '__main__':
    live_Data = HistoricalDataVisualisation()

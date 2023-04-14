from Code.LiveData.LiveData import *
from Code.HandlingInteractions import *

import folium
import webbrowser
import os

import plotly.graph_objects as go

import geopandas as gpd
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


class LiveDataVisualisation:
    """
    LiveDataVisualisation Class to be imported into GUI files. This class contains all Live Data Visualisation functions that can
    be called in the GUI file easily.
    """
    def __init__(self):
        """
        LiveDataVisualisation Class Constructor that calls the LiveData Class and Matplotlib Interaction Class, remove the matplotlib
        toolbar and creates all the pop-up maps.
        """
        self.interact = HandlingInteractions()
        self.live_data = LiveData()

        self.dataset_in_pollutant_order = pd.DataFrame()
        self.pop_up_df = pd.DataFrame(columns=['City', 'html_file', 'Latitude', 'Longitude'])

        self.create_Folder('LiveDataVisualisation', True)

        self.pop_up_graph()
        self.create_Map()

        # Remove the matplotlib toolbar
        plt.rcParams['toolbar'] = 'None'

    # Use scatter map to produce a bubble map
    def bubble_map(self, pollutant_type):
        """
        A function that creates a bubble map to visualise the pollutant chosen.
        :param pollutant_type: The type of air pollutant the user want to visualise
        :return: A matplotlib figure that shows the bubble map on the pollutant chosen using a scatter plot
        """
        # Get the world map from reading the file online
        worldmap = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

        # Creating axes and plotting world map
        fig, ax = plt.subplots(figsize=(12, 6))
        fig.canvas.manager.set_window_title('Bubble Map Visualisation')

        # Allow panning and zooming using a mouse
        pan_handler = panhandler(fig, 1)
        self.interact.zoom_factory(ax, base_scale=1.2)

        # Plot the world map on ax
        worldmap.plot(ax=ax)

        data = self.live_data.split_data_based_on_pollutant(self.live_data.live_dataset, pollutant_type)

        # Plotting the measurements data with a color map
        x = data['longitude']
        y = data['latitude']
        z = data['measurements_value']

        # Create how size of each scatter point
        s = 10 * z
        s[s > 200] = 200

        # Plot the data using a scatter plot
        plt.scatter(x, y, s=s, c=z, alpha=0.6, vmin=min(z), vmax=max(z), cmap='autumn_r')
        plt.colorbar(label='measurements_value')

        # Creating axis limits and title
        plt.xlim([-180, 180])
        plt.ylim([-90, 90])

        # Set the title, X and Y labels for the figure
        plt.title(pollutant_type + " Pollutant Bubblemap")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")

        plt.show()

    # Bar Graph on world map
    def bar_graph_on_map(self, pollutant_type, visual_type):
        """
        A function that allows the user to visualise the pollutant chosen using a bar graph and the graph is planted into a world map.
        :param pollutant_type: The type of air pollutant the user want to visualise
        :param visual_type: The type of measurement time the user want to visualise
        :return: A matplotlib figure that shows the bar graph on map for the pollutant chosen using a bar graph
        """
        colours = []
        time = []
        colour_number = 0
        visual_city = []
        unique_time = []

        # Creating axes and plotting world map
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        fig, ax = plt.subplots(figsize=(12, 6))
        fig.canvas.manager.set_window_title('Bar Graph on Map Visualisation')

        # Allow panning and zooming using a mouse
        pan_handler = panhandler(fig, 1)
        self.interact.zoom_factory(ax, base_scale=1.2)

        # Plot the world map on ax
        world.plot(ax=ax)

        # Creating axis limits and title
        plt.xlim([-180, 180])
        plt.ylim([-90, 90])

        # Set the X and Y labels for the figure
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")

        data = self.live_data.split_data_based_on_pollutant(self.live_data.all_live_dataset, pollutant_type)

        if visual_type == 'most_frequent':
            # Get the most frequent city data
            frequent_city = data['city'].value_counts().index.values
            visual_city = frequent_city[:80]

            visual_data = self.live_data.on_map_data(pollutant_type, 'most_frequent')
            unique_time = visual_data['Time'].unique()

            # Set the title for the figure
            plt.title("Most Frequent Bar Graph on map for " + pollutant_type + " Pollutant")
        elif visual_type == 'last_updated':
            # Get the last updated city data
            unique_city = data['city'].unique()
            visual_city = unique_city[:80]

            visual_data = self.live_data.on_map_data(pollutant_type, 'last_updated')
            unique_time = visual_data['Time'].unique()

            # Set the title for the figure
            plt.title("Last Updated Bar Graph on map for " + pollutant_type + " Pollutant")

        # Create the plot legend based on the unique time in the dataset
        for i in range(len(unique_time)):
            colour_number += 1
            time.append(unique_time[i])
            colours.append("C" + str(colour_number))

        colours_legend = dict(zip(time, colours))
        labels = list(colours_legend.keys())
        handles = [plt.Rectangle((0, 0), 1, 1, color=colours_legend[label]) for label in labels]
        plt.legend(handles, labels)

        for i in range(0, len(visual_city)):
            measurements = []
            # Get the row of the data based on the value of the city
            city_data = data.loc[data['city'] == visual_city[i]].reset_index(drop=True)

            # Get the latitude and longitude of the data
            latitude = city_data['latitude'].iloc[0]
            longitude = city_data['longitude'].iloc[0]

            # Make the value of the data to be in correct position as the unique time used
            for j in unique_time:
                for time in city_data['Time']:
                    if time != j:
                        measurements.append(0)
                    else:
                        values = city_data[city_data['Time'] == j]
                        measurements_data = values['measurements_value'].values
                        measurements.append(float(measurements_data))

            x_axis = list(range(1, len(measurements) + 1))

            if all(num == 0 for num in measurements) and len(measurements) > 0:
                continue

            # Plot the bar chart on the world map
            ax_bar = inset_axes(ax, width=0.6, height=0.4, loc=10, bbox_to_anchor=(longitude, latitude),
                                bbox_transform=ax.transData)

            ax_bar.bar(x_axis, measurements, color=colours)
            ax_bar.set_axis_off()

        plt.show()

    # Pie Chart on world map
    def pie_chart_on_map(self, pollutant_type, visual_type):
        """
        A function that allows the user to visualise the pollutant chosen using a pie chart and the graph is planted into a world map.
        :param pollutant_type: The type of air pollutant the user want to visualise
        :param visual_type: The type of measurement time the user want to visualise
        :return: A matplotlib figure that shows the bar graph on map for the pollutant chosen using a pie chart
        """
        colours = []
        time = []
        colour_number = 0
        visual_city = []

        # Creating axes and plotting world map
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        fig, ax = plt.subplots(figsize=(12, 6))
        fig.canvas.manager.set_window_title('Pie Chart on Map Visualisation')

        # Allow panning and zooming using a mouse
        pan_handler = panhandler(fig, 1)
        self.interact.zoom_factory(ax, base_scale=1.2)

        # Plot the world map on ax
        world.plot(ax=ax)

        # Creating axis limits and title
        plt.xlim([-180, 180])
        plt.ylim([-90, 90])

        # Set the X and Y labels for the figure
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")

        # Plotting the measurements data with a color map
        data = self.live_data.split_data_based_on_pollutant(self.live_data.all_live_dataset, pollutant_type)

        unique_time = data['Time'].unique()

        if visual_type == 'most_frequent':
            frequent_city = data['city'].value_counts().index.values
            visual_city = frequent_city[:80]

            # Set the title for the figure
            plt.title("Most Frequent Pie Chart on map for " + pollutant_type + " Pollutant")
        elif visual_type == 'last_updated':
            unique_city = data['city'].unique()
            visual_city = unique_city[:80]

            # Set the title for the figure
            plt.title("Last Updated Pie Chart on map for " + pollutant_type + " Pollutant")

        # Create the plot legend based on the unique time in the dataset
        for i in range(len(unique_time)):
            colour_number += 1
            time.append(unique_time[i])
            colours.append("C" + str(colour_number))

        colours_legend = dict(zip(time, colours))
        labels = list(colours_legend.keys())
        handles = [plt.Rectangle((0, 0), 1, 1, color=colours_legend[label]) for label in labels]
        plt.legend(handles, labels)

        for i in range(0, len(visual_city)):
            measurements = []
            # Get the row of the data based on the value of the city
            city_data = data.loc[data['city'] == visual_city[i]].reset_index(drop=True)

            # Get the latitude and longitude of the data
            latitude = city_data['latitude'].iloc[0]
            longitude = city_data['longitude'].iloc[0]

            # Make the value of the data to be in correct position as the unique time used
            for j in unique_time:
                for time in city_data['Time']:
                    if time != j:
                        measurements.append(0)
                    else:
                        values = city_data[city_data['Time'] == j]
                        measurements_data = values['measurements_value'].values
                        measurements.append(float(measurements_data))

            if all(num == 0 for num in measurements) and len(measurements) > 0:
                continue

            # Plot the pie chart on the world map
            ax_pie = inset_axes(ax, width=0.6, height=0.4, loc=10, bbox_to_anchor=(longitude, latitude),
                                bbox_transform=ax.transData)

            ax_pie.pie(measurements, colors=colours)
            ax_pie.set_axis_off()

        plt.show()

    # Create the graph that will be shown when clicked on enhanced map
    def pop_up_graph(self):
        """
        A function that creates the bar graph on the unique country for the enhanced pop-up map.
        :return: A dataframe of html file for the enhanced map
        """
        # Get the name of unique country in an array
        unique_country = self.live_data.all_live_dataset['country_name_en'].unique()

        # Loop through the number of unique country
        for a in range(0, len(unique_country)):
            # Get the row of data based on the value of the country
            enhanced_data = self.live_data.all_live_dataset.loc[
                self.live_data.all_live_dataset['country_name_en'] == unique_country[a]].reset_index(drop=True)

            # Get the latitude and longitude of the data
            median_latitude = enhanced_data['latitude'].iloc[0]
            median_longitude = enhanced_data['longitude'].iloc[0]

            # Create figure
            fig = go.Figure()
            number_of_time = []

            # Get the air pollutant for the country
            parameters = enhanced_data['measurements_parameter'].unique()

            # Group the data based on the air pollutant, city and time, then get the average value of the data
            enhanced_data = enhanced_data.groupby(['city', 'measurements_parameter', 'Time']).mean(
                numeric_only=True).reset_index()

            # Loop through the number of air pollutant
            for i in range(0, len(parameters)):
                # Get the row of data based on the value of the air pollutant from the country dataset
                individual_data = enhanced_data.loc[
                    enhanced_data['measurements_parameter'] == parameters[i]].reset_index(drop=True)

                # Get the unique time from the dataset previously
                time_parameter = individual_data['Time'].unique()
                time_parameter = np.sort(time_parameter, axis=0)
                number_of_time.append(len(time_parameter))

                # Loop through the number of unique time
                for j in range(0, len(time_parameter)):
                    # Get the row of data based on the value of the time from the individual dataset
                    time_data = individual_data.loc[individual_data['Time'] == time_parameter[j]].reset_index(drop=True)

                    # Add the traces for the row of data using a bar chart
                    fig.add_trace(go.Bar(x=time_data['city'], y=time_data['measurements_value'], name=time_parameter[j],
                                         hovertemplate='City: %{x} <br>Value: %{y} <br>Country: ' + unique_country[a] +
                                                       '<br>Pollutant: ' + parameters[i] + '<br>' + 'Time: ' +
                                                       time_parameter[j]))

            minimum_total = 0
            maximum_total = 0

            # List of button that used to change the type of the air pollutant
            button_list = [dict(label='All', method='update',
                                args=[{'visible': True}, {'title': 'Pollutant Values for all types of pollutant'}])]

            # Loop through the number of air pollutant
            for i in range(0, len(parameters)):
                maximum_total += number_of_time[i]
                visible = [minimum_total <= k < maximum_total for k in list(range(0, sum(number_of_time)))]
                minimum_total += number_of_time[i]
                # Button that allows the user to change the view on the parameters
                button_list.append(dict(label=parameters[i], method='update',
                                        args=[{'visible': visible},
                                              {'title': 'Pollutant Values for ' + str(parameters[i])}]))

            # Set the plot title and axis label
            fig.update_xaxes(title_text=str(unique_country[a]) + ' Cities')
            fig.update_yaxes(title_text='Pollutant Values (µg/m³)')
            fig.update_layout(barmode='group', title='Pollutant Values for all types of pollutant', legend_title='Time',
                              updatemenus=[dict(active=0, buttons=button_list)])
            text = "fig" + str(a) + ".html"
            # Save the figure as html
            fig.write_html(self.path + "/" + text, config={'displayModeBar': False})

            # Put the list of data, country information into the pop_up_df
            self.pop_up_df.loc[len(self.pop_up_df)] = [unique_country[a], text, median_latitude, median_longitude]

    # Markers for each type basic map
    def input_Basic_Marker(self, header_name, folium_Map):
        """
        A function that input the pop-up into the map chosen.
        :param header_name: The type of air pollutant the user want to visualise
        :param folium_Map: The map that want the pop-up to be inputted
        :return: A folium map that has all the pop-up inputted based on the pollutant chosen
        """
        # Split data into variable based on header_name of pollutant
        data = self.live_data.split_data_based_on_pollutant(self.live_data.live_dataset, header_name)

        # Markers for pollutant based on header_name
        for i in range(0, len(data)):
            folium.Marker(
                # coordinates for the marker
                location=[data['latitude'][i], data['longitude'][i]],
                tooltip=(
                    "Value: {value} {unit}<br>"
                    "Country: {country}<br>"
                    "City: {city}<br>"
                    "Latitude: {latitude}<br>"
                    "Longitude: {longitude}<br>"
                ).format(value=data['measurements_value'][i],
                         unit=data['measurements_unit'][i],
                         country=data['country_name_en'][i],
                         city=data['city'][i],
                         latitude=data['latitude'][i],
                         longitude=data['longitude'][i],
                         ),  # hover label for the marker
                icon=folium.Icon(icon='info-sign')
            ).add_to(folium_Map)

    def input_Enhanced_Marker(self, folium_Map):
        """
        A function that input the html bar graph pop-up into the enhanced map.
        :param folium_Map: The map that want the pop-up to be inputted
        :return: A folium map that has all the pop-up inputted
        """
        # Loop through all the pop_up dataframe for enhanced map and put them in Enhanced map pop-up
        for i in range(0, len(self.pop_up_df)):
            html = """
            <iframe src=\"""" + "EnhancedLiveMapPopUp/" + self.pop_up_df['html_file'][i] + """\" width="1000" height="750"  frameborder="0">    
            """
            popup = folium.Popup(folium.Html(html, script=True))
            folium.Marker([self.pop_up_df['Latitude'].iloc[i], self.pop_up_df['Longitude'].iloc[i]],
                          popup=popup, icon=folium.Icon(icon='home', prefix='fa')).add_to(folium_Map)

    def display_Map(self, filename):
        """
        A function that view the map.
        :param filename: The name of the file the user want to visualise
        :return: A HTML file based on the filename to view
        """
        webbrowser.open(self.live_path + "/" + filename)

    def save_Map(self, map_name, filename):
        """
        A function that save the map as HTML.
        :param map_name: The pop-up map that want to be saved
        :param filename: The name of the file to be saved
        :return: A HTML file that is saved to the computer
        """
        map_name.save(self.live_path + "/" + filename)

    def create_Map(self):
        """
        A function that creates the pop-up maps.
        :return: All the pop-up maps as HTML files
        """
        pollutant_name = ['PM2.5', 'PM10', 'O3', 'NO2', 'SO2', 'CO', 'BC']
        location = []

        for i in range(0, 7):
            # Rearrange the dataset based on the type of pollutant
            data = self.live_data.split_data_based_on_pollutant(self.live_data.live_dataset, pollutant_name[i])
            self.dataset_in_pollutant_order = pd.concat([self.dataset_in_pollutant_order, data], ignore_index=True,
                                                        sort=False)
            # Get the average location from the type of pollutant
            pollutant_location = [data['latitude'].iloc[0], data['longitude'].iloc[0]]
            location = location + pollutant_location

        # Display the map
        if location[0] and location[1] is not np.nan:
            map_PM2 = folium.Map(location=(location[0], location[1]), tiles="openstreetmap", min_zoom=2)
            self.input_Basic_Marker('PM2.5', map_PM2)
            self.save_Map(map_PM2, "PM2_dot_5.html")

        if location[2] and location[3] is not np.nan:
            map_PM10 = folium.Map(location=(location[2], location[3]), tiles="openstreetmap", min_zoom=2)
            self.input_Basic_Marker('PM10', map_PM10)
            self.save_Map(map_PM10, "PM10.html")

        if location[4] and location[5] is not np.nan:
            map_O3 = folium.Map(location=(location[4], location[5]), tiles="openstreetmap", min_zoom=2)
            self.input_Basic_Marker('O3', map_O3)
            self.save_Map(map_O3, "O3.html")

        if location[6] and location[7] is not np.nan:
            map_NO2 = folium.Map(location=(location[6], location[7]), tiles="openstreetmap", min_zoom=2)
            self.input_Basic_Marker('NO2', map_NO2)
            self.save_Map(map_NO2, "NO2.html")

        if location[8] and location[9] is not np.nan:
            map_SO2 = folium.Map(location=(location[8], location[9]), tiles="openstreetmap", min_zoom=2)
            self.input_Basic_Marker('SO2', map_SO2)
            self.save_Map(map_SO2, "SO2.html")

        if location[10] and location[11] is not np.nan:
            map_CO = folium.Map(location=(location[10], location[11]), tiles="openstreetmap", min_zoom=2)
            self.input_Basic_Marker('CO', map_CO)
            self.save_Map(map_CO, "CO.html")

        if location[12] and location[13] is not np.nan:
            map_BC = folium.Map(location=(location[12], location[13]), tiles="openstreetmap", min_zoom=2)
            self.input_Basic_Marker('BC', map_BC)
            self.save_Map(map_BC, "BC.html")

        if self.pop_up_df['Latitude'][0] and self.pop_up_df['Longitude'][0] is not np.nan:
            map_enhanced = folium.Map(location=(self.pop_up_df['Latitude'][0], self.pop_up_df['Longitude'][0]),
                                           tiles="openstreetmap", min_zoom=2)
            self.input_Enhanced_Marker(map_enhanced)
            self.save_Map(map_enhanced, "Enhanced.html")

    def create_Folder(self, directory_name, another):
        """
        A function that is used to create a folder in the user's computer.
        :param directory_name: The name of the created folder
        :param another: Check if the software need to create an inner folder
        :return: Creates the folder and return the path of the folder
        """
        new_directory = directory_name  # New folder name
        current_path = os.path.dirname(os.getcwd())  # Get current file path

        if another:
            self.live_path = os.path.join(current_path, new_directory)

            # Create new folder
            if not os.path.exists(self.live_path):
                os.mkdir(self.live_path)
        else:
            path = os.path.join(current_path, new_directory)

            # Create new folder
            if not os.path.exists(path):
                os.mkdir(path)

            return path

        # Create new folder
        if not os.path.exists(self.live_path):
            os.mkdir(self.live_path)

        if another:
            # Create another folder to store enhanced vis
            new_directory = "EnhancedLiveMapPopUp"  # New folder name
            self.path = os.path.join(self.live_path, new_directory)

            # Create new folder
            if not os.path.exists(self.path):
                os.mkdir(self.path)


if __name__ == '__main__':
    live_Data = LiveDataVisualisation()

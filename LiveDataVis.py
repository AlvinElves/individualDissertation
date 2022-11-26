import os
import folium
import webbrowser

import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from LiveData import *


class LiveDataVisualisation:
    def __init__(self):
        self.map_SO2 = None
        self.map_NO2 = None
        self.map_BC = None
        self.map_CO = None
        self.map_O3 = None
        self.map_PM10 = None
        self.map_PM2_dot_5 = None
        self.map_enhanced = None
        self.path = None
        self.live_path = None
        self.dataset_in_pollutant_order = pd.DataFrame()
        self.pop_up_df = pd.DataFrame(columns=['City', 'html_file', 'Latitude', 'Longitude'])

        live_data = LiveData()

        self.createFolder()

        self.pop_up_graph(live_data)
        self.createMap(live_data)

        self.inputBasicMarker(live_data, 'PM2.5', self.map_PM2_dot_5)
        self.inputBasicMarker(live_data, 'PM10', self.map_PM10)
        self.inputBasicMarker(live_data, 'O3', self.map_O3)
        self.inputBasicMarker(live_data, 'NO2', self.map_NO2)
        self.inputBasicMarker(live_data, 'SO2', self.map_SO2)
        self.inputBasicMarker(live_data, 'CO', self.map_CO)
        self.inputBasicMarker(live_data, 'BC', self.map_BC)

        self.inputEnhancedMarker(self.map_enhanced)

        self.saveMap()

    # Create the graph that will be shown when clicked on enhanced map
    def pop_up_graph(self, live_data):
        # Get the name of unique country in an array
        unique_country = live_data.all_live_dataset['country_name_en'].unique()

        for a in range(0, len(unique_country)):
            enhanced_data = live_data.all_live_dataset.loc[live_data.all_live_dataset['country_name_en'] == unique_country[a]].reset_index(drop=True)
            median_latitude = enhanced_data['latitude'].median()
            median_longitude = enhanced_data['longitude'].median()

            fig = go.Figure()
            number_of_time = []
            parameters = enhanced_data['measurements_parameter'].unique()
            enhanced_data = enhanced_data.groupby(['city', 'measurements_parameter', 'Time']).mean(numeric_only=True).reset_index()
            for i in range(0, len(parameters)):
                individual_data = enhanced_data.loc[enhanced_data['measurements_parameter'] == parameters[i]].reset_index(drop=True)
                time_parameter = individual_data['Time'].unique()
                time_parameter = np.sort(time_parameter, axis=0)
                number_of_time.append(len(time_parameter))

                for j in range(0, len(time_parameter)):
                    time_data = individual_data.loc[individual_data['Time'] == time_parameter[j]].reset_index(drop=True)
                    fig.add_trace(go.Bar(x=time_data['city'], y=time_data['measurements_value'], name=time_parameter[j]))

            minimum_total = 0
            maximum_total = 0
            button_list = [dict(label='All', method='update',
                                args=[{'visible': True}, {'title': 'Pollutant Values for all types of pollutant'}])]
            for i in range(0, len(parameters)):
                maximum_total += number_of_time[i]
                visible = [minimum_total <= k < maximum_total for k in list(range(0, sum(number_of_time)))]
                minimum_total += number_of_time[i]
                button_list.append(dict(label=parameters[i], method='update',
                                        args=[{'visible': visible}, {'title': 'Pollutant Values for ' + str(parameters[i])}]))
            fig.update_traces(hovertemplate='City: %{x} <br>Value: %{y}')
            fig.update_xaxes(title_text=str(unique_country[a]) + ' Cities')
            fig.update_yaxes(title_text='Pollutant Values (µg/m³)')
            fig.update_layout(barmode='group', title='Pollutant Values for all types of pollutant', legend_title='Time',
                              updatemenus=[dict(active=0, buttons=button_list)])
            text = "fig" + str(a) + ".html"
            fig.write_html(self.path + "/" + text)

            self.pop_up_df.loc[len(self.pop_up_df)] = [unique_country[a], text, median_latitude, median_longitude]

    @staticmethod
    def inputBasicMarker(live_data, header_name, folium_Map):
        # Split data into variable based on header_name of pollutant
        data = live_data.split_data_based_on_pollutant(header_name)

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

    def inputEnhancedMarker(self, folium_Map):
        for i in range(0, len(self.pop_up_df)):
            html = """
            <iframe src=\"""" + "EnhancedLiveMapPopUp/" + self.pop_up_df['html_file'][i] + """\" width="1000" height="750"  frameborder="0">    
            """
            popup = folium.Popup(folium.Html(html, script=True))
            folium.Marker([self.pop_up_df['Latitude'].iloc[i], self.pop_up_df['Longitude'].iloc[i]],
                          popup=popup, icon=folium.Icon(icon='home', prefix='fa')).add_to(folium_Map)

    def displayMap(self, filename):
        webbrowser.open(self.live_path + "/" + filename)

    def saveMap(self):
        self.map_PM2_dot_5.save(self.live_path + "/" + "PM2_dot_5.html")
        self.map_PM10.save(self.live_path + "/" + "PM10.html")
        self.map_CO.save(self.live_path + "/" + "CO.html")
        self.map_BC.save(self.live_path + "/" + "BC.html")
        self.map_O3.save(self.live_path + "/" + "O3.html")
        self.map_NO2.save(self.live_path + "/" + "NO2.html")
        self.map_SO2.save(self.live_path + "/" + "SO2.html")
        self.map_enhanced.save(self.live_path + "/" + "Enhanced.html")

    def createMap(self, live_data):
        pollutant_name = ['PM2.5', 'PM10', 'O3', 'NO2', 'SO2', 'CO', 'BC']
        location = []

        for i in range(0, 7):
            # Rearrange the dataset based on the type of pollutant
            data = live_data.split_data_based_on_pollutant(pollutant_name[i])
            self.dataset_in_pollutant_order = pd.concat([self.dataset_in_pollutant_order, data], ignore_index=True,
                                                        sort=False)

            # Get the average location from the type of pollutant
            pollutant_location = [data['latitude'].median(), data['longitude'].median()]
            location = location + pollutant_location

        # Display the map
        self.map_PM2_dot_5 = folium.Map(location=(location[0], location[1]), tiles="openstreetmap", min_zoom=2)
        self.map_PM10 = folium.Map(location=(location[2], location[3]), tiles="openstreetmap", min_zoom=2)
        self.map_O3 = folium.Map(location=(location[4], location[5]), tiles="openstreetmap", min_zoom=2)
        self.map_NO2 = folium.Map(location=(location[6], location[7]), tiles="openstreetmap", min_zoom=2)
        self.map_SO2 = folium.Map(location=(location[8], location[9]), tiles="openstreetmap", min_zoom=2)
        self.map_CO = folium.Map(location=(location[10], location[11]), tiles="openstreetmap", min_zoom=2)
        self.map_BC = folium.Map(location=(location[12], location[13]), tiles="openstreetmap", min_zoom=2)
        self.map_enhanced = folium.Map(location=(self.pop_up_df['Latitude'][0], self.pop_up_df['Longitude'][0]),
                                       tiles="openstreetmap", min_zoom=2)

    def createFolder(self):
        new_directory = "LiveMapHTML"  # New folder name
        current_path = os.getcwd()  # Get current file path
        self.live_path = os.path.join(current_path, new_directory)

        # Create new folder
        if not os.path.exists(self.live_path):
            os.mkdir(self.live_path)

        # Create another folder to store enhanced vis
        new_directory = "EnhancedLiveMapPopUp"  # New folder name
        self.path = os.path.join(self.live_path, new_directory)

        # Create new folder
        if not os.path.exists(self.path):
            os.mkdir(self.path)


if __name__ == '__main__':
    live_Data = LiveDataVisualisation()

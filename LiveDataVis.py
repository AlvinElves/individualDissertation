import os
import folium
import webbrowser
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
        self.path = None
        self.dataset_in_pollutant_order = pd.DataFrame()

        live_data = LiveData()

        self.createFolder()
        self.createMap(live_data)

        self.inputMarker(live_data, 'PM2.5', self.map_PM2_dot_5)
        self.inputMarker(live_data, 'PM10', self.map_PM10)
        self.inputMarker(live_data, 'O3', self.map_O3)
        self.inputMarker(live_data, 'NO2', self.map_NO2)
        self.inputMarker(live_data, 'SO2', self.map_SO2)
        self.inputMarker(live_data, 'CO', self.map_CO)
        self.inputMarker(live_data, 'BC', self.map_BC)

        self.saveMap()
        self.displayMap('BC.html')

    @staticmethod
    def inputMarker(live_data, header_name, folium_Map):
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

    def displayMap(self, filename):
        webbrowser.open(self.path + "/" + filename)

    def saveMap(self):
        self.map_PM2_dot_5.save(self.path + "/" + "PM2_dot_5.html")
        self.map_PM10.save(self.path + "/" + "PM10.html")
        self.map_CO.save(self.path + "/" + "CO.html")
        self.map_BC.save(self.path + "/" + "BC.html")
        self.map_O3.save(self.path + "/" + "O3.html")
        self.map_NO2.save(self.path + "/" + "NO2.html")
        self.map_SO2.save(self.path + "/" + "SO2.html")

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

    def createFolder(self):
        new_directory = "LiveMapHTML"  # New folder name
        current_path = os.getcwd()  # Get current file path
        self.path = os.path.join(current_path, new_directory)

        # Create new folder
        if not os.path.exists(self.path):
            os.mkdir(self.path)


if __name__ == '__main__':
    live_Data = LiveDataVisualisation()

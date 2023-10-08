import matplotlib.pyplot as plt
import requests
from matplotlib.animation import FuncAnimation

#-----LOCATION INFORMATION-----
API_KEY = 'd06a98ce19472ba94a76d6d111e16d4d' #This api key will be deleted later, you can use it now to test data acquisition
#city = 'guarulhos'
lat = -23.453761327559913
lon = -46.53051244930775
link = f'http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={API_KEY}'
#------------------------------

y = []

# Function to take a new no2 concentration reading every 10 minutes
def generate_new_data(i):

    request = requests.get(link)
    request_json = request.json()
    no2 = request_json['list'][0]['components']['no2']
    y.append(no2)
    
    # Keep only the last 10 data to keep the graph of fixed size
    if len(y) > 10:
        y.clear()

        '''
            Here we will define an action for the player to take based on 
            the data collected from their neighborhood

            medium_no2 = sum(y)/10
            if medium_no2 > 10:
                the player must take action to improve the humidity levels
            
        '''  
    
    plt.clf()  
    plt.bar(range(1, len(y) + 1), no2)
    plt.xlabel('Sample')
    plt.ylabel('NO2 (ug/m³)')
    plt.title('NO2 Air Concentration - Maia, Guarulhos - SP')
    plt.tight_layout()

    for x, z in enumerate(y):
        plt.annotate(str(f'{z}ug/m³'), (x + 1, z), ha='center', va='bottom')

# Cria a figura e o eixo do gráfico
fig, ax = plt.subplots()

#Create the animation that calls the function generate_new_data every 10 minutes
ani = FuncAnimation(fig, generate_new_data, interval=3000)

plt.show()


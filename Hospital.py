import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Temperature_C": [110, 115, 118, 120, 122, 125, 128, 130, 132, 135],
    "Pressure_bar": [1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.5, 2.8, 3.0, 3.2],
    "Time_min": [10, 12, 15, 18, 20, 22, 25, 28, 30, 35],
    "Energy_kWh": [1.5, 1.7, 1.9, 2.1, 2.4, 2.8, 3.2, 3.6, 3.9, 4.3],
    "Sterilization_Efficiency_percent": [70, 75, 80, 85, 88, 92, 95, 97, 98, 99]
}

df=pd.DataFrame(data)
print(df)

df['Efficiency_per_Energy']=df[ "Sterilization_Efficiency_percent"] /df["Energy_kWh"]
print(df)

print(df.corr())

plt.scatter(df["Temperature_C"],df["Pressure_bar"])
plt.xlabel("Temperature_C")
plt.ylabel( "Pressure_bar")
plt.title('Temperature vs Pressure in Autoclave')
plt.figure()

plt.scatter(df["Temperature_C"],df["Sterilization_Efficiency_percent"])
plt.xlabel("Temperature_C")
plt.ylabel("Sterilization_Efficiency_percent")
plt.title('Temperature vs Sterilization Efficiency')
plt.figure()

plt.scatter(df["Pressure_bar"],df["Sterilization_Efficiency_percent"])
plt.xlabel("Pressure_bar")
plt.ylabel("Sterilization_Efficiency_percent")
plt.title('Pressure vs Sterilization Efficiency')
plt.figure()

plt.scatter(df["Energy_kWh"],df["Sterilization_Efficiency_percent"])
plt.xlabel("Energy_kWh")
plt.ylabel("Sterilization_Efficiency_percent")
plt.title('Energy Consumption vs Sterilization Efficienncy')
plt.show()



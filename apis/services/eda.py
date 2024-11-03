from decouple import config

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

class cases_eda:

    name_dataset = None

    route_price_with_brand_max = None

    route_price_with_brand_min = None

    route_brand_sold = None

    def __init__(self):

        self.init_name_dataset()

        self.init_route_price_with_data_max()

        self.init_route_price_with_data_min()

        self.init_route_brand_sold()

    def init_route_brand_sold(self):

        self.route_brand_sold = config("ROUTE_EDA_BRAND_SOLD")

        return True
    
    def get_route_brand_sold(self):

        return self.route_brand_sold

    def init_route_price_with_data_min(self):

        self.route_price_with_brand_min = config("ROUTE_EDA_PRICE_WITH_BRAND_MIN")

        return True
    
    def get_route_price_with_data_min(self):

        return self.route_price_with_brand_min

    def init_route_price_with_data_max(self):

        self.route_price_with_brand_max = config("ROUTE_EDA_PRICE_WITH_BRAND_MAX")

        return True
    
    def get_route_price_with_data_max(self):

        return self.route_price_with_brand_max

    def init_name_dataset(self):

        self.name_dataset = config("NAME_DATASET")

        return True
    
    def get_name_dataset(self):

        return self.name_dataset
    
    def get_csv(self):

        return pd.read_csv(self.get_name_dataset())
    
    def check_most_sold_brand(self):

        df = self.get_csv()

        brand_counts = df['Manufacturer'].value_counts()

        print("Marca con más ventas:")

        print(brand_counts.head(1))

        print("\nTop 10 marcas más vendidas:")

        print(brand_counts.head(10))

        return True

    def check_price_max(self):

        df = self.get_csv()

        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

        df = df.dropna(subset=['Price'])

        df_sorted = df.sort_values(by='Price', ascending=False)

        print("Los 10 autos más caros son:")

        for index, row in df_sorted.head(10).iterrows():

            print(f"Marca: {row['Manufacturer']}, Precio: {row['Price']}, Modelo: {row['Model']}, Año: {row['Prod. year']}")

        return True
    
    def check_price_min(self):

        df = self.get_csv()

        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

        df = df.dropna(subset=['Price'])

        df_sorted = df.sort_values(by='Price', ascending=True)

        print("Los 10 autos más baratos son:")

        for index, row in df_sorted.head(10).iterrows():

            print(f"Marca: {row['Manufacturer']}, Precio: {row['Price']}, Modelo: {row['Model']}, Año: {row['Prod. year']}")

        return True

    def check_price_with_brand_max(self):

        df = self.get_csv()

        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

        df = df.dropna(subset=['Price'])

        df_sorted = df.sort_values(by='Price', ascending=False).head(10)

        plt.figure(figsize=(12, 6))

        sns.barplot(x='Manufacturer', y='Price', data=df_sorted)

        plt.title('Relación entre Precio y Marca de los 10 Vehículos más Caros')

        plt.xlabel('Marca')

        plt.ylabel('Precio')

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig(self.get_route_price_with_data_max())

        plt.close()

        return True
    
    def check_price_with_brand_min(self):

        df = self.get_csv()

        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

        df = df.dropna(subset=['Price'])

        df_sorted = df.sort_values(by='Price', ascending=True).head(10)

        plt.figure(figsize=(12, 6))

        sns.barplot(x='Manufacturer', y='Price', data=df_sorted)

        plt.title('Relación entre Precio y Marca de los 10 Vehículos más Baratos')

        plt.xlabel('Marca')

        plt.ylabel('Precio')

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig(self.get_route_price_with_data_min())  

        plt.close()  

        return True

    def check_most_sold_brands(self):

        df = self.get_csv()

        brand_counts = df['Manufacturer'].value_counts().head(10)  

        plt.figure(figsize=(10, 6))

        sns.barplot(x=brand_counts.values, y=brand_counts.index, palette='viridis')

        plt.title('Top 10 Marcas de Vehículos Más Vendidas', fontsize=16)

        plt.xlabel('Número de Vehículos Vendidos', fontsize=12)

        plt.ylabel('Marca', fontsize=12)

        plt.tight_layout()

        plt.savefig(self.get_route_brand_sold())  

        plt.close()

        return True

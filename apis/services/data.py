import pandas as pd
import pickle
from decouple import config
from sklearn.preprocessing import LabelEncoder
import re

class cases_data:

    name_dataset = None

    name_dataset_debug = None

    name_label_encoder = None

    column_to_remove = None

    label_encoder = None  

    def __init__(self):

        self.init_name_label_encoder()

        self.init_label_encoder()

        self.init_name_dataset()

        self.init_name_dataset_debug()

        self.init_column_to_remove()

    def init_label_encoder(self):

        self.label_encoder = LabelEncoder()

        return True

    def init_name_label_encoder(self):
        
        self.name_label_encoder = config("NAME_LABEL_ENCODER")

        return True

    def init_column_to_remove(self):

        self.column_to_remove = ['ID', 'Levy', 'Doors', 'Wheel', 'Color', 'Airbags']

        return True

    def init_name_dataset(self):

        self.name_dataset = config("NAME_DATASET")

        return True

    def init_name_dataset_debug(self):

        self.name_dataset_debug = config("DEBUG_NAME_DATASET")

        return True

    def get_columns(self, dataset):

        return dataset.columns

    def debug_dataset(self, dataset):

        cols_to_remove = [col for col in self.column_to_remove if col in dataset.columns]

        processed_df = dataset.drop(columns=cols_to_remove, errors='ignore')

        processed_df.columns = processed_df.columns.str.replace('"', '').str.strip()

        return processed_df

    def save_dataset(self, dataset):

        dataset.to_csv(self.name_dataset_debug, index=False)

        return True

    def apply_label_encoding(self, df):

        categorical_cols = df.select_dtypes(include=['object']).columns

        for col in categorical_cols:

            df[col] = self.label_encoder.fit_transform(df[col])

        return df

    def save_label_encoder(self):

        with open(self.name_label_encoder, 'wb') as f:

            pickle.dump(self.label_encoder, f)

        return True

    def load_label_encoder(self):

        with open(self.name_label_encoder, 'rb') as f:

            self.label_encoder = pickle.load(f)

        return True

    def load_csv(self):

        return pd.read_csv(self.name_dataset)

    def load_csv_debug(self):

        return pd.read_csv(self.name_dataset_debug)

    def check_cell_null(self, dataset):

        return dataset.isnull().sum()
    
    def debug_cvs_native(self):

        with open(self.name_dataset, 'r') as file:

            content = file.read()

            cleaned_content = re.sub(r'[^A-Za-z0-9,._\n]', '', content)

        with open(self.name_dataset, 'w') as file:

            file.write(cleaned_content)

    def clasificar_edad(self,edad):

        if edad < 30:

            return "Baja"
        
        elif edad <= 50:

            return "Media"
        
        else:

            return "Alta"

    def generate_number_person(self,df):

        return len(df)
    
    def generate_number_profesionals(self,df):

        return df['Profesin'].nunique()
    
    def generate_persona_for_profesion(self,df):

        return df['Profesin'].value_counts()
    
    def generate_age_for_profession(self,df):

        return df.groupby('Profesin')['Edad'].mean()
    
    def generate_abogados_menores(self,df):

        return df[(df['Profesin'] == 'Abogado') & (df['Edad'] < 30)].shape[0]
    
    def add_dataframe_rango_edad(self,df):

        return df['Edad'].apply(self.clasificar_edad)

    def check_data(self):

        self.debug_cvs_native()

        df = self.load_csv()

        print("////////////////////////////////////////////////// COLUMNS")

        print(df.columns)

        print("////////////////////////////////////////////////// HEAD")

        print(df.head(20)) 

        print("////////////////////////////////////////////////// ASKS")
        
        print("Número total de personas:", self.generate_number_person(df))
        
        print("Número de profesiones únicas:", self.generate_number_profesionals(df))
        
        print("Personas por profesión:\n", self.generate_persona_for_profesion(df))
        
        print("Edad promedio por profesión:\n", self.generate_age_for_profession(df))
    
        print("Abogados menores de 30 años:", self.generate_abogados_menores(df))

        print("Incorporación rango de edad:")

        df['rango_edad'] = self.add_dataframe_rango_edad(df)
        
        print(df)

        print("////////////////////////////////////////////////// END")

        return True

import pandas as pd

import pickle

from decouple import config

from sklearn.preprocessing import LabelEncoder

class cases_data:

    name_dataset = None

    name_dataset_debug = None

    name_label_encoder = None

    column_to_remove = None

    label_encoder = None  

    def __init__(self):

        self.init_name_label_encoder()

    def generate_dataframe(self,data):

        return pd.DataFrame([data])

    def init_label_encoder(self):

        self.label_encoder = LabelEncoder()

    def init_name_label_encoder(self):

        self.name_label_encoder = config("NAME_LABEL_ENCODER")

        return True
    
    def get_name_label_encoder(self):

        return self.name_label_encoder

    def init_name_dataset_debug(self):

        self.name_dataset_debug = config("DEBUG_NAME_DATASET")

        return True
    
    def get_name_dataset_debug(self):

        return self.name_dataset_debug

    def init_column_to_remove(self):

        self.column_to_remove = ['ID', 'Levy', 'Doors', 'Wheel', 'Color', 'Airbags']

        return True

    def get_column_to_remove(self):

        return self.column_to_remove

    def init_name_dataset(self):

        self.name_dataset = config("NAME_DATASET")

    def get_name_dataset(self):

        return self.name_dataset
    
    def check_cell_null(self, dataset):

        return dataset.isnull().sum()
    
    def get_columns(self, dataset):

        return dataset.columns
    
    def debug_dataset(self, dataset):

        self.init_column_to_remove()

        return dataset.drop(columns=self.get_column_to_remove())
    
    def save_dataset(self, dataset):

        self.init_name_dataset_debug()

        dataset.to_csv(self.get_name_dataset_debug(), index=False)

        return True

    def apply_label_encoding(self, df):

        categorical_cols = df.select_dtypes(include=['object']).columns

        for col in categorical_cols:

            df[col] = self.label_encoder.fit_transform(df[col])

        return df

    def save_label_encoder(self):

        with open(self.get_name_label_encoder(), 'wb') as f:

            pickle.dump(self.label_encoder, f)

        return True

    def load_label_encoder(self):

        with open(self.get_name_label_encoder(), 'rb') as f:

            self.label_encoder = pickle.load(f)

        return True
    
    def load_csv(self):

        self.init_name_dataset()

        return pd.read_csv(self.get_name_dataset())
    
    def load_csv_debug(self):

        self.init_name_dataset_debug()

        return pd.read_csv(self.get_name_dataset_debug())

    def check_data(self):

        self.init_label_encoder()

        self.init_name_dataset()

        df = pd.read_csv(self.get_name_dataset())

        print(df.head())

        print(self.check_cell_null(df))

        print(self.get_columns(df))

        processed_df = self.apply_label_encoding(self.debug_dataset(df))

        self.save_dataset(processed_df)

        self.save_label_encoder()

        return True

import pandas as pd
from decouple import config

class cases_eda:
    
    name_dataset = None

    def __init__(self):

        self.init_name_dataset()

    def init_name_dataset(self):

        self.name_dataset = config("DEBUG_NAME_DATASET")

    def get_name_dataset(self):
        return self.name_dataset

    def get_csv(self):

        df = pd.read_csv(self.get_name_dataset(), delimiter=',')

        return df

    def check_status_account_with_gender(self):

        df = self.get_csv()

        gender_attrition_counts = df.groupby(['Gender', 'Attrition_Flag']).size().unstack()
        print(gender_attrition_counts)
        
        return True

import os
import numpy as np 			        # linear algebra
import pandas as pd 			    # data processing
import random
import matplotlib.pyplot as plt		# visualization
from sklearn import datasets


class Function():
    def __init__(self, file_name='iris.csv'):
        self.file_name = file_name
        self.data = datasets.load_iris()
        self.working_dir = os.path.join(os.getcwd().split('Datacademy')[0], "Datacademy", "Modules", "M4_ML", "src")
        self.data_dir = os.path.join(os.getcwd().split('Datacademy')[0], "Datacademy", "data", "M4_ML")
        self.database_location = os.path.join(self.working_dir, self.file_name)

        self.iris = self.data_modification()


    def data_modification(self):
        """ Create a modified DataFrame for the iris dataset """
        # Transform to Pandas DataFrame
        iris = pd.DataFrame(data=self.data.data, columns=self.data.feature_names)
        
        # Create NaN values (missing values) in petal width
        none_values = [random.randint(0, 149) for _ in range(5)]
        iris.loc[none_values, 'petal length (cm)'] = None

        # Add additional column for categorical features
        iris['state'] = np.random.choice(['wet', 'dry'], iris.shape[0])

        # Transform one column its measure unit
        iris = iris.rename(columns={'sepal width (cm)':'sepal width (mm)'})
        iris['sepal width (mm)'] = iris['sepal width (mm)'].apply(lambda x: x*10)

        # Add outlier to the DataFrame
        index_val = 72
        value = iris.loc[index_val, 'sepal length (cm)']
        new_value = float(str(value).split('.')[0] + '0.' + str(value).split('.')[-1])
        iris.loc[index_val, 'sepal length (cm)'] = new_value

        return iris

    def remove_0_in_outlier(self, outlier_value):
        # Verwijder de 0 in de outlier value en update the DataFrame
        location_outlr = self.iris[self.iris['sepal length (cm)'] == outlier_value].index[0]

        # get index of first occurrence of '0'
        id = str(outlier_value).index('0')

        # remove the first occurrence of '0'
        new_value = float(str(outlier_value)[:id] + str(outlier_value)[id+1:])

        # Append the new value to the DataFrame
        self.iris.loc[location_outlr, 'SepalLengthCm'] = new_value


    def supervised_dataset(self):
        iris = pd.DataFrame(data=self.data.data, columns=self.data.feature_names)
        iris['target'] = self.data.target.tolist()


    def unsupervised_dataset(self):
        pass


    def execute_function(self, exercise:str=None, save_output:bool=True):
        if save_output:
            if not os.path.exists(os.path.join(self.data_dir, "answers")):
                os.mkdir(os.path.join(self.data_dir, "answers"))
            if exercise is None:
                return "Please provide the exercise name in the function if you want to save the outputs."
            self.data.to_csv(os.path.join(self.data_dir, "answers", f"{exercise}.csv"), sep=";", index=False)
        return self.data

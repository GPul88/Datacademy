import os
from sklearn import datasets
import pandas as pd

class ReviewFunction:
    def __init__(self):
        self.working_dir = os.path.join(os.getcwd().split('Datacademy')[0], "Datacademy", "Modules", "M2_PCC", "src")
        self.data_dir = os.path.join(os.getcwd().split('Datacademy')[0], "Datacademy", "data", "M2_PCC")

        self.data = datasets.load_diabetes()
        self.n_features = self.data.data.shape[1]
        self.input_columns = ['column_' + str(i) for i in range(self.n_features)]
        self.pandas_data = pd.DataFrame(self.data.data, columns=self.input_columns)

    def check_answer(self, answer, exercise):
        if exercise[0] == "B":
            self.check_B(answer, exercise)
        elif exercise[0] == "C":
            self.check_C(answer, exercise)
        elif exercise[0] == "D":
            self.check_D(answer, exercise)
        else:
            print("You didn't specify the correct exercise.")

    def check_B(self, ans, ex):
        if ex[1] == "1":
            if ans < 70.66:
                return "Incorrect, a Boeing 747-100 is larger."
            elif ans > 70.66:
                return "Incorrect, a Boeing 747-100 is smaller."
            else:
                return "Correct! A Boeing 747-100 is indeed 70.66 meters."
        
        if ex[1] == "2":
            if ans < 146.7:
                return "Incorrect, an Iphone 12 is larger."
            elif ans > 146.7:
                return "Incorrect, an Iphone 12 is smaller."
            else:
                return "Correct! An Iphone 12 is indeed 146.7 millimeters."
        
        if ex[1] == "3":
            if ans == True:
                return "Correct! The more you know!"
            else:
                return "Incorrect! You might want to check your math once more"

        

        if ex[1] in ["1", "2"]:
            if type(ans) == float:
                if 50 < ans < 150:
                    print("This is indeed the correct size.")
                else:
                    print("This is NOT the correct size.")
            else:
                print("This is not a float value.")
        else:
            if ans or ans == "No":
                print("You're indeed correct.")
            else:
                print("Oops, you're wrong.")

    def check_C(self, ans, ex):
        pass

    def check_D(self, ans, ex):
        pass
import os


class ReviewFunction:
    def __init__(self):
        self.working_dir = os.path.join(os.getcwd().split('Datacademy')[0], "Datacademy", "Modules", "M2_PCC", "src")
        self.data_dir = os.path.join(os.getcwd().split('Datacademy')[0], "Datacademy", "data", "M2_PCC")

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
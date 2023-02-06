import os
import pandas as pd

answers_dir = "./Modules/M08_CICD/answers"

exercises = [f for f in os.listdir(answers_dir) if ".csv" in f]
exercises.sort()

answers_dict = {}

for exercise in exercises:
    exercise_df = pd.read_csv(os.path.join(answers_dir, exercise), sep=";") 
    exercise_name = f"A_{exercise.split('.')[0]}"
    answers_dict[exercise_name] = exercise_df


def test_helloname():
    ans = answers_dict["A_1"]

    assert ans.answer[0] != None, "The name can't be empty"


def test_addnum():
    ans = answers_dict["A_2"]

    assert ans.answer[0] == ans.a[0]+ans.b[0], \
        f"The sum of {ans.a[0]}+{ans.b[0]} should be {ans.a[0]+ans.b[0]}"


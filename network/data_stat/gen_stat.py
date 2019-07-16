import json
import numpy
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

# DONE
def count_in_guess():
    latnums = numpy.empty(7)
    for i in range(7):
        latnums[i] = len(open("../nn_model/data/crystal_{}_list.txt".format(i)).readlines())
    return latnums


# DONE
def count_in_theory():
    crystals = numpy.zeros(7)
    for i in range(7):
        with open("../nn_model/data/crystal_{}_list.txt".format(i), "r") as list_file:
            for data_file_path in list_file:
                with open("../nn_model/" + data_file_path.split()[0], "r") as data_file:
                    data_json = json.load(data_file)

                    for c, margin in enumerate([2, 15, 74, 142, 167, 194, 230]):
                        if data_json["number"] <= margin:
                            crystals[c] += 1
                            break
    return crystals


def crystal_number(sgnum: int):
    for c, margin in enumerate([2, 15, 74, 142, 167, 194, 230]):
        if sgnum <= margin:
            return c


def correct_in_guess(plot=False):
    corrects = numpy.zeros(7)
    error_dict = {}
    for i in range(7):
        error_list = []
        with open("../nn_model/data/crystal_{}_list.txt".format(i), "r") as list_file:
            for data_file_path in list_file:
                with open("../nn_model/" + data_file_path.split()[0], "r") as data_file:
                    data_json = json.load(data_file)
                    sg_num = crystal_number(data_json["number"])
                    if sg_num == i:
                        corrects[i] += 1
                    #
                    else:
                        error_list.append([data_file_path.split()[0], sg_num, i])

            error_dict["crystal_{}".format(i)] = error_list
    with open("error_list.json", 'w') as sum_f:
        json.dump(error_dict, sum_f, indent=2)

    if plot is True:
        numpy.set_printoptions(suppress=True)
        confusion_matrix = numpy.zeros([7, 7])
        plt.figure()
        for i in range(7):
            stat = error_dict["crystal_{}".format(i)]
            for j in range(len(stat)):
                index = stat[j][1]
                confusion_matrix[i][index] += 1

        # Added corrects
        for i in range(7):
            confusion_matrix[i][i] = corrects[i]

        df_cm = pd.DataFrame(confusion_matrix, index=[i for i in "1234567"],
                             columns=[i for i in "1234567"])
        plt.figure(figsize=(10, 7))
        sn.heatmap(df_cm, annot=True, cmap="YlGnBu", fmt='g')
        plt.show()
    return corrects


guess_count = count_in_guess()
theory_count = count_in_theory()
guess_correct = correct_in_guess(plot=True)
print("guess count: ", guess_count, guess_count.sum())
print("theory count: ", theory_count, theory_count.sum())
print("guess correct: ", guess_correct, guess_correct.sum())

print("correct percentage: ", (1 - (guess_count - guess_correct).sum()/guess_count.sum())*100)

print(guess_count - guess_correct)
print(theory_count - guess_correct)

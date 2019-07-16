import numpy


def total_count(group_numbers, list_dir, list_format):
    counts = numpy.zeros(len(group_numbers)).astype(int)
    for i, index in enumerate(group_numbers):
        counts[i] = len(open(list_dir + list_format.format(index)).readlines())
    return counts


def correct_count(group_numbers, guess_list_dir, actual_list_dir, list_format):
    counts = numpy.zeros(len(group_numbers)).astype(int)
    for i, index in enumerate(group_numbers):
        with open(guess_list_dir + list_format.format(index), "r") as list_file:
            guesses = set([line.split("/")[-1] for line in list_file.readlines()])
        with open(actual_list_dir + list_format.format(index), "r") as list_file:
            actuals = set([line.split("/")[-1] for line in list_file.readlines()])
        counts[i] = len(set.intersection(guesses, actuals))
    return counts


def crystal_number(sgnum: int):
    for c, margin in enumerate([2, 15, 74, 142, 167, 194, 230]):
        if sgnum <= margin:
            return c


def sg_cm_plt(data_dir):
    error_dict = {}
    corrects = numpy.zeros(230)
    # create error_list.json
    import json
    for i in range(230):
        error_list = []
        with open("data/guess/spacegroup_list_{}.txt".format(i + 1), "r") as list_file:
            for data_file_path in list_file:
                with open(data_file_path.split()[0], "r") as data_file:
                    data_json = json.load(data_file)
                    sg_num = data_json["number"]
                    if sg_num == i:
                        corrects[i] += 1
                    #
                    else:
                        error_list.append([data_file_path.split()[0], sg_num, i + 1])

            error_dict["spacegroup_{}".format(i + 1)] = error_list
    with open("error_sg_list.json", 'w') as sum_f:
        json.dump(error_dict, sum_f, indent=2)
    # plot confusion matrix
    import seaborn as sn
    import pandas as pd
    import matplotlib.pyplot as plt

    numpy.set_printoptions(suppress=True)
    confusion_matrix = numpy.zeros([230, 230])
    plt.figure()
    for i in range(230):
        stat = error_dict['spacegroup_{}'.format(i + 1)]
        for j in range(len(stat)):
            index = stat[j][1]
            confusion_matrix[i][index] += 1

    # Added corrects
    for i in range(230):
        confusion_matrix[i][i] = corrects[i]

    # guess_total = [sum(confusion_matrix[i]) for i in range(230)]
    # cm_normalized = [confusion_matrix[i]/guess_total[i] for i in range(230)]

    df_cm = pd.DataFrame(confusion_matrix)
    # plt.rc('xtick', labelsize=20)
    # plt.rc('ytick', labelsize=20)
    # plt.tick_params(axis='both', labelsize=20)
    plt.figure(figsize=(10, 7))
    sn.heatmap(df_cm, annot=False, cmap="YlGnBu", vmin=50, vmax=100)
    plt.xlabel('Actual space group')
    plt.ylabel('Predicted space group')
    plt.title('Confusion matrix of sg prediction')
    plt.show()


def cs_cm_plt(data_dir):  # <<<<<
    error_dict = {}
    corrects = numpy.zeros(7)
    # create error_list.json
    import json
    for i in range(7):
        error_list = []
        with open("data/guess/crystal_list_{}.txt".format(i+1), "r") as list_file:
            for data_file_path in list_file:
                with open(data_file_path.split()[0], "r") as data_file:
                    data_json = json.load(data_file)
                    sg_num = crystal_number(data_json["number"])
                    if sg_num == i:
                        corrects[i] += 1
                    #
                    else:
                        error_list.append([data_file_path.split()[0], sg_num, i+1])

            error_dict["crystal_{}".format(i+1)] = error_list
    with open("error_list.json", 'w') as sum_f:
        json.dump(error_dict, sum_f, indent=2)
    # plot confusion matrix
    import seaborn as sn
    import pandas as pd
    import matplotlib.pyplot as plt

    numpy.set_printoptions(suppress=True)
    confusion_matrix = numpy.zeros([7, 7])
    plt.figure()
    for i in range(7):
        stat = error_dict['crystal_{}'.format(i+1)]
        for j in range(len(stat)):
            index = stat[j][1]
            confusion_matrix[i][index] += 1

    # Added corrects
    for i in range(7):
        confusion_matrix[i][i] = corrects[i]

    df_cm = pd.DataFrame(confusion_matrix, index=[i for i in "1234567"],
                         columns=[i for i in "1234567"])
    plt.rc('axes', titlesize=20, labelsize=20)
    plt.rc('figure', titlesize=20)
    plt.figure(figsize=(10, 7))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    sn.heatmap(df_cm, annot=True, cmap="Blues", fmt='g',annot_kws={"size": 20})
    plt.xlabel('Actual Crystal System')
    plt.ylabel('Predicted Crystal System')
    plt.title('Confusion matrix of CS prediction')
    plt.show()

    guess_total = [sum(confusion_matrix[i]) for i in range(7)]
    cm_normalized = [confusion_matrix[i]/guess_total[i] for i in range(7)]

    df_cm = pd.DataFrame(cm_normalized, index=[i for i in "1234567"],
                         columns=[i for i in "1234567"])

    plt.rc('axes', titlesize=20, labelsize=20)
    plt.rc('figure', titlesize=20)
    plt.figure(figsize=(10, 7))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    sn.heatmap(df_cm, annot=True, annot_kws={"size": 20}, cmap="Blues", fmt='.0%')
    plt.xlabel('Actual Crystal System')
    plt.ylabel('Predicted Crystal System')
    plt.title('Confusion matrix(normalized) of CS prediction')
    plt.show()


def print_result(group_numbers, guess_list_dir, actual_list_dir, list_format, plt =True):

    guess_total = total_count(group_numbers, guess_list_dir, list_format)
    actual_total = total_count(group_numbers, actual_list_dir, list_format)
    guess_correct = correct_count(group_numbers, guess_list_dir, actual_list_dir, list_format)
    print("guess count:", guess_total, guess_total.sum())
    print("actual count:", actual_total, actual_total.sum())
    print("guess correct:", guess_correct, guess_correct.sum())

    print("correct percentage in guess:", (1 - (guess_total - guess_correct).sum()/guess_total.sum())*100)

    print("TP:", guess_correct)
    print("TN:", numpy.full(len(group_numbers), actual_total.sum()) - guess_total - actual_total + guess_correct
          if len(group_numbers) > 1 else None)
    print("FP:", guess_total - guess_correct)
    print("FN:", actual_total - guess_correct)


if __name__ == '__main__':
    # print_result(range(1, 8), "data/guess/", "data/actual/", "crystal_list_{}.txt")
    # print_result(range(1, 231), "data/guess/", "data/actual/", "spacegroup_list_{}.txt")
    cs_cm_plt('data/input_data_test06/')  # <<<<<<<
    # sg_cm_plt('data/input_data_test06/')
    pass

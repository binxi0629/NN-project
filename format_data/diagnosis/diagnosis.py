import json
import os
import numpy as np


def check_spacegroup_weight(num_data=1):
    data_dir = '../../input_data/'
    store = {}
    # initialize sg_weight
    sg_weight = np.zeros([230, 2])
    for i in range(230):
        sg_weight[i][0] = i+1

    for subdir, dirs, files in os.walk(data_dir):
        for i in range(num_data):
            with open(data_dir+files[i]) as f:
                data_json = json.load(f)
                sg_number = np.array(data_json["number"])
                sg_weight[sg_number-1][1] += 1

    print(sg_weight)


class NumpyEncoder(json.JSONEncoder):
    """
        to solve Error: NumPy array is not JSON serializable
        see: https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
    """
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':
    check_spacegroup_weight(9771)

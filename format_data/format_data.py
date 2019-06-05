import json
import re
import numpy as np


class BandsData:

    # generic dict of high-symmetry points
    __gen_dict = {
        '\\Gamma': None,  # Center of the Brillouin zone
        'M': None,  # Center of an edge
        'R': None,  # Corner point
        'X': None,  # Center of a face
        'K': None,  # Middle of an edge joining two hexagonal faces
        'L': None,  # Center of a hexagonal face
        'U': None,  # Middle of an edge joining a hexagonal and a square face
        'W': None,  # Corner point
        'H': None,  # Corner point joining four edges
        'N': None,  # Center of a face
        'P': None,  # Corner point joining three edges
        'A': None,  # Center of a hexagonal face
    }

    def __init__(self, mp_id):
        # self.file_name = file_name
        self.mp_id = mp_id
        self.new_dict = self.__gen_dict
        """
            input: data file with .json format
            output: return bands(type: list), bands_info(type: dict)
                bands: a new matrix with rearranged ordering corresponding to each high-symmetry point
                bands_info: keywords = high-symmetry points, value = vector of each band

            more detail see:
        """

    @staticmethod
    def load_data(file_dir='../data/', mp_id='mp_id'):
        """
            This is used to load data from downloaded data file
        :param file_dir: dir of .json file, default: '../data/'
        :param mp_id: material-project id
        :return: bands: in matrix form
                branches: contains info of bands along which high-symmetry direction

        """

        with open('{file_dir}raw_data_{mp_id}.json'.format(file_dir=file_dir, mp_id=mp_id), 'r') as f:
            data = json.load(f)
            bands = data["band"]["bands"]
            bands = np.array(bands)
            branches = data["band"]["branches"]

        return bands, branches

    def format_data(self, bands, branches):
        """
            each .json data file contains original bands matrix, and their corresponding high-symmetry direction
            e.g. '\\Gamma-X'

        :param bands:
        :param branches:
        :return:
        """

        order = []  # list to store high-symmetry point
        band_index = {}  # dict to store band index info corresponding to its high-symmetry point e.g. "X": 18
        formatted_bands = []
        zero_matrix = np.zeros(np.shape(bands))

        for i in range(len(branches)):
            order.append(branches[i]["name"])
            spilt = re.split('-', order[i])

            band_index[spilt[0]] = branches[i]['start_index']
            band_index[spilt[1]] = branches[i]['end_index']

        # iterate all keys in band_index, and if exists, give value to new_dict, if not, pass
        for hs_point in band_index:
            if hs_point in self.new_dict:
                self.new_dict[hs_point] = band_index[hs_point]

        # iterate all keys in new_dict, export bands (not arranged in bands dimension)
        for hs_point in self.new_dict:
            hs_value = self.new_dict[hs_point]
            if self.new_dict[hs_point] == None:
                # fill zeros in bands
                formatted_bands.append(zero_matrix[:, 0])
            else:
                formatted_bands.append(bands[:, hs_value])

        # TBC
        # transpose
        formatted_bands = np.transpose(formatted_bands)

        return formatted_bands, self.new_dict


class NumpyEncoder(json.JSONEncoder):
    """
        to solve Error: NumPy array is not JSON serializable
        see: https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
    """
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
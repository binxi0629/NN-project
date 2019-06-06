import json
import re
import numpy as np


class BandsData:

    def __init__(self, mp_id):

        # generic dict of high-symmetry points
        self.__gen_dict = {
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

        # self.file_name = file_name
        self.mp_id = mp_id
        self.new_dict = self.__gen_dict

    @staticmethod
    def load_data(file_dir='../data/', mp_id='mp_id'):
        """
            This is used to load data from downloaded data file, each .json data file contains original bands matrix,
            and their corresponding high-symmetry direction e.g. '\\Gamma-X'

        :param file_dir: dir of .json file, default: '../data/'
        :param mp_id: material-project id
        :return: bands: bands info in matrix form
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
            This is for formatting original data

        :param bands: bands info in matrix form
        :param branches: contains info of bands along which high-symmetry direction
        :return: formatted_bands: formatted bands info in matrix form
                 self.new_dict: write the split high-symmetry points, in dict form

        """
        self.new_dict = self.__gen_dict
        order = []  # list to store high-symmetry point
        band_index = {}  # dict to store band index info corresponding to its high-symmetry point e.g. "X": 18
        formatted_bands = []
        zero_matrix = np.zeros(np.shape(bands))
        """
            zero_matrix is for: if one configuration does not have some high-symmetry points listed in __generic_dict
            then fill zeros in those columns 
        """

        for i in range(len(branches)):
            order.append(branches[i]["name"])
            spilt = re.split('-', order[i])

            band_index[spilt[0]] = branches[i]['start_index']
            band_index[spilt[1]] = branches[i]['end_index']

        # print('>>>>>>>>>>>>>>>>>>', band_index)
        # iterate all keys in band_index, and if exists, give value to new_dict, if not, pass
        for hs_point in band_index:
            if hs_point in self.new_dict:
                self.new_dict[hs_point] = band_index[hs_point]
        # print('>>>>>>>>>>>>>>>>>', BandsData.__gen_dict)

        # iterate all keys in new_dict, export bands (not arranged in bands dimension)
        for hs_point in self.new_dict:
            hs_value = self.new_dict[hs_point]
            if self.new_dict[hs_point] == None:
                # fill zeros in bands
                formatted_bands.append(zero_matrix[:, 0])
            else:
                formatted_bands.append(bands[:, hs_value])

        # transpose of formatted_bands
        formatted_bands = np.transpose(formatted_bands)

        return formatted_bands, self.new_dict

    @staticmethod
    def degen_translate(formatted_bands, en_tolerance=0.01):
        """
            This method is for represent the bands matrix into a degeneracy form
        :param formatted_bands: one of the output from format_data() metod
        :param en_tolerance: energy tolerance, default 0.01eV
        :return:
        """
        tmp = np.array(formatted_bands)
        size = np.shape(tmp)
        degen_bands = np.zeros(size)

        # Need further test
        for i in range(size[1]):
            each_column = []
            count = 1
            for j in range(size[0]-1):
                if tmp[j][i] == 0:
                    count = 0
                    break
                else:
                    if np.absolute(tmp[j+1][i]-tmp[j][i]) <= en_tolerance:
                        count += 1
                    else:
                        for k in range(count):
                            each_column.append(count)
                        count = 1
            if count == 0:
                pass
            else:
                for k in range(count):
                    each_column.append(count)
                degen_bands[:, i] = np.array(each_column)

        return degen_bands

    @staticmethod
    def fix_bands_dim(degen_bands, num_of_bands=30):
        """
            This method is for cut bands dimension to a fixed number, default 30
        :param degen_bands: output from degen_translate() method
        :param num_of_bands: the fixed dimension default:30 (30 is the minimum bands value of all data)
        :return: fixed_bands: bands matrix with fixed dimension
        """

        tmp = np.array(degen_bands)

        fixed_bands = tmp[0:num_of_bands, :]
        # print(np.shape(fixed_bands))
        return fixed_bands


class NumpyEncoder(json.JSONEncoder):
    """
        to solve Error: NumPy array is not JSON serializable
        see: https://stackoverflow.com/questions/26646362/numpy-array-is-not-json-serializable
    """
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

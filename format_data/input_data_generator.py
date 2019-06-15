from pymatgen.ext.matproj import MPRester
from pathlib import Path
import format_data
import json
import os
import numpy as np

m = MPRester("z9urSTLgyAmN85OW")


def get_space_group_from_file(mp_id):  # load file in input_data
    try:
        with open('../input_data/input_data_{}.json'.format(mp_id), 'r') as f:
            doc = json.load(f)
        return doc["spacegroup"], doc["number"]
    except FileNotFoundError:
        return


def create_new_data():
    """
        Create new data without doing degeneracy translation
    :return: None
    """

    data = {}
    data_dir = '../data/'  # raw data directory
    data["number"] = 0
    data["spacegroup"] = None
    count = 1
    error_files = {}
    error_files["mp_id"] =[]

    for subdir, dirs, files in os.walk(data_dir):
        num_files = len(files)
        for i in range(num_files):
            with open(data_dir+files[i]) as f:
                data_json = json.load(f)

                mp_id = data_json["id"]
                data['id'] = mp_id
                this_data = format_data.BandsData(mp_id=mp_id)
                bands = data_json["band"]["bands"]
                bands = np.array(bands)
                branches = data_json["band"]["branches"]
                formatted_bands, new_dict = this_data.format_data(bands, branches)

                new_bands = this_data.fix_bands_dim(formatted_bands)  # <<<<<<<<<<<<<<<<

                data["bands"] = new_bands
                # data["spacegroup"], data["number"] = get_space_group_from_file(mp_id)

                # save new_input_data_*.json under new_input_data_3/
                try:
                    with open('../input_data/input_data_{}.json'.format(mp_id), 'r') as input_file:
                        doc = json.load(input_file)
                    data["spacegroup"], data["number"] = doc["spacegroup"], doc["number"]
                except FileNotFoundError:
                    error_files["mp-id"].append(mp_id)
                    continue
                # input data file name: new_input_data_<mp-id>.json
                save_file_name = 'new_input_data_{}.json'.format(mp_id)

                with open('../new_input_data/{}'.format(save_file_name), 'w') as file:
                    json.dump(data, file, cls=format_data.NumpyEncoder, indent=4)
                    print("finished... {}/21,737".format(count))  # total input: 21,737
                    count += 1

    with open('error_files.json', 'w') as ef:
        json.dump(error_files, ef, cls=format_data.NumpyEncoder, indent=2)


def create_new_data_around_fermi():
    """
        More useful than create_new_data()
        Create new input data around fermi level, slightly modified from above function
    :return: None
    """

    data = {}
    data_dir = '../data/'  # raw data directory
    data["number"] = 0
    data["spacegroup"] = None
    count = 1
    error_files = {}
    error_files["mp_id"] = []
    low_fermi = []

    for subdir, dirs, files in os.walk(data_dir):
        num_files = len(files)
        for i in range(num_files):
            # load original data
            with open(data_dir + files[i]) as f:
                data_json = json.load(f)

                mp_id = data_json["id"]
                # id
                data['id'] = mp_id

                # create format_data class
                this_data = format_data.BandsData(mp_id=mp_id)
                bands = data_json["band"]["bands"]  # load original bands
                bands = np.array(bands)
                branches = data_json["band"]["branches"]  # load original branches
                formatted_bands, new_dict = this_data.format_data(bands, branches)  # formatted bands at HS points

                new_bands = this_data.fix_bands_dim_around_fermi(formatted_bands)  # <<<<<<<
                if new_bands is None:
                    print('The fermi level is below 10 for {} band'.format(mp_id))
                    low_fermi.append(mp_id)
                    continue
                else:
                    data["bands"] = new_bands
                    # data["spacegroup"], data["number"] = get_space_group_from_file(mp_id)
                    try:
                        with open('../input_data/input_data_{}.json'.format(mp_id), 'r') as input_file:
                            doc = json.load(input_file)
                        data["spacegroup"], data["number"] = doc["spacegroup"], doc["number"]
                    except FileNotFoundError:
                        error_files["mp-id"].append(mp_id)
                        continue
                    save_file_name = 'new_input_data_{}.json'.format(mp_id)

                    with open('../new_input_data_5/{}'.format(save_file_name), 'w') as file:
                        json.dump(data, file, cls=format_data.NumpyEncoder, indent=4)
                        print("finished... {}/21,737".format(count))
                        count += 1

    with open('error_files.json', 'w') as ef:
        json.dump(error_files, ef, cls=format_data.NumpyEncoder, indent=2)

    print(low_fermi)


if __name__ == "__main__":
    create_new_data_around_fermi()


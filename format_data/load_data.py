from pymatgen.ext.matproj import MPRester
from pathlib import Path
import format_data
import json
import os
import numpy as np

m = MPRester("HvxfB98DFTCPiadV")


def get_space_group(file_id):  # function to get space group by id

    doc = m.get_doc("mp-{}".format(file_id))

    return doc["spacegroup"]["symbol"], doc["spacegroup"]["number"]


def create_data():
    data = {}
    data_dir = '../data/'
    data["number"] = 0
    data["spacegroup"] = None
    count = 1

    for subdir, dirs, files in os.walk(data_dir):
        num_files = len(files)
        for i in range(num_files):
            with open(data_dir + files[i]) as f:
                data_json = json.load(f)

                mp_id = data_json["id"]
                data['id'] = mp_id
                this_data = format_data.BandsData(mp_id=mp_id)
                bands = data_json["band"]["bands"]
                bands = np.array(bands)
                branches = data_json["band"]["branches"]
                formatted_bands, new_dict = this_data.format_data(bands, branches)
                degen_bands = this_data.degen_translate(formatted_bands)
                new_bands = this_data.fix_bands_dim(degen_bands)
                data["bands"] = new_bands
                try:
                    data["spacegroup"], data["number"] = get_space_group(mp_id)
                except:
                    print("{} is not found".format(mp_id))
                    continue

                save_file_name = 'input_data_{}.json'.format(mp_id)
                with open('../input_data/{}'.format(save_file_name), 'w') as file:
                    json.dump(data, file, cls=format_data.NumpyEncoder, indent=4)
                    print("finished... {}/21,738".format(count))
                    count += 1


"""
def add_data():
    # Fixed the issue: https://github.com/binxi0629/NN-project/issues/4

    with open('error_files.json', 'r') as f:
        files_id = json.load(f)
        for i in files_id["mp_id"]:
            try:
                get_space_group(i)
            except:
                print("{} is not found".format(i))
                continue

            sg, sg_number = get_space_group(i)


            data = {}
            data["bands"] = []
            data["number"] = 0
            data["spacegroup"] = None

            # step 1: new a format_data cls
            this_data = format_data.BandsData(mp_id=i)

            # step 2: load the bands matrix by mp_id
            bands, branches = this_data.load_data(mp_id=i)

            # step 3: format bands to a __gen_dict form
            formatted_bands, new_dict = this_data.format_data(bands, branches)

            # step 4: degeneracy representation
            degen_bands = this_data.degen_translate(formatted_bands)

            # step 5: cut the bands dimension
            fixed_bands = this_data.fix_bands_dim(degen_bands)

            # step 6: save in a dict
            data["bands"] = fixed_bands

            data["spacegroup"], data["number"] = sg, sg_number

            # need one more step to store data["sg_label"]

            # save in a .json file
            save_file_name = 'input_data_{}.json'.format(i)

            with open('../input_data/{}'.format(save_file_name), 'w') as f2:
                json.dump(data, f2, cls=format_data.NumpyEncoder, indent=4)

            print("File raw_data_{}.json saved, loading next file... ".format(i))

"""


def create_new_data_around_fermi():
    """
        Create new input data around fermi level
    :return:
    """

    data = {}
    data_dir = '../data/'
    data["number"] = 0
    data["spacegroup"] = None
    count = 1
    error_files = {}
    error_files["mp_id"] = []

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

                with open('../new_input_data_3/{}'.format(save_file_name), 'w') as file:
                    json.dump(data, file, cls=format_data.NumpyEncoder, indent=4)
                    print("finished... {}/21,737".format(count))
                    count += 1

    with open('error_files.json', 'w') as ef:
        json.dump(error_files, ef, cls=format_data.NumpyEncoder, indent=2)


if __name__ == "__main__":
    # main()
    create_data()

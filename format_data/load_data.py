from pymatgen.ext.matproj import MPRester
from diagnosis import diagnosis
import format_data
import json, os
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

                with open('../input_data_1/{}'.format(save_file_name), 'w') as file:  # <<<<<<<
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
                    save_file_name = 'new_EL_input_data_{}.json'.format(mp_id)

                    with open('../input_data_3_5/{}'.format(save_file_name), 'w') as file:
                        json.dump(data, file, cls=format_data.NumpyEncoder, indent=4)
                        print("finished... {}/21,737".format(count))
                        count += 1

    with open('error_files.json', 'w') as ef:
        json.dump(error_files, ef, cls=format_data.NumpyEncoder, indent=2)

    print(low_fermi)


def create_high_weights_new_data(data_dir, new_data_dir, weights_lower_limit=100):
    print("Running... please wait")
    sg_num_list, total_num = diagnosis.check_specific_spacegroup_num(data_dir=data_dir,
                                                                     occurrence_limit=weights_lower_limit,
                                                                     greater=True,
                                                                     save=False, plt=False)
    count = 0
    for i in sg_num_list:
        file_count = 0
        for subdir, dirs, files in os.walk(data_dir):
            num_files = len(files)
            for j in range(num_files):
                with open(data_dir + files[j]) as f:
                    data_json = json.load(f)

                    if data_json["number"] == i:
                        this_data = {}
                        this_data = data_json
                        this_data["new_number"] = count
                        with open(new_data_dir+files[j], 'w') as new_file:
                            json.dump(this_data, new_file, cls=format_data.NumpyEncoder, indent=2)
                        file_count +=1
                        print("\rSaved: {}".format(file_count), end="")

        count += 1
        print("\nFinished current spacegroup number, running next one: {}/{}".format(count, total_num))

    print("Done! Check in {}".format(new_data_dir))


def create_den_data_around_fermi():
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

                fermi_index = this_data.find_fermi_index(formatted_bands)  # locate fermi

                translated_bands = this_data.degen_translate(formatted_bands)  # degeneracy translate

                new_bands = this_data.fix_bands_dim_around_fermi(translated_bands,
                                                                 fermi_index=fermi_index)  # <<<<<<<

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

                    with open('../input_data_3/{}'.format(save_file_name), 'w') as file:  # <<<<<
                        json.dump(data, file, cls=format_data.NumpyEncoder, indent=4)
                        print("finished... {}/21,737".format(count))
                        count += 1

    with open('error_files.json', 'w') as ef:
        json.dump(error_files, ef, cls=format_data.NumpyEncoder, indent=2)

    print(low_fermi)


if __name__ == "__main__":
    # create_new_data()
    # create_new_data_around_fermi()
    # create_den_data_around_fermi()

    create_high_weights_new_data(data_dir="../input_data_3/",
                                 new_data_dir="../hw_input_data_5_3/",
                                 weights_lower_limit=200)



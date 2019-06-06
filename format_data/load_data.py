from pymatgen.ext.matproj import MPRester
from pathlib import Path
import format_data
import json

m = MPRester("Hyxf8a7HI7RhXZI1kaFT")


def get_space_group(file_id):  # function to get space group by id

    doc = m.get_doc("mp-{}".format(file_id))

    return doc["spacegroup"]["symbol"], doc["spacegroup"]["number"]



def main():
    print('running..., please wait')

    for file_id in range(10):
        file = Path("../data/raw_data_{}.json".format(file_id))
        if file.is_file():
            print("File raw_data_{}.json exists, formatting file...       TOTAL: {}/10,000".format(file_id, file_id))

            # step 0: initialize
            data = {}
            data["bands"] = []
            data["number"] = 0
            data["spacegroup"] = None

            # step 1: new a format_data cls
            this_data = format_data.BandsData(mp_id=file_id)

            # step 2: load the bands matrix by mp_id
            bands, branches = this_data.load_data(mp_id=file_id)

            # step 3: format bands to a __gen_dict form
            formatted_bands, new_dict = this_data.format_data(bands, branches)

            # step 4: degeneracy representation
            degen_bands = this_data.degen_translate(formatted_bands)

            # step 5: cut the bands dimension
            fixed_bands = this_data.fix_bands_dim(degen_bands)

            # step 6: save in a dict
            data["bands"] = fixed_bands

            data["spacegroup"], data["number"] = get_space_group(file_id)

            # need one more step to store data["sg_label"]

            # save in a .json file
            save_file_name = 'input_data_{}.json'.format(file_id)

            with open('../input_data/{}'.format(save_file_name), 'w') as f:
                json.dump(data, f, cls=format_data.NumpyEncoder, indent=4)
            print("File raw_data_{}.json saved, loading next file...      TOTAL: {}/10,000".format(file_id, file_id))
        else:
            print("File raw_data_{}.json NOT FOUND, loading next file...  TOTAL: {}/10,000".format(file_id, file_id))

    print('All files successfully saved, please check in /input_data/')


if __name__ == "__main__":
    main()
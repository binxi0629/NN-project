import format_data
import json
import numpy as np
from pymatgen.ext.matproj import MPRester

# step 1: new a format_data cls
test_data = format_data.BandsData(mp_id=32306)  # test_sample 1

# step 2: load the bands matrix by mp_id
bands, branches = test_data.load_data(file_dir='../sample_data/', mp_id=32306)
# print(bands)
# print(branches)

# step 3: format bands to a __gen_dict form
formatted_bands, new_dict = test_data.format_data(bands, branches)

# step 4: degeneracy representation
degen_bands = test_data.degen_translate(formatted_bands)

# step 5: cut the bands dimension
fixed_bands = test_data.fix_bands_dim(degen_bands)

print(fixed_bands)
# print(type(degen_bands))
# print(np.shape(input_bands))
# print(formatted_bands)
# print(new_dict)

data = {'bands': degen_bands}
with open('sample_input.json', 'w') as f:
    json.dump(data, f, cls=format_data.NumpyEncoder, indent=4)


"""
test_data02 = format_data.BandsData(mp_id=32428)  # test_sample 2
bands02, branches02 = test_data02.load_data(file_dir='../sample_data/', mp_id=32428)
# print(bands02)
# print(branches02)

formatted_bands02, new_dict02 = test_data02.format_data(bands02, branches02)
input_bands02 = test_data02.fix_bands_dim(formatted_bands02)
data02 = {'bands': input_bands02}
with open('output02.json', 'w') as f02:
    json.dump(data02, f02, cls=format_data.NumpyEncoder, indent=4)
"""
print('>>>>>>>>>>>>>')


m = MPRester("Hyxf8a7HI7RhXZI1kaFT")
doc = m.get_doc("mp-1")
print(doc["spacegroup"])
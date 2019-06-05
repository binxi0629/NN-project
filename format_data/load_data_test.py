import format_data
import json
# import numpy as np

"""
    This part moved to format_data.py
    
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
"""

test_data = format_data.BandsData(mp_id=32306)  # test_sample 1
bands, branches = test_data.load_data(file_dir='../sample_data/', mp_id=32306)
# print(bands)
# print(branches)
formatted_bands, new_dict = test_data.format_data(bands, branches)
# print(formatted_bands)
# print(new_dict)
data = {'bands': formatted_bands}
with open('output.json', 'w') as f:
    json.dump(data, f, cls=format_data.NumpyEncoder, indent=4)


test_data02 = format_data.BandsData(mp_id=32428)  # test_sample 2
bands02, branches02 = test_data02.load_data(file_dir='../sample_data/', mp_id=32428)
print(bands02)
print(branches02)

formatted_bands02, new_dict02 = test_data02.format_data(bands02, branches02)
data02 = {'bands': formatted_bands02}
with open('output02.json', 'w') as f02:
    json.dump(data02, f02, cls=format_data.NumpyEncoder, indent=4)

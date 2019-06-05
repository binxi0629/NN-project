import format_data
import json
# import numpy as np

"""
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
"""

test_data = format_data.BandsData(mp_id=32306)
bands, branches = test_data.load_data(mp_id=32306)
# print(bands)
# print(branches)
formatted_bands, new_dict = test_data.format_data(bands, branches)
# print(formatted_bands)
# print(new_dict)
data = {'bands': formatted_bands}
with open('output.json', 'w') as f:
    json.dump(data, f, cls=format_data.NumpyEncoder, indent=4)

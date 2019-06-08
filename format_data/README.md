## This repo is for formatting the downloaded data into the form of NN input data

## Files info

1. format_data.py: core module which contains BandsData class and NumpyEncoder class
    - BandsData
      - provide method to load data (*default dir*: [../data/](../data/))
      - probide method to format data         

2. load_data.py: load and format data, saved in [../input_data](../input_data) (you can check the data format there)


## More to come ...

## Todos

- [x] load data (sample data in ../sample_data/)
- [x] format data contain two parts
  - [x] part 1: the new formatted data should be at high-symmetry point (dimension of the rows should be all the same)
  - [x] part 2: the new formatted data should have the same number of bands (dimension of the columns should be all the same)
- [x] test for formatting the same data
- [x] translate to a new representation(a new matrix by referring their degeneracies)
- [x] format all the data, saved in ../input_data
- [x] supervised learning, should labbel space group, this one can be done by using [MPRester](https://pymatgen.org/pymatgen.ext.matproj.html) module by their mp_id
- [x] a script to load all data
- [ ] according to training data result, modify some config parameters e.g. dimension of bands and HS points
- [x] add new tag "mp_id" in input_data_<mp_id>.json 
- [ ] write a config file, put all parameters there

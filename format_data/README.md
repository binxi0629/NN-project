## This repo is for formatting the downloaded data into the form of NN input data

## Files info

1. format_data.py: core module which contains BandsData class and NumpyEncoder class
    - BandsData
      - provide method to load data (*default dir*: [../data/](../data/))
      - probide method to format data         

2. load_data.py: load and format data, saved in [../input_data](../input_data) (you can check the data format there)

3. new_data_generating.py: script to create input data without doing degeneracy translation

4. stat.py: script to check whether input data are good or not

## Usage guideline(NOT finished)
  All parameters are written in [config.py](config.py)
 
 1. Required folders:
 ``` 
    ├── data/
    ├── input_data/
    ├── new_input_data_*/  # you will save data here  
    └── format_data/
        ├── format_data.py
        ├── load_data.py
        ├── config.py
        └── utils/*
 ```
 2. Tune parameters
 -  `args['create_data']` 
    - if  `start`  is `True`, will create data
    - `data_dir` : load raw data from here
    - if `degeneracy` is `True`: degenerate (D) bands
    - `en_tolerance`: energy tolerance, recommanded `0.001`
    - `around`
 
  

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
- [x] regenerate input_data_<mp_id>.json without doing degeneracy translation 
- [x] regenerate input_data_<mp_id>.json with bands around fermi level

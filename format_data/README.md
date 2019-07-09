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
    - if `around_fermi` is `True`: energy level (EL) bands around the fermi level
    - if `b2t` is `True`: energy level (EL) bands from bottom to the top
    - if `padding_b2t` is `True`: padded bands from bottom to the top
    - if `padding_around_fermi` is `True`: padded bands around fermi level
    - `num_of_bands`: number of bands
    - `bands_below_fermi_limit`: bands number below fermi level, if symmetric, it should be half of `num_of_bands`
    - `save_dir`: floder that you will save your new data here
 
 Note: `b2t`, `around_fermi` can not both be `True`,
       `padding_b2t`, `padding_around_fermi` can not both be `True`,
       `padding_b2t`(or `padding_around_fermi`), `b2t`(or `around_fermi` ) can not both be `True`
 
 priority: `padding_b2t` > `padding_around_fermi` > `around_fermi` > `b2t`
 
 -  `args['create_hw_data']`
    - if  `start`  is `True`, will create high weight data
    - `data_dir` : load FORMATTED data (e.g. `../input_data_*`) from here
    - `new_data_dir`: floder that you will save your new data here   
    - `lowest_weights_limit`: lowest occurrence 
    - if `greater` is `True`: greater than `lowest_weights_limit`
    - if `save` is `True`: will save in new file (more to come)
    - if `plt` is `True`: will plot sg occurence Vs. sg number

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

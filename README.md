# NN-project
## This project is a NN project, which outputs space group with input being band structure

## Folder Structure
```
  ├── data/    # original data(not formatted data)
  ├── input_data/    # input data(formatted data)
  ├── sample_data/    # sample data for testing use
  ├── data_generation/    # contians script to generate new data set in proper format (NOT finished).
  |   ├──download_data.py    # a scirpt to download new data by MPRester modules
  |   └──utils/*    # contains progress bar (NOT used in code)
  ├── format_data/    # a folder on coverting data to proper format
  |   ├── format_data.py    # a script to format data
  |   ├── load_data.py    # main script
  |   ├── stat.py    # run statistics on current input data
  |   ├── bands_res.json    # statistics result: band_num Vs its occurrences
  |   ├── bands_occurrences.jepg    # .png to show statistics result
  |   └── diagnosis/    # diagnosis possible issuse on the input data
  |       ├── diagnosis.py    # diagonsing script
  |       └── spacegroup_weights.txt    # diagnosis result: the weights of space group
  ├── network/    # key folder contains fully connected Neural Network architecture
      ├── data_stat/
      |   └──gen_stat.py  # script of counting mispredicted result
      └── nn_model/
          ├──data_loader_bs_crys.py  # load input data (230 sg-> 7 crystal systems )
          ├──dara_loader_bs_sg.py  # load input data (directly classify all input into 230 sg)
          ├──data_loader-crys_sg.py # load input data (classification of each subcrystal system)
          ├──mdoel_*.py # neural network model
          ├──filter_data.py  # filter bnads_num-less-than-threshold cases
          └──main.py 
 ```
 For data generation: see [data_generation](data_generation/)
 
 For data format: see [format_data](format_data/)
 
 For NN archi: see [network](network/)

## TODOS: UPDATED 03/07

- [x] Reduce the classes from 230 to e.g. 100
- [x] Optimize the NN archi, bands number...
- [x] Convergence test of loss
- [x] Check the code, data_loader, shuffling, data format...
- [x] Code refactoring
- [ ] Add bands padding function and do testing

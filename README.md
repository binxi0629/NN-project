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
  ├── format_data/    # a folder on covert data to proper format
  |   ├── format_data.py    # a script to format data
  |   ├── load_data.py    # main script
  |   ├── stat.py    # run statistics on current input data
  |   ├── bands_res.json    # statistics result: band_num Vs its occurrences
  |   ├── bands_occurrences.jepg    # .png to show statistics result
  |   └── diagnosis/    # diagnosis possible issuse on the input data
  |       ├── diagnosis.py    # diagonsing script
  |       └── spacegroup_weights.txt    # diagnosis result: the weights of space group
  ├── network/    # ket folder contains fully connected Neural Network architecture
      └── ...(TBC)
 ```
 For data generation: see [data_generation](data_generation/)
 
 For data format: see [format_data](format_data/)
 
 For NN archi: see [network](network/)

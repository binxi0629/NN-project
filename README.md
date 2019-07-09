# NN-project
## This project is a NN project, which outputs space group with input being band structure

## Folder Structure
```
  ├── data/    
  ├── input_data/    
  ├── sample_data/    
  ├── data_generation/    
  |   ├──download_data.py    
  |   └──utils/*   
  ├── format_data/   
  |   ├── format_data.py    
  |   ├── load_data.py   
  |   ├── stat.py    
  |   ├── config.py   
  |   └── diagnosis/    
  |       ├── diagnosis.py    
  |       └── spacegroup_weights.txt    
  └── network/    
      ├── data_stat/
      |   └──gen_stat.py  
      └── nn_model/
          ├──data_loader_bs_crys.py  
          ├──dara_loader_bs_sg.py 
          ├──data_loader-crys_sg.py 
          ├──mdoel_*.py 
          ├──filter_data.py  
          └──main.py 
 ```
 For data generation: see [data_generation](data_generation/)
 
 For data format: see [format_data](format_data/)
 
 For NN archi: see [network](network/)

## TODOS: UPDATED 09/07

- [x] Reduce the classes from 230 to e.g. 100
- [x] Optimize the NN archi, bands number...
- [x] Convergence test of loss
- [x] Check the code, data_loader, shuffling, data format...
- [x] Code refactoring
- [x] Add bands padding function and do testing

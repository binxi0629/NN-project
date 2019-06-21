# Results Show

| No.| # of bands | Around Fermi| # sg classes| EL or D| NN model| # of epochs | # of data | Results|
|----|------------|-------------|-------------|--------|---------|-------------|-----------|--------|
| 1 | 30 | yes | 38 (> 100)| EL | model_2 | 10 | 11988 | 61.8% |
| 2 | 30 | yes | 42 (> 90) | EL | model_2 | 10 | 12370 | 62.2% |
| 3 | 30 | no | 44 (> 100) | EL | model_2 | 10 | 17266 | 70.4% |
| 4 | 30 | no| 49 (> 80) | EL | model_2 | 10 |  17647 | 66.0% |
| 5 | 30 | yes | 38 (> 100) | D | model_2 | 10| 11988 | 73.7% |
| 6 | 30 | yes | 42 (> 90) | D | model_2 | 10 | 12370 | 75.6% |
| 7 | 30 | yes | 44 (> 80) | D | model_2 | 10 | 12536 | 74.4%|
| 8 | 30 | yes | 60 (> 50) | D | model_2 | 10 | 13566 | 72.2%|
|9 | 30 | yes | 230 | D| model_2 | 10 | 14937 | 63.4%|
| 10 | 40 | yes | 31 (> 100) | D | model_2 | 10 | 9026 | 72.3% |
| 11 | 50 | yes | 27 (> 100) | D | model_2 | 10 | 7438 | 76.5% |
| 12 | 50 | yes | 27 (> 100) | D | model_2 | 40 | 7438 | ~78% | 

## Loss Vs. epochs and preidction Vs. epochs
( [No. 12](./hw_input_5_40epochs) )

Seems it does converge (very quickly) but turns out the input data are not good:
 - Maybe we have cut too much info
 - The input are complicated and cound not learn any thing new

## TODOS
- [ ] Feed both EL and D into the network
    - [x] with no weights: 0.5/0.5
    - [ ] with weights: 0.7/0.3
    - [ ] with weights: 0.3/0.7
- [ ] Try only Gamma point
- [ ] Try sg occurrences > 200
- [ ] Try mispredicted sg numbers, see the physics behind it

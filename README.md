# Efficient columnwise correlation

Efficient ways to compute Pearson's correlation between columns of two matrices in numpy (and beyond)

See http://stackoverflow.com/questions/19401078/efficient-columnwise-correlation-coefficient-calculation-with-numpy for the initial discussion

So far, it appears that one line of code in Julia is almost 5 times faster than 5 lines of code in Python (numpy MKL) doing the same thing.

## Timings

Machine: i7-5650U 2.2 GHz, 8GB 1600 MHz DDR3, 512 GB PCIe SSD, Mac OS 10.12.4

| Version                                     | Time, s |
|:------------------------------------------- |:------- |
| python 2.7.13 with numpy 1.12.1 (anaconda)  | 12.1    | 
| julia 0.5.1                                 | 2.6     |

## Running the timings

Required: numpy

```python columnwise_corrcoef_perf.py```

```julia columnwise_corrcoef_perf.jl```

## More timings (and memory)

python 3.6.1 with numpy 1.11.3 (anaconda): 12.1 s

python 2.7.10 with numpy 1.8.0rc1 (came default on MacOS): 12.4 s

julia 0.5.1: 2.623510 seconds (846.50 k allocations: 993.003 MB, 4.86% gc time)
# efficient-columnwise-correlation
Efficient ways to compute Pearson's correlation between columns of two matrices in numpy (and beyond)

See http://stackoverflow.com/questions/19401078/efficient-columnwise-correlation-coefficient-calculation-with-numpy for the discussion

## Timings

Machine: i7-5650U 2.2 GHz, 8GB 1600 MHz DDR3, 512 GB PCIe SSD, Mac OS 10.12.4

python 3.6.1 with numpy 1.11.3 (mkl): 12.1 s

python 2.7.13 with numpy 1.12.1 (mkl): 12.1 s

julia 0.5.1: 2.623510 seconds (846.50 k allocations: 993.003 MB, 4.86% gc time)

## Running the timings

Required: numpy.

```python columnwise_corrcoef_perf.jl```
```julia columnwise_corrcoef_perf.jl```
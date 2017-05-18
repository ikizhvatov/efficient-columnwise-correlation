# Efficient columnwise correlation

Efficient ways to compute Pearson's correlation between columns of two matrices in numpy and other scientific computing languages.

See http://stackoverflow.com/questions/19401078/efficient-columnwise-correlation-coefficient-calculation-with-numpy for the initial discussion.

So far, it appears that one line of code in Julia is almost 5 times faster than 5 lines of code in Python (numpy MKL) doing the same thing.

The numpy version is used in https://github.com/ikizhvatov/pysca.

## Timings

Machine: i7-5650U 2.2 GHz, 8GB 1600 MHz DDR3, 512 GB PCIe SSD, Mac OS 10.12.4

| Version                                     | Time, s |
|:------------------------------------------- |:------- |
| python 2.7.13 with numpy 1.12.1 (anaconda)  | 12.1    | 
| julia 0.5.1                                 | 1.71    |
| R 3.3.3                                     | 26.4    |
| MATLAB R2017a                               | 1.85    |

## Running the timings

Required for python: numpy

Required for R: Hmisc

Required for MATLAB: Statistics and Machine Learning Toolbox

```python columnwise_corrcoef_perf.py```

```julia columnwise_corrcoef_perf.jl```

```Rscript columnwise_corrcoef_perf.r```

```/Applications/MATLAB_R2017a.app/bin/matlab -nojvm -nodisplay -nosplash -r "columnwise_corrcoef_perf; exit;"```

For MATLAB, the example is given for Mac OS; path needs to be adjusted depending on your platform.

## More timings (and memory)

python 3.6.1 with numpy 1.11.3 (anaconda): 12.1 s

python 2.7.10 with numpy 1.8.0rc1 (came default on MacOS): 12.1 s

julia 0.5.1: 1.707247 seconds (40 allocations: 960.226 MB, 6.76% gc time)

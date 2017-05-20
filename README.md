# Efficient columnwise correlation

Efficient ways to compute Pearson's correlation between columns of two matrices in numpy and other scientific computing languages.

See http://stackoverflow.com/questions/19401078/efficient-columnwise-correlation-coefficient-calculation-with-numpy for the initial discussion.

So far, it appears that one line of code in Julia is almost 5 times faster than 5 lines of code in Python (numpy MKL) doing the same thing.

The numpy version is used in https://github.com/ikizhvatov/pysca.

## Timings

**Laptop**: i7-5650U 2.2 GHz (dual-core), 8GB 1600 MHz DDR3, 512 GB PCIe SSD, Mac OS 10.12.4 x64

**Desktop**: i7-4790K 4.0 GHz (quad-core), 32GB 1333 MHz DDR3, 250GB SATA SSD, Linux Mint 17.3 x64

On both machines, TurboBoost left on.

| Version                                     | Laptop, s  | Desktop, s | Ratio |
|:------------------------------------------- |:---------- |:---------- |:----- |
| python 2.7.13 with numpy 1.12.1 (anaconda)  | 12.1       | 7.63       | 1.6   |
| julia 0.5.2                                 | 1.71       | 0.57       | 3.0   |
| R 3.4.0                                     | 36.9       | 23.55      | 1.6   |
| MATLAB R2017a                               | 1.85       | 1.08       | 1.7   |

Python timings are the same for Python 3, and for default python 2.7 with numpy on Mac OS.

R timing degraded in 3.4.0 compared to 3.3.3 (36 s vs 26 s), despite http://blog.revolutionanalytics.com/2017/02/preview-r-340.html.

## Running the timings

Required for python: numpy

Required for R: Hmisc

Required for MATLAB: Statistics and Machine Learning Toolbox

```python columnwise_corrcoef_perf.py```

```julia columnwise_corrcoef_perf.jl```

```Rscript columnwise_corrcoef_perf.r```

```/Applications/MATLAB_R2017a.app/bin/matlab -nojvm -nodisplay -nosplash -r "columnwise_corrcoef_perf; exit;"```

For MATLAB, the example is given for Mac OS; path needs to be adjusted depending on your platform.

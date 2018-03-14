# Efficient columnwise correlation

Efficient ways to compute Pearson's correlation between columns of two matrices in numpy and other scientific computing languages.

See http://stackoverflow.com/questions/19401078/efficient-columnwise-correlation-coefficient-calculation-with-numpy for the initial discussion.

The numpy version is used in https://github.com/ikizhvatov/pysca.

## Timings

**Laptop**: i7-5650U 2.2 GHz (dual-core), 8GB 1600 MHz DDR3, 512 GB PCIe SSD, Mac OS 10.13.3

**Desktop**: i7-4790K 4.0 GHz (quad-core), 32GB 1333 MHz DDR3, 250GB SATA SSD, Ubuntu 16.04. x64

On both machines, TurboBoost left on.

| Version         | Laptop, s  | Desktop, s | Ratio |
|:--------------- |:---------- |:---------- |:----- |
| numpy 1.14.2    | 1.63       | 0.82       | 2.0   |
| julia 0.6.2     | 1.75       | 0.74       | 2.3   |
| R 3.4.3         | 33         | 26.6       | 1.2   |
| MATLAB R2017a   | 1.85       | 1.08       | 1.7   |

Python timings are given for Anaconda python 3.6.4; they are similar for Python 2.7, and for default python 2.7 with numpy on Mac OS. The `optimize` option of `einsum` leads to almost 10-fold increase in speed, bringing numpy on par with julia and MATLAB.

R timing degraded in 3.4.x compared to 3.3.3 (36 s vs 26 s), despite http://blog.revolutionanalytics.com/2017/02/preview-r-340.html.

## Running the timings

Required for python: numpy

Required for R: Hmisc

Required for MATLAB: Statistics and Machine Learning Toolbox

```python columnwise_corrcoef_perf.py```

```julia columnwise_corrcoef_perf.jl```

```Rscript columnwise_corrcoef_perf.r```

```/Applications/MATLAB_R2017a.app/bin/matlab -nojvm -nodisplay -nosplash -r "columnwise_corrcoef_perf; exit;"```

For MATLAB, the example is given for Mac OS; path needs to be adjusted depending on your platform.

## Notes

* The rough estimated performance improvement ratio when moving from laptop to desktop is 3.6 (increase in the number of cores times increase of clock speed). Interestingly, only Julia implementation is very close to this estimate, while solutions in other languages significantly lag behind.
* The same Numpy solution (but without einsum) is described independently at https://waterprogramming.wordpress.com/2014/06/13/numpy-vectorized-correlation-coefficient/
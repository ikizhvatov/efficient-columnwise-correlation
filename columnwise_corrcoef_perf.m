% Performance of column-wise correlation coefficient
%
% Requires Statistic and Machine Learning Toolbox
%
% Ilya Kizhvatov

O = randn(100000, 1000);
P = randn(100000, 256);
tic
corr(O, P);
toc
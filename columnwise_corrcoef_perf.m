% Performance of column-wise correlation coefficient
%
% Requires Statistic and Machine Learning Toolbox
%
% Ilya Kizhvatov

% dummy arrays for the dry run
foo = rand(100000, 1000);
bar = rand(100000, 256);

% arrays representing real data
O = randn(100000, 1000);
P = randn(100000, 256);

% dry run
disp('Dry run...')
tic
corr(foo, bar);
toc

% real run
disp('Real run...')
tic
corr(O, P);
toc
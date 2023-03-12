

clear 
close all

%% Obtain cities data

% read in from file
[num, txt, raw] = xlsread('cities.xlsx');

% extract parallel vectors
names = txt(2:end,1);
pop = num(:,1);
lat = num(:,2);
lon = num(:,3);


%% Calculate some basic stastics of the latitude data

[maxLat, iMaxLat] =                  % complete to find the max latitude
[minLat, iMinLat] =                  % complete to find the min latitude
meanLat =                            % complete to find the mean latitude 
medianLat =                          % complete to find the median latitude
[modeLat, freqModeLat] =              % complete to find the mode of the latitudes

disp(['The most northern city is ' names{iMaxLat} ' (' num2str(maxLat) ' deg)']);
disp(['The most southern city is ' names{iMinLat} ' (' num2str(minLat) ' deg)']);
disp(['The mean latitude is ' num2str(meanLat) ' deg']);
disp(['The median latitude is ' num2str(medianLat) ' deg']);
disp(['The mode latitude is ' num2str(modeLat) ' deg']);


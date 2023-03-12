

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

[maxLat, iMaxLat] = max(lat);           % complete to find the max latitude
[minLat, iMinLat] = min(lat);             % complete to find the min latitude
meanLat =   mean(lat);                         % complete to find the mean latitude 
medianLat =  median(lat);                        % complete to find the median latitude
[modeLat, freqModeLat] =  mode(lat);            % complete to find the mode of the latitudes

disp(['The most northern city is ' names{iMaxLat} ' (' num2str(maxLat) ' deg)']);
disp(['The most southern city is ' names{iMinLat} ' (' num2str(minLat) ' deg)']);
disp(['The mean latitude is ' num2str(meanLat) ' deg']);
disp(['The median latitude is ' num2str(medianLat) ' deg']);
disp(['The mode latitude is ' num2str(modeLat) ' deg']);

%% get variance and std dev

lat_var = var(lat);
lat_std = std(lat);

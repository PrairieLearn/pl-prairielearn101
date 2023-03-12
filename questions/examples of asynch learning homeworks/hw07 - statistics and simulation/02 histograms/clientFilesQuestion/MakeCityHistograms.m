%% Clear old data and close figure windows

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


%% Make histogram of cities' latitude

figure();
bins = -100:10:100;
h = histogram(lat,bins);

% change the defaults so the plot is better for a presentation
h.LineWidth = 3;
ax = gca;
ax.FontSize = 20;
grid on;

% add some labels
xlabel('Latitude (deg)');
ylabel('Number of Cities');
title('Distribution of the World''s Most Populous Cities');

% once the figure is generated, you can resize it by grabbing a 
% corner of the window and resizing the window.

%% Make histogram of cities' longitude

figure();
bins = -180:20:180;
h = histogram(lon,bins);

% change the defaults so the plot is better for a presentation
h.LineWidth = 3;
ax = gca;
ax.FontSize = 20;
grid on;

% add some labels
xlabel('Longitude (deg)');
ylabel('Number of Cities');
title('Distribution of the World''s Most Populous Cities');

% once the figure is generated, you can resize it by grabbing a 
% corner of the window and resizing the window.

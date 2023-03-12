% clear out any old data
clear;
clc;
close all;

% load the data!
load('batteryLife.mat');

% create a plot with error bars
h = errorbar(time, batteryMean, batteryStdDev);

% use graphics object (h) to set the line width
set(h,'LineWidth',3);

% add title and axis labels
title('Battery Lifetime Performance');
xlabel('Years of Use');
ylabel('Full-Charge Battery Life (hours)');

% use gca to set properties
ax = gca;
ax.FontSize = 20;
ax.XLim = [0,5];
ax.YLim = [0,3.5];
ax.LineWidth = 2;
grid on;

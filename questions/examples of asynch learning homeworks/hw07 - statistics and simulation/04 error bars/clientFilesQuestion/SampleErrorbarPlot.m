% Make sample errorbar plot

clear
close all

figure();

% make some data
x = 1:4;
y = [5,8,13,9];

% this is the +/- error for each data point
err = [1,2,4,1];

h = errorbar(x, y, err);

% use the graphics object to set the line width
set(h, 'LineWidth', 3); 

% use gca to set properties
ax = gca;
ax.FontSize = 20;
ax.XLim = [0,5];
ax.YLim = [0,20];
ax.LineWidth = 2;
grid on;

print('SampleErrorPlot.png','-dpng');